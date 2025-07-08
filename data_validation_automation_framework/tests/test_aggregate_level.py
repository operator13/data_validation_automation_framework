import pandas as pd
from validation.aggregate_level import compare_aggregate_level

def test_compare_aggregate_level():
    df1 = pd.DataFrame({'id': [1,1,2], 'val': [10,20,30]})
    df2 = pd.DataFrame({'id': [1,2], 'val': [30,30]})
    mismatches = compare_aggregate_level(df1, df2, ['id'], ['val'])
    assert not mismatches.empty 