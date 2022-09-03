from bs4 import BeautifulSoup
import requests
import pandas as pd


req = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')
link = BeautifulSoup(req.text, 'html.parser')       # col1, col2, col3

req_21 = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-21-ianuarie-ora-13-00/')
link_21 = BeautifulSoup(req_21.text, 'html.parser') # col4 link_21 de la data 21.01....

req_22 = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-22-ianuarie-ora-13-00/')
link_22 = BeautifulSoup(req_22.text, 'html.parser') # col5

req_23 = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-23-ianuarie-ora-13-00/')
link_23 = BeautifulSoup(req_23.text, 'html.parser') # col6

req_24 = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-24-ianuarie-ora-13-00/')
link_24 = BeautifulSoup(req_24.text, 'html.parser') # col7

req_25 = requests.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-25-ianuarie-ora-13-00/')
link_25 = BeautifulSoup(req_25.text, 'html.parser') # col8



col1 = []
col2 = []

col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []

head_ = []                # aici am introdus separat doar  "NR CRT", "JUDET", "20.01" ,"21.01"  etc...
total = []                # cuvantul "TOTAL" din site l am "curatat"  avea scris  <p>&nbsp;</p>.. si apenduit la col1
clean = ''

match = link.find_all('tr')       # pentru col1, col2, col3
match4 = link_21.find_all('tr')       # col4
match5 = link_22.find_all('tr')       # col5
match6 = link_23.find_all('tr')       # col6
match7 = link_24.find_all('tr')       # col7
match8 = link_25.find_all('tr')       # col8

match2 = link.find_all('table', attrs={'width': '710'})   # pt head_
for x in match:
    for y in x.find_all('td', attrs={'width': '47'}):
        col1.append(y.text)
del col1[0]               # am sters primul index "NR CRT" si l am pus in head_  si la fel la restul in continuare....

for x in match:
    for z in x.find_all('td', attrs={'width': '151'}):
        col2.append(z.text)
del col2[0]

for x in match:
    for z in x.find_all('td', attrs={'width': '189'}):
        col3.append(z.text)
del col3[0]

for x in match4:
    for z in x.find_all('td', attrs={'width': '189'}):
        col4.append(z.text)
del col4[0]

for x in match5:
    for z in x.find_all('td', attrs={'width': '189'}):
        col5.append(z.text)
del col5[0]

for x in match6:
    for z in x.find_all('td', attrs={'width': '189'}):
        col6.append(z.text)
del col6[0]

for x in match7:
    for z in x.find_all('td', attrs={'width': '189'}):
        col7.append(z.text)
del col7[0]

for x in match8:
    for z in x.find_all('td', attrs={'width': '189'}):
        col8.append(z.text)
del col8[0]


for x in match2:
    for z in x.find_all('strong'):
        head_.append(z.get_text())

for x in match2:                                 # "TOTAL" curatat si apenduit pe col1
    for z in x.find_all('td', attrs={'width': '198'}):
        total.append(z.get_text())

clean = str(total)
clean = clean[6:11]
total = clean
col1.append(total)

head_[2] = '20.01'  # am introdus manual la pozitiile head_ data si luna corespunzatoare......
head_[3] = '21.01'     # head_  pana la index[4] avea date am scris peste...am lasat primele 2 "NR CRT" si "JUDET"
head_[4] = '22.01'   # head_ din for-ul de mai sus avea 4 index-uri si dupa am appenduit...
head_.append('23.01')
head_.append('24.01')
head_.append('25.01')

del col5[43]                        # aici copiaza de pe site caractere garbage pe cele 3 coloane si am sters...
col6=col6[0:44]
col7=col7[0:44]


# aici am reglat lungimea sirurilor sa fie egale , dupa cel mai lung si cele scurte le am umplut cu ' '
#     pt a converti in tabel multidimensional in pandas
max_col=int(len(col1)) ,int(len(col2)), int(len(col3)), int(len(col4)),int(len(col5)), int(len(col6)), int(len(col7)), int(len(col8))
max_col = max(max_col)       # max_col l-am covertit la INT  din tuple...  sa pot lucra la if...

count_reglare = 0
if len(col1) < max_col:
    rez_reglare = (max_col-len(col1))
    for i in range(0,rez_reglare):
        col1.append(' ')

if len(col2) < max_col:
    rez_reglare=(max_col-len(col2))
    for i in range(0,rez_reglare):
        col2.append(' ')

if len(col3) < max_col:
    rez_reglare=(max_col-len(col3))
    for i in range(0,rez_reglare):
        col3.append(' ')

if len(col4) < max_col:
    rez_reglare=(max_col-len(col4))
    for i in range(0,rez_reglare):
        col4.append(' ')

if len(col5) < max_col:
    rez_reglare=(max_col-len(col5))
    for i in range(0,rez_reglare):
        col5.append(' ')

if len(col6) < max_col:
    rez_reglare=(max_col-len(col6))
    for i in range(0,rez_reglare):
        col6.append(' ')

if len(col7) < max_col:
    rez_reglare=(max_col-len(col7))
    for i in range(0,rez_reglare):
        col7.append(' ')

if len(col8) < max_col:
    rez_reglare=(max_col-len(col8))
    for i in range(0,rez_reglare):
        col8.append(' ')



titled_column ={ head_[0] : col1,            # am introdus datele de tip-ul dictionar pt pandas
                 head_[1] : col2,
                 head_[2] : col3,
                 head_[3] : col4,
                 head_[4] : col5,
                 head_[5] : col6,
                 head_[6] : col7,
                 head_[7] : col8,
                 }
data = pd.DataFrame(titled_column)
writer=pd.ExcelWriter('temacovid_.xlsx')            # aici am scris si salvat in Excel, am scos index-ul
data.to_excel(writer,sheet_name='temaCOVID',index=False)
writer.save()

