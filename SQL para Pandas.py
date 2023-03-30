##SQL para Pandas

#Union do sql
df_union = pd.concat([df1. df2]).reset_index(drop=True)

#Inner join
df_join = df1.merge(df2, on = 'key')
