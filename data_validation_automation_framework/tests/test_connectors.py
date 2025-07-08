import pytest
from unittest.mock import patch, MagicMock
from connectors.sql_server import SQLServerConnector
from connectors.snowflake import SnowflakeConnector

@patch('connectors.sql_server.sqlalchemy.create_engine')
def test_sql_server_connector_fetch_table(mock_create_engine):
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    connector = SQLServerConnector('dummy_conn_str')
    with patch('connectors.sql_server.pd.read_sql') as mock_read_sql:
        mock_read_sql.return_value = 'df'
        result = connector.fetch_table('table', ['col1', 'col2'], 'col1=1')
        mock_read_sql.assert_called_once()
        assert result == 'df'

@patch('connectors.snowflake.snowflake.connector.connect')
def test_snowflake_connector_fetch_table(mock_connect):
    mock_ctx = MagicMock()
    mock_connect.return_value = mock_ctx
    connector = SnowflakeConnector('user','pass','acct','wh','db','schema')
    with patch('connectors.snowflake.pd.read_sql') as mock_read_sql:
        mock_read_sql.return_value = 'df'
        result = connector.fetch_table('table', ['col1', 'col2'], 'col1=1')
        mock_read_sql.assert_called_once()
        assert result == 'df' 