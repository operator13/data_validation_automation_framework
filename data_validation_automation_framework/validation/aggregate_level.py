import pandas as pd

def compare_aggregate_level(df_source: pd.DataFrame, df_target: pd.DataFrame, group_by_columns, agg_columns):
    agg_funcs = {col: 'sum' for col in agg_columns}
    src_agg = df_source.groupby(group_by_columns).agg(agg_funcs).reset_index()
    tgt_agg = df_target.groupby(group_by_columns).agg(agg_funcs).reset_index()
    merged = src_agg.merge(tgt_agg, on=group_by_columns, suffixes=('_src', '_tgt'), how='outer', indicator=True)
    mismatches = []
    for _, row in merged.iterrows():
        if row['_merge'] != 'both':
            mismatches.append(row)
        else:
            for col in agg_columns:
                if row[f'{col}_src'] != row[f'{col}_tgt']:
                    mismatches.append(row)
                    break
    return pd.DataFrame(mismatches) 