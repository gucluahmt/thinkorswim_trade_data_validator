# Trade Analytics Pipeline

This project simulates a robust trade analytics pipeline inspired by trading platforms. It replicates real-world trading data scenarios to enable validation, anomaly detection, and analytical insights using Python.

As a Business /Data Analyst, I designed this solution to reflect production-level data quality checks and to empower QA teams, developers, and business users with actionable reporting and traceability.

---
## How It Works

1. **Data Generation**: Realistic trade orders are generated with varied types (Market, Limit, Stop), statuses, and quantities using custom Python scripts.
2. **Execution Analysis**: Anomalies such as high quantity + pending status are flagged using `lambda` and `np.where()` logic.
3. **Validation Check**: Zero-quantity executions and unknown statuses are filtered for QA reporting.
4. **Report Output**: Clean CSV files are exported to support QA or dashboard integration.


## 🚀 Project Objectives

- Simulate trade order execution logs for various order types (Market, Limit, Stop)
- Generate realistic large datasets (1000+ entries)
- Analyze execution behavior, status ratios, and unique symbol distribution
- Validate data consistency: check for missing status values and zero-quantity executions
- Flag unusual conditions like:
  - High quantity but still "Pending"
  - High price but "Cancelled"
- Export ready-to-use reports for QA or dashboard pipelines

---
## Setup & Installation

1. Clone this repository:
```bash
git clone https://github.com/gucluahmt/thinkorswim_trade_data_validator.git
cd thinkorswim_trade_data_validator

## 🧠 Technologies Used

- Python 3.12  
- Pandas  
- NumPy (if needed)  
- Modular scripting with CSV export for QA visibility

---

## 🧩 Folder Structure

---


As a Business Analyst, I designed the full pipeline and took ownership of:

- Defining validation rules for order execution data  
- Writing Python-based logic to simulate real trading behavior  
- Identifying inconsistencies and flagging edge cases  
- Exporting findings in clean CSV format for use in QA or dashboards  
- Structuring the project for future extension (SQL, API, ML-ready)

---

✅ **This solution showcases real-world data validation and anomaly detection logic that can easily scale into institutional trading systems.**

## Sample Output

Example flagged data for invalid executions and suspicious trades is exported as:

- `flagged_order_summary.csv`
- `invalid_quantity_executions.csv`
- `invalid_status_entries.csv`
