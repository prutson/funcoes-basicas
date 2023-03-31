##SQL para Pandas

#Union do sql
df_union = pd.concat([df1. df2]).reset_index(drop=True)

#Inner join
df_join = df1.merge(df2, on = 'key')

#One to many
df_join = df1.merge(df2, on = 'key', suffixes=('_key', '_key'))

#select var1, count(var2) grupo by var1
counted_df = df.groupby('var1').agg({'var2':'count'})

#select va1 order by var1 desc
sorted_df = df.sort_values('var1', ascending = False)
