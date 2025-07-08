# Data Validation Automation Framework

A robust, scriptable, and extensible Python framework for validating data across enterprise data warehouse migrations (e.g., from on-prem SQL Server to Azure/Snowflake).

## Features
- Extract data from SQL Server, Snowflake, and Azure sources
- Row-level and aggregate-level data comparisons
- Configurable table/column mapping and transformation logic
- Structured reporting (HTML, Excel, PDF)
- CI/CD and Azure Data Factory integration ready
- Extensible to new data sources (S3, BigQuery, etc.)
- Placeholder for dbt integration

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your validation in `config/`
3. Run validations: `python cli.py --config config/sample_config.yaml`

## Directory Structure
- `connectors/` - Source connectors (SQL Server, Snowflake, Azure, etc.)
- `validation/` - Validation logic (row/aggregate level)
- `config/` - Config files for mapping and rules
- `reporting/` - Reporting modules (HTML, Excel, PDF)
- `tests/` - Pytest-based test suite
- `cli.py` - Command-line entry point
- `hooks/` - Integration hooks (dbt, ADF, etc.)

## License
MIT 