# Retail Sales Data Engineering Pipeline & Analytics Platform

## Project Overview

This project demonstrates an end-to-end Data Engineering solution for processing retail sales data and generating business insights. The solution covers data ingestion, cleaning, validation, transformation, KPI generation, cloud storage integration, interactive Power BI reporting, and an AI-powered Natural Language to SQL (NL-SQL) analytics agent.

The project was developed as part of the NeoStats Data Engineering Assessment to showcase practical skills in ETL pipeline development, data quality management, analytics engineering, cloud integration, and business intelligence.

---

## Business Objective

Retail organizations generate large volumes of transactional data from multiple channels. Raw data often contains inconsistencies, missing values, duplicates, and sensitive information that reduce its usability for analytics.

The objective of this project is to:

* Build a scalable ETL pipeline
* Clean and validate retail transaction data
* Generate business KPIs
* Create analytics-ready datasets
* Store curated data in AWS S3
* Build interactive Power BI dashboards
* Develop an NL-SQL analytics assistant for business users

---

## Solution Architecture

The solution consists of the following layers:

1. Data Ingestion Layer
2. Data Cleaning Layer
3. Data Quality Validation Layer
4. Data Transformation Layer
5. KPI Generation Layer
6. AWS Cloud Storage Layer
7. Power BI Reporting Layer
8. NL-SQL Analytics Agent Layer

Detailed architecture diagrams are available in the `architecture/` folder.

---

## Technology Stack

### Programming

* Python 3.x
* Pandas
* NumPy

### Data Engineering

* ETL Pipeline
* Data Quality Validation
* Data Transformation
* Star Schema Design

### Cloud

* AWS S3
* Boto3

### Analytics & Visualization

* Power BI Desktop

### AI Analytics

* Streamlit
* SQLite
* Rule-Based NL-SQL Engine

---

## Project Structure

```text
Retail_Data_Engineering_Project/

├── architecture/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── curated/
│   └── kpis/
│
├── documentation/
├── logs/
├── outputs/
├── powerbi/
├── retail_agent/
├── screenshots/
├── src/
│
├── README.md
├── requirements.txt
├── config.py
└── .env.example
```

---

## ETL Workflow

### Step 1 – Data Ingestion

* Load raw retail datasets
* Consolidate source files
* Store raw data for processing

### Step 2 – Data Cleaning

* Handle missing values
* Remove duplicate records
* Standardize formats
* Fix invalid values

### Step 3 – Data Quality Validation

* Completeness checks
* Duplicate validation
* Business rule validation
* Audit reporting

### Step 4 – Data Transformation

* Revenue calculations
* Discount calculations
* Net Revenue calculations
* Date dimension creation
* Feature engineering

### Step 5 – KPI Generation

Generated KPI datasets include:

* Executive Summary
* Product Analysis
* City Analysis
* Customer Analysis
* Payment Analysis
* Time Trend Analysis
* Data Quality Summary

---

## AWS Cloud Integration

Curated retail datasets are uploaded to AWS S3 for cloud-based storage and future analytics integration.

### AWS Services Used

* Amazon S3
* AWS CLI
* Boto3 SDK

### S3 Bucket

```text
retail-data-engineering-keerthana
```

---

## Power BI Dashboard

The Power BI dashboard contains six analytics pages:

### Executive Dashboard

* Total Revenue
* Net Revenue
* Orders
* Customers
* Average Order Value

### Product Analysis

* Revenue by Category
* Product Performance
* Quantity Sold Analysis

### Location Analysis

* Revenue by City
* Order Distribution
* Customer Distribution

### Payment & Channel Analysis

* Payment Method Performance
* Revenue Distribution
* Channel Insights

### Time Trends

* Monthly Revenue Trends
* Order Trends
* Net Revenue Trends

### Data Quality Dashboard

* Data Completeness
* Duplicate Records Removed
* Missing Value Statistics
* Customer Data Masking Validation

---

## NL-SQL Analytics Agent

A Streamlit-based Natural Language to SQL agent allows business users to query retail data using natural language.

### Supported Query Types

* Revenue by City
* Revenue by Category
* Top Customers
* Top Products
* Revenue by Payment Method
* Monthly Revenue
* Pending Payments

### Features

* Automatic SQL generation
* SQLite execution engine
* Interactive visualizations
* Business insights generation

---

## Key Results

### Dataset Statistics

* Total Transactions: 7,914
* Total Customers: 1,960
* Revenue Generated: ₹150.14 Crore
* Net Revenue: ₹116.39 Crore

### Data Quality Improvements

* Missing values corrected
* Duplicate records removed
* Negative value validation applied
* Sensitive customer information masked

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository_url>
cd Retail_Data_Engineering_Project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python src/ingestion.py
python src/data_cleaning.py
python src/data_quality_audit.py
python src/transformation.py
python src/kpi_generation.py
```

### Upload Curated Data to AWS S3

```bash
python src/s3_upload.py
```

### Run NL-SQL Agent

```bash
python retail_agent/create_db.py
streamlit run retail_agent/app.py
```

---
## Repository Contents

- Source code for ETL pipeline
- Data quality audit reports
- KPI generation scripts
- AWS S3 integration
- Power BI dashboard (.pbix)
- NL-SQL analytics agent
- Architecture diagrams
- Complete project documentation

## Documentation

Complete project documentation is available at:

documentation/Retail_Data_Engineering_Documentation.md

---

## Future Enhancements

* Automated workflow orchestration using Apache Airflow
* Real-time streaming pipelines using Kafka
* Cloud Data Warehouse integration
* Generative AI powered SQL generation
* Automated Power BI refresh using cloud services

---

## Author

Keerthana P

Data Engineering | Analytics | AI Applications

---

## License

This project was developed for educational and assessment purposes.
