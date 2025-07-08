import pandas as pd

def compare_row_level(df_source: pd.DataFrame, df_target: pd.DataFrame, key_columns, compare_columns=None):
    if compare_columns is None:
        compare_columns = [col for col in df_source.columns if col in df_target.columns and col not in key_columns]
    merged = df_source.merge(df_target, on=key_columns, suffixes=('_src', '_tgt'), how='outer', indicator=True)
    mismatches = []
    for _, row in merged.iterrows():
        if row['_merge'] != 'both':
            mismatches.append(row)
        else:
            for col in compare_columns:
                if row[f'{col}_src'] != row[f'{col}_tgt']:
                    mismatches.append(row)
                    break
    return pd.DataFrame(mismatches) 