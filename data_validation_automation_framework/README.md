[![CI](https://github.com/operator13/data_validation_automation_framework/actions/workflows/ci.yml/badge.svg)](https://github.com/operator13/data_validation_automation_framework/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/operator13/data_validation_automation_framework/branch/main/graph/badge.svg)](https://codecov.io/gh/operator13/data_validation_automation_framework)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
[![Last Commit](https://img.shields.io/github/last-commit/operator13/data_validation_automation_framework.svg)](https://github.com/operator13/data_validation_automation_framework/commits/main)
[![Issues](https://img.shields.io/github/issues/operator13/data_validation_automation_framework.svg)](https://github.com/operator13/data_validation_automation_framework/issues)

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

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com/operator13/data_validation_automation_framework.git
   cd data_validation_automation_framework
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your validation:**
   Edit `config/sample_config.yaml` with your connection details and validation rules.
4. **Run validations:**
   ```bash
   python cli.py --config config/sample_config.yaml
   ```
5. **View the report:**
   Open the generated HTML report at the path specified in your config.

## Usage Example
```bash
python cli.py --config config/sample_config.yaml
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT 