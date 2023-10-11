# SQL para Pandas

## Union do sql
`#select * from df1 union select * from df2`
```
df_union = pd.concat([df1. df2]).reset_index(drop=True)
```

## Inner join
`#select * from df1 1 inner join df2 2 on 1.key = 2.key`
```
df_join = df1.merge(df2, on = 'key', suffixes=('_1', '_2'))
```

## Inner join com duas clausulas 
`#select * from df1 1 inner join df2 2 on 1.key1 = 2.key1 and 1.key2 = 2.key2`
```
df_join = df1.merge(df2, on = ['key1', 'key2'], suffixes=('_1', '_2'))
```

## Count Group By
`#select var1, count(var2) grupo by var1`
```
counted_df = df.groupby('var1').agg({'var2':'count'})
```

## AVG Group By
`#select var1, count(var2) grupo by var1`
```
counted_df = df.groupby('var1').agg({'var2':'median'})
```

## Order by
`#select va1 order by var1 desc`
```
sorted_df = df.sort_values('var1', ascending = False)
```
