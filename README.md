# Data pipeline: dbt + Python (+ R, Power BI)

A learning project simulating a field-data pipeline (agents, sites, missions), 
built with **synthetic data only** — no real HIDS/PARF2 data is used.

## Purpose

Built to close a specific skills gap (dbt, R) for a Werkstudent Data/BI 
analytics role requiring R, SQL, dbt, and Python. SQL was already a solid 
skill; this project demonstrates hands-on dbt and Python analysis, plus 
working knowledge of R (reading/adapting existing scripts, not from-scratch 
proficiency).

## Architecture

Synthetic seeds (CSV) → dbt staging (cleaning) → dbt marts (aggregation, 
tested) → DuckDB → consumed by Python (pandas/matplotlib) and exported 
(CSV/Parquet) for R and Power BI.

## Stack

- **dbt-core + DuckDB**: transformation, testing, documentation
- **Python** (pandas, numpy, matplotlib, duckdb): direct analysis on the mart
- **R**: in progress — reading/adapting an existing script, not built from scratch
- **Power BI**: in progress — Parquet import, no live connector (none stable exists for