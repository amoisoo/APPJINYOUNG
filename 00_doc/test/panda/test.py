
#https://nittaku.tistory.com/258


import pandas as pd
#pip install xlrd

data = pd.read_excel( 'panda.xls' , sheet_name= 'Sheet1' )
print(data.shape)
data.to_csv('./pandas_csv.csv',index=False)

print(data.head())

print(data.head())

#print(data.tail())
#from openpyxl import load_workbook



