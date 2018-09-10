df = pd.read_csv(r"public.test.csv")
df.drop_duplicates(df.columns.drop('ID'), keep='first', inplace=True)
df.drop(df[(df.电压A > 800) | (df.电压A < 500)].index,inplace=True)
df.drop(df[(df.电压B > 800) | (df.电压B < 500)].index,inplace=True)
df.drop(df[(df.电压C > 800) | (df.电压C < 500)].index,inplace=True)
df.drop(df[(df.现场温度 > 30) | (df.电压B < -30)].index,inplace=True)
df.drop(df[(df.转换效率A > 100)].index,inplace=True)
df.drop(df[(df.转换效率B > 100)].index,inplace=True)
df.drop(df[(df.转换效率C > 100)].index,inplace=True)
df.drop(df[(df.风向 > 360)].index,inplace=True)
df.drop(df[(df.风速 > 20)].index,inplace=True)
df.to_csv('clean.test.csv')
df
df.describe()
这是我处理的噪声


import pandas as pd
origin_result=pd.read_csv('origin_result.csv')#需保留列名
clean_result=pd.read_csv('clean_result.csv')#需保留列名
clean_ID=list(clean_result['ID'])
clean_score=list(clean_result['score'])
for i in range(len(clean_ID)):
    origin_result.loc[origin_result['ID'] == clean_ID[i],'score'] = clean_score[i]
origin_result.drop(origin_result.index)
origin_result.to_csv('result.csv',header=False)