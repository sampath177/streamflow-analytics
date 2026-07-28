# StreamFlow Analytics

A production-style Data Engineering project inspired by modern streaming platforms like Netflix.

## Project Overview

This project simulates an end-to-end analytics pipeline for a streaming platform. It demonstrates how raw user activity data flows through a modern data engineering architecture to produce business-ready analytics.

## Tech Stack

- Python
- Apache Airflow
- PySpark
- Google BigQuery
- DBT
- Looker Studio
- Docker
- Git & GitHub

## Planned Architecture

```
Raw Data
    │
    ▼
Apache Airflow
    │
    ▼
PySpark Transformations
    │
    ▼
BigQuery (Raw → Silver)
    │
    ▼
DBT (Gold Layer)
    │
    ▼
Looker Studio Dashboard
```

## Project Structure

```
streamflow-analytics/
├── airflow/
├── data/
├── dbt/
├── docs/
├── notebooks/
├── src/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Status

🚧 Project Setup in Progress

---

Built for learning, portfolio development, and interview preparation.