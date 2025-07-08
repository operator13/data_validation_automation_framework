import pandas as pd
import sqlalchemy

class SQLServerConnector:
    def __init__(self, connection_string):
        self.engine = sqlalchemy.create_engine(connection_string)

    def fetch_table(self, table_name, columns=None, where=None):
        cols = ', '.join(columns) if columns else '*'
        query = f"SELECT {cols} FROM {table_name}"
        if where:
            query += f" WHERE {where}"
        return pd.read_sql(query, self.engine) 