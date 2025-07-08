import pandas as pd
from validation.row_level import compare_row_level

def test_compare_row_level():
    df1 = pd.DataFrame({'id': [1,2], 'val': [10,20]})
    df2 = pd.DataFrame({'id': [1,2], 'val': [10,21]})
    mismatches = compare_row_level(df1, df2, ['id'], ['val'])
    assert not mismatches.empty 