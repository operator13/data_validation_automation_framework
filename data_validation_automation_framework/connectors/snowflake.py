import pandas as pd
import snowflake.connector

class SnowflakeConnector:
    def __init__(self, user, password, account, warehouse, database, schema):
        self.ctx = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )

    def fetch_table(self, table_name, columns=None, where=None):
        cols = ', '.join(columns) if columns else '*'
        query = f"SELECT {cols} FROM {table_name}"
        if where:
            query += f" WHERE {where}"
        return pd.read_sql(query, self.ctx) 