-- OPTIONAL / PAID. Not on the free desk (docs/data-cleaning.md, config/quota.yaml).
-- Do not schedule this. T3/T4 definition only, for if a warehouse is ever purchased.
--
-- Agent-economy quality panel on Allium crosschain.agents
-- Native unit: one x402 token transfer.
-- from_address = buyer, to_address = seller, transaction_from_address = facilitator.
-- usd_amount is Allium's USD column (not amount_usd).
-- T0..T4 + Service Spend: docs/agent-economy-monitoring-playbook.md §3
-- Make vs buy: docs/data-cleaning.md
--   Buy T1: NOT is_inorganic (self-pay OR 24h reciprocal return).
--   Own: drop is_agent_economy_circulation (ACP notional ≠ Service Spend),
--        then T2 facilitator EOAs, T3 named catalog, T4 repeat.
-- Allium does not flag high-frequency buyers or A→B→C rings.
-- Do not publish T0 or Allium "organic" as GMV.

WITH params AS (
  SELECT
    CURRENT_DATE - INTERVAL '60 days' AS start_date,
    CURRENT_DATE AS end_date,
    3 AS repeat_min_days,
    5 AS repeat_min_txs
),

t0 AS (
  SELECT
    t.chain,
    t.block_timestamp,
    DATE(t.block_timestamp) AS activity_date,
    LOWER(t.from_address) AS buyer,
    LOWER(t.to_address) AS seller,
    LOWER(t.transaction_from_address) AS facilitator_eoa,
    t.usd_amount AS amount_usd,
    t.transaction_hash AS tx_hash,
    COALESCE(t.is_inorganic, FALSE) AS is_inorganic,
    COALESCE(t.is_agent_economy_circulation, FALSE) AS is_agent_economy_circulation
  FROM crosschain.agents.x402_transfers_adjusted t
  CROSS JOIN params p
  WHERE DATE(t.block_timestamp) BETWEEN p.start_date AND p.end_date
),

facilitator_eoas AS (
  SELECT DISTINCT LOWER(wallet_address) AS eoa
  FROM crosschain.agents.x402_facilitators
),

named_servers AS (
  SELECT
    LOWER(payment_address) AS seller,
    origin,
    category
  FROM crosschain.agents.x402_servers
  WHERE origin IS NOT NULL
),

t1 AS (
  -- Vendor hygiene minus ACP circulation. This is still not T3 Service Spend.
  SELECT t0.*
  FROM t0
  WHERE t0.buyer <> t0.seller
    AND t0.amount_usd > 0
    AND NOT t0.is_inorganic
    AND NOT t0.is_agent_economy_circulation
),

t2 AS (
  SELECT t1.*
  FROM t1
  LEFT JOIN facilitator_eoas fb ON fb.eoa = t1.buyer
  LEFT JOIN facilitator_eoas fs ON fs.eoa = t1.seller
  WHERE fb.eoa IS NULL
    AND fs.eoa IS NULL
),

t3 AS (
  SELECT t2.*, s.origin, s.category
  FROM t2
  INNER JOIN named_servers s ON s.seller = t2.seller
),

buyer_activity AS (
  SELECT
    buyer,
    COUNT(DISTINCT activity_date) AS active_days,
    COUNT(*) AS txs
  FROM t3
  GROUP BY 1
),

t4 AS (
  SELECT t3.*
  FROM t3
  INNER JOIN buyer_activity b
    ON b.buyer = t3.buyer
  CROSS JOIN params p
  WHERE b.active_days >= p.repeat_min_days
    AND b.txs >= p.repeat_min_txs
),

daily AS (
  SELECT
    activity_date,
    COUNT(*) AS t0_txs,
    SUM(amount_usd) AS t0_usd
  FROM t0
  GROUP BY 1
),

daily_t2 AS (
  SELECT
    activity_date,
    COUNT(*) AS t2_txs,
    SUM(amount_usd) AS t2_usd,
    COUNT(DISTINCT buyer) AS t2_payers,
    COUNT(DISTINCT seller) AS t2_payees
  FROM t2
  GROUP BY 1
),

daily_t3 AS (
  SELECT
    activity_date,
    COUNT(*) AS t3_txs,
    SUM(amount_usd) AS t3_usd,
    COUNT(DISTINCT buyer) AS t3_payers,
    COUNT(DISTINCT seller) AS t3_payees
  FROM t3
  GROUP BY 1
),

daily_t4 AS (
  SELECT
    activity_date,
    COUNT(*) AS t4_txs,
    SUM(amount_usd) AS t4_usd,
    COUNT(DISTINCT buyer) AS t4_payers,
    COUNT(DISTINCT seller) AS t4_payees
  FROM t4
  GROUP BY 1
),

ticket_mix AS (
  SELECT
    activity_date,
    SUM(CASE WHEN amount_usd < 0.10 THEN amount_usd ELSE 0 END)
      / NULLIF(SUM(amount_usd), 0) AS share_lt_10c,
    SUM(CASE WHEN amount_usd >= 0.10 AND amount_usd < 1 THEN amount_usd ELSE 0 END)
      / NULLIF(SUM(amount_usd), 0) AS share_10c_1,
    SUM(CASE WHEN amount_usd >= 1 AND amount_usd < 10 THEN amount_usd ELSE 0 END)
      / NULLIF(SUM(amount_usd), 0) AS share_1_10,
    SUM(CASE WHEN amount_usd >= 10 THEN amount_usd ELSE 0 END)
      / NULLIF(SUM(amount_usd), 0) AS share_10plus
  FROM t2
  GROUP BY 1
),

buyer_share AS (
  SELECT
    activity_date,
    SUM(CASE WHEN buyer_rank_pct <= 0.01 THEN usd ELSE 0 END)
      / NULLIF(SUM(usd), 0) AS top1pct_buyer_share
  FROM (
    SELECT
      activity_date,
      buyer,
      usd,
      CUME_DIST() OVER (PARTITION BY activity_date ORDER BY usd DESC) AS buyer_rank_pct
    FROM (
      SELECT activity_date, buyer, SUM(amount_usd) AS usd
      FROM t2
      GROUP BY 1, 2
    ) b
  ) ranked
  GROUP BY 1
),

chain_share AS (
  SELECT
    activity_date,
    chain,
    SUM(amount_usd) AS t2_usd,
    SUM(amount_usd) / NULLIF(SUM(SUM(amount_usd)) OVER (PARTITION BY activity_date), 0)
      AS t2_usd_share
  FROM t2
  GROUP BY 1, 2
)

SELECT
  d.activity_date,
  d.t0_txs,
  d.t0_usd,
  t2.t2_txs,
  t2.t2_usd,
  t2.t2_payers,
  t2.t2_payees,
  t3.t3_txs,
  t3.t3_usd,
  t3.t3_payers,
  t3.t3_payees,
  t4.t4_txs,
  t4.t4_usd,
  t4.t4_payers,
  t4.t4_payees,
  t3.t3_usd / NULLIF(t2.t2_usd, 0) AS t3_share_of_t2,
  t2.t2_usd / NULLIF(t2.t2_txs, 0) AS t2_avg_ticket,
  tm.share_lt_10c,
  tm.share_10c_1,
  tm.share_1_10,
  tm.share_10plus,
  bs.top1pct_buyer_share
FROM daily d
LEFT JOIN daily_t2 t2 USING (activity_date)
LEFT JOIN daily_t3 t3 USING (activity_date)
LEFT JOIN daily_t4 t4 USING (activity_date)
LEFT JOIN ticket_mix tm USING (activity_date)
LEFT JOIN buyer_share bs USING (activity_date)
ORDER BY d.activity_date DESC;

-- Companion: new named origins in the last 7 days (S2).
-- SELECT origin, category, COUNT(*) AS txs, SUM(amount_usd) AS t3_usd
-- FROM t3
-- WHERE activity_date >= CURRENT_DATE - INTERVAL '7 days'
-- GROUP BY 1, 2
-- ORDER BY t3_usd DESC;

-- Companion: chain share of T2 USD (C1). Never use T0 tx share for chain flips.
-- SELECT * FROM chain_share WHERE activity_date >= CURRENT_DATE - INTERVAL '14 days';
