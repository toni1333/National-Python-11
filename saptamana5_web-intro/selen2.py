from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pandas import ExcelWriter
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.bnr.ro/files/xml/nbrfxrates2021.htm')
table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
# print(table_head.text)
table_body= driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/tbody')
# print(table_body.text)

header=table_head.text.split('\n')
body= table_body.text.split('\n')
print(len(header))
print(len(body))
print(header)
print(body)
#Tabel generat pe randuri
# body_rows=[]
# counter= 0
# for i in range(0, len(body), len(header)):
#     counter= i
#     body_rows.append(body[counter: counter+len(header)])

    # Tabel generat pe coloane:
body_columns =[]
    # for i in range(len(header)):
    #     body_columns.append({i:[]})

body_columns={key: [] for key in range(len(header))}
body_columns_list = len(body_columns)
counter2= 0
for j in body:
    body_columns[counter2 % body_columns_list].append(j)
    counter2+=1
df=pd.DataFrame(body_columns)
df.to_excel("CursBnrbis.xls", header=header)
driver.close()
# with ExcelWriter('TABEL2_BNR_2021.xlsx') as writer:
#     df.to_excel(writer,header= header, index=0)

# # print(body_rows, '*************')
# df = pd.DataFrame(body_rows,columns=header)
# with ExcelWriter('TABEL_BNR_2021.xlsx') as writer:
#     df.to_excel(writer, index=0)


