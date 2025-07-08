import argparse
import yaml
import os
from connectors.sql_server import SQLServerConnector
from connectors.snowflake import SnowflakeConnector
from validation.row_level import compare_row_level
from validation.aggregate_level import compare_aggregate_level
from reporting.html_report import generate_html_report


def main():
    parser = argparse.ArgumentParser(description='Data Validation Automation Framework')
    parser.add_argument('--config', required=True, help='Path to YAML config file')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    # Source extraction
    src_conf = config['sources']['sql_server']
    tgt_conf = config['sources']['snowflake']
    src = SQLServerConnector(src_conf['connection_string'])
    df_src = src.fetch_table(src_conf['table'], src_conf.get('columns'))
    tgt = SnowflakeConnector(
        tgt_conf['user'], tgt_conf['password'], tgt_conf['account'],
        tgt_conf['warehouse'], tgt_conf['database'], tgt_conf['schema']
    )
    df_tgt = tgt.fetch_table(tgt_conf['table'], tgt_conf.get('columns'))

    # Validation
    if config['validation']['type'] == 'row_level':
        mismatches = compare_row_level(df_src, df_tgt, src_conf['key_columns'], config['validation'].get('compare_columns'))
    else:
        mismatches = compare_aggregate_level(df_src, df_tgt, src_conf['key_columns'], config['validation'].get('compare_columns'))

    # Reporting
    summary = {
        'total_source_rows': len(df_src),
        'total_target_rows': len(df_tgt),
        'mismatched_rows': len(mismatches),
        'percent_match': 100 * (1 - len(mismatches) / max(len(df_src), 1))
    }
    report_conf = config['report']
    os.makedirs(os.path.dirname(report_conf['output']), exist_ok=True)
    if report_conf['format'] == 'html':
        generate_html_report(mismatches, summary, report_conf['output'])
    else:
        print('Only HTML reporting is implemented in this sample.')
    print(f"Validation complete. Report saved to {report_conf['output']}")

if __name__ == '__main__':
    main() 