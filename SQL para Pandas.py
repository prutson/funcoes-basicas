##SQL para Pandas

# Union do sql
#select * from df1 union select * from df2
df_union = pd.concat([df1. df2]).reset_index(drop=True)

# Inner join
#select * from df1 1 inner join df2 2 on 1.key = 2.key
df_join = df1.merge(df2, on = 'key', suffixes=('_1', '_2'))

#Group By
#select var1, count(var2) grupo by var1
counted_df = df.groupby('var1').agg({'var2':'count'})

# Order by
#select va1 order by var1 desc
sorted_df = df.sort_values('var1', ascending = False)
