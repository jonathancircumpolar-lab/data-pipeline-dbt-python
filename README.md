# Data pipeline: dbt + Python (+ R, Power BI)

A learning project simulating a field-data pipeline (agents, sites, missions), built with synthetic data only - no real HIDS/PARF2 data is used.

## Purpose

Built to close a specific skills gap (dbt, R) for a Werkstudent Data/BI analytics role requiring R, SQL, dbt, and Python. SQL was already a solid skill; this project demonstrates hands-on dbt and Python analysis, plus working knowledge of R (reading/adapting existing scripts, not from-scratch proficiency).

## Architecture

Synthetic seeds (CSV) -> dbt staging (cleaning) -> dbt marts (aggregation, tested) -> DuckDB -> consumed by Python (pandas/matplotlib) and exported (CSV/Parquet) for R and Power BI.

## Stack

- dbt-core + DuckDB: transformation, testing, documentation
- Python (pandas, numpy, matplotlib, duckdb): direct analysis on the mart
- R: reading/adapting an existing script (not built from scratch) - read a CSV export, adapted the aggregation key from status to site
- Power BI: Parquet import, stacked bar chart by site and status (no live connector - none stable exists for DuckDB)

## Status

| Component | Status |
|---|---|
| dbt pipeline (seeds, staging, tests, mart) | Done |
| dbt documentation (dbt docs generate) | Done |
| Python analysis + export | Done |
| R script | Done - reads dbt export, adapted aggregation key |
| Power BI report | Done - see powerbi/dashboard_screenshot.png |

## Honesty note

This is a self-directed learning project on synthetic data, not professional production experience. R and Power BI are intentionally scoped narrow - see Stack section above for exact skill level claimed.

