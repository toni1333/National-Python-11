import matplotlib.pyplot as plot
import pandas as pd



description = ('Country', ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 ', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 ', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 ', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']), ]


# am scris tarile "manual"
lista_tari = ['Albania','Austria','Bosnia si Hertegovina','Belgia','Bulgaria',
              'Elvetia','Cipru','Cehia','Germania','Danemarca',
              'Ceuta', 'Estonia', 'Grecia', 'Spania', 'Finlanda',
              'Franta', 'Croatia', 'Ungaria', 'Irlanda', 'Islanda', 'Italia',
              'Lituania','Luxemburg','Letonia','Muntenegru','Macedonia de Nord',
              'Malta', 'Tarile de Jos', 'Norvegia', 'Polonia',
              'Portugalia', 'Romania', 'Serbia', 'Suedia', 'Slovenia',
              'Slovacia', 'Turcia', 'Regatul Unit','Cosovo']


lista_ani = []
lista_data_set = []

for x in description[1]:
    lista_ani.append(x)      #am apenduit anii din description in lista ani
print('1 Lista ani: ',lista_ani)
print('2 Lista Tari: ',lista_tari)
for y in dataset:
    lista_data_set.append(y[1])   # am apenduit lista data din dataset
print('3 Lista data: ', lista_data_set)


lista_goala = []             # aici am inlocuit ":" cu 0
for i in range(len(lista_data_set)):
    for x in lista_data_set[i]:
       if x.strip() == ':':
           x = '0'
           lista_goala.append(x)
       else:
           lista_goala.append(x)
lista_data_set.clear()
for y in range(0,len(lista_goala),9):
        lista_data_set.append(lista_goala[y:y+9])

print("4 lista data set cu zero ", lista_data_set)
print()

global dictionar_final
dictionar_final = {}

lista_medie_g = []


def get_year_data(dataset,an):            # in partea aceasta a codului am lasat asa "desfasurat" sa am amintire
                                          #      cum am inceput sa scriu cod...

    dataset=dataset
    lista_goala=[]
    lista_completare = []
    get_year_data_dict19 = {}
    get_year_data_dict18 = {}
    get_year_data_dict17 = {}
    get_year_data_dict16 = {}
    get_year_data_dict15 = {}
    get_year_data_dict14 = {}
    get_year_data_dict13 = {}
    get_year_data_dict12 = {}
    get_year_data_dict11 = {}

    for x in range(len(lista_data_set)):
        lista_completare.append(lista_data_set[x][8])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict19['2019'] = lista_goala
    lista_goala=[]
    lista_completare=[]

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][7])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict18['2018'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][6])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict17['2017'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][5])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict16['2016'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][4])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict15['2015'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][3])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict14['2014'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][2])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict13['2013'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][1])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict12['2012'] = lista_goala
    lista_goala = []
    lista_completare = []

    for x in range(len(dataset)):
        lista_completare.append(lista_data_set[x][0])
    lista_zip=zip(lista_tari,lista_completare)
    for x in lista_zip:
        lista_goala.append(x)
    get_year_data_dict11['2011'] = lista_goala

    if an == '2019':
        print(get_year_data_dict19)
    elif an == '2018':
        print(get_year_data_dict18)
    elif an == '2017':
        print(get_year_data_dict17)
    elif an == '2016':
        print(get_year_data_dict16)
    elif an == '2015':
        print(get_year_data_dict15)
    elif an == '2014':
        print(get_year_data_dict14)
    elif an == '2013':
        print(get_year_data_dict13)
    elif an == '2012':
        print(get_year_data_dict12)
    elif an == '2011':
        print(get_year_data_dict11)
    else:
        print("Ati introdus un an nevalid, mai incerca-ti intre anii 2011 si 2019")



def get_country_data(dataset,tara):
    dataset = lista_data_set
    dict_tari = {}

    for x in range(len(lista_data_set)):
        dict_tari[lista_tari[x]] = list(zip([x for x in reversed(lista_ani)], [y for y in reversed(lista_data_set[x])]))
    for k,v in dict_tari.items():
        dict_g = {}
        if k == tara:
            dict_g[k] = v
            print(dict_g)





def perform_average(param):
    country_data = {}

    for x in range(len(lista_data_set)):
        country_data[lista_tari[x]] = list([y for y in (lista_data_set[x])])
    for k, v in country_data.items():
        dict_g = {}
        if k == param:
            dict_g[k] = v
            for y in dict_g.values():
                n_int = []
                for i in y:
                    i = int(i)
                    n_int.append(i)
                average = sum(n_int) / len(n_int)
                average = float(average)
                average= "{:.1f}".format(average)  # am limitat dupa virgula sa afiseze o cifra
                print(f"Average for {param} is:", average)


def data_set_include_average():
    lista_goala = [[int(j) for j in i] for i in lista_data_set]
    lista_medie = []
    for x in lista_goala:
        lista_for = x
        suma = sum(lista_for)/len(lista_for)
        lista_medie.append(suma)  #am obtinut in lista_medie toate mediile ale tarilor

    for y in range(len(lista_medie)):
        num_activ = lista_medie[y]
        num_activ = float(num_activ)
        num_activ = "{:.2f}".format(num_activ) #am limitat la 2 cifre dupa virgula
        lista_medie[y] = num_activ
        lista_medie_g.append(lista_medie[y])

    for z in range(len(lista_data_set)):
        lista_data_set[z].append(lista_medie[z])

    print("Lista date cu mediile adaugate pe ultima coloana", lista_data_set)



def create_final_data():
    dict_final = {}
    csv_columns = ["tara","an"]
    for x in range(len(lista_data_set)):
        dict_final[lista_tari[x]] = list(zip([x for x in reversed(lista_ani)], # reversed ca sa fie ca in cerinta 2019,2018...
                                             [y for y in reversed(lista_data_set[x])]))
    for k, v in dict_final.items():
            dict_final[k] = v
            dictionar_final[k] = v
    print("dict_final",dict_final)
    print()















#-----------------------------------------------------------
#  de aici ruleaza programul

get_year_data(dataset,'2019')          # dupa anul ales
get_country_data(dataset,'Romania')    # dupa tara aleasa
perform_average('Romania')             # media pe tara aleasa
create_final_data()                    # am facut un dictionar care sa contina datele tara + date
data_set_include_average()             #am creat o functie care adauga media la finalul coloanei media si am afisat



description_list = list(description)    #salvare date in CSV
value = [ year for year in description[1]]
lista_valori = []
lista_valori.append(description_list[0])
header_csv = lista_valori + value


dictionar_csv = dict(dataset)
dataset_csv = []
for k,v in dictionar_csv.items():
    dataset_csv.append([k]+v)


df = pd.DataFrame(dataset_csv, columns=header_csv)
df.replace(': ', 0, inplace=True)
df.to_csv('temaJson.csv', index=0)
df = pd.read_csv('temaJson.csv')


print("CSV",df)
print()

# df.to_excel('temaJson.xls')

print("Describe")
print(df.describe())
df.plot()                              # Describe


df.plot(kind='scatter', x='AL',y='AT',color='red')
plot.show()


df['RO'].plot(kind='hist')
plot.show()