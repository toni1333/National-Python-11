import pandas as pd

print(pd.__version__)

# a= {"x":1,"y":7,"z":2}
# # a=[1,7,2]
# variabila=pd.Series(a, index=['x','y'])
# print(variabila)
# # variabila=pd.Series(a,index=a.keys())
# # print(variabila)
# data={
#     "key1": [0,1,2],
#     "key2" : [3,4,7]
# }
# print(data)
#
# variabila =pd.DataFrame(data, index=['linie1','linie2','linie3'])
# print(variabila.loc['linie2'])

# df = pd.read_excel('CursBnrBis.xls')
# for x in df.index:
#     # print(df.loc[x, 'AED'])
#     if float(df.loc[x,"AED"])<1.2:
#         df.drop(x, inplace=True)
# print(df)
# df1= df.to_excel('CursAED.xls')
# print(df.corr())
# print(df.describe())
# variabila= df.describe()
# # variabila= df.describe().to_excel('describe2.xls')
# variabila.to_excel('describe.xls')

import matplotlib.pyplot as plot
# df.plot(kind='scatter', x='AED', y='100 HUF')
# df['AED'].plot(kind='hist')
# plot.show()

# print(df.head(2))
# print(df.tail(3))

df=pd.read_csv('test.csv')
# df.dropna(inplace=True)
df.fillna(0, inplace=True)
# df['AL'].filna(0,inplace=True)
# df.loc[7,'AL']=45
df.replace(':', 0, inplace=True)
df.replace(':', 0, inplace=True)
# print(df)
print(df.transpose())
df.to_excel('test1.xls')
df.transpose().to_excel('test1transpose.xls')