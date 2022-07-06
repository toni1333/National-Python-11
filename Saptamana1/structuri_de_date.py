# # structuri de date
# # LISTE - ordonate / mutabile (pot fi modificate, si indexate)
# my_list = [8, 2, 'a', '4']
# # print('mesaj')
# # print(type(my_list)) # tipul unei variabile
# # print(my_list[2])
# # print(my_list[3])
# # print(my_list[-1])
# # print(len(my_list))
# # my_list.append('ANA')
# # print(my_list)
# # print(my_list.index(8))
# # my_list.insert(-1, 'A')
# # print(my_list[-2: ])
# # print(my_list[7:9])
# # my_list.append(['A' , 'B', 3, 'x', [4, 7,'w']])
# # print(my_list)
# # print(my_list[7][4][2])
# # print(my_list[7:8])
# # print(len(my_list))
# # print(my_list[len(my_list)-1])
# # print(my_list)
# # lista_1 = [2,3]
# # lista_2 = [5,6]
# # lista_3 = lista_2 + lista_1
# # print(lista_3)
# # # TUPLURI - ordonate / immutabile (nu poate fi modificat)
# #
# # my_tuple = (8, 2, 'a' ,8, '4')
# # zilele_anului= ('luni')
# # zilele_anului=tuple()
# # print(type(zilele_anului))
# # lista_1= (1, )
# # lista_1 = ('George', 'Ion' , 'Mihai')
# # lista_2 = list(lista_1)
# # print(lista_2)
# # lista_2[1]= 'Razvan'
# # lista_1 =tuple(lista_2)
# # print(lista_1)
# # # print(type(lista_1))
# # print(lista_1[1])
# # lista_2 =('Razvan', )
# # lista_1 += lista_2
# # print(lista_1)
#
# # lista_1 = ('George', 'Ion', 'Mihai')
# # (name_1, name_2, name_3) = lista_1
# # print(name_1)
# # print(name_2)
# #
# # choices = [(40, 'Bucuresti'), ]
#
# # lista_1 = ('Ana', 'Ion', 'Mihai', 'Bogdan', 'Ovidiu')
# # (name_1, *name_2, name_3) = lista_1
# # print(name_1)
# # print(name_2)
# # print(name_3)
#
# # SET-uri  neordonate si immutabile (nu pot fi indexate)
#
# # set_1 = {'mar', 'para', 'banana'}
# # # set_1.remove('banana') # aici da erroare daca nu gaseste elementul "banana"
# # # set_1.discard('banana')
# # set_1.pop()
# # set_1.clear()
# #
# # print(set_1)
# # new_set = set(my_list)
# # print(new_set)
#
# # DICTIONAR ordonat si mutabil
# # dict_1 = dict()
# # dict_1 = {"key" : "valoare", 3 : 'u', 4 : None }
# # print(len(dict_1))
# # k=dict_1.keys()
# # print(k)
# # val= dict_1.values()
# # print(val)
# # items= dict_1.items()
# # print(items)
# # dict_1[3]='Gigel'
# # dict_1.update({100: (2,4)})
# # dict_1.popitem()
# # dict_1.clear()
# # dict_1.__delitem__(4)
#
# # print(dict_1)
# #
# #
# # # CONDITIONARI
# #
# # # varsta = int(input("Va rugam sa introduce-ti varsta dumneavoastra: "))
# # # if varsta >= 18:
# # #     print("Sunteti major!!!")
# # # elif varsta == 17:
# # #         print("Mai aveti un an pana la majorat")
# # # else:
# # #     print("Nu sunteti major")
# # varsta_1 = True
# # print(varsta_1)
#
# # WHILE  bucle repetitiva
#
# # print("primul print")
# # i =0
# # while i < 3:
# #     print("se respecta conditia")
# #     print("valoarea este: "+ str(i))
# #     i+=1
# # print("am ajuns la sfarsit")
#
#
# # FOR
# # list_a =[]
# # list_1 =[ 1, 4 , 8, 'w']
# # for i in list_1:
# #     i+=1
# #     list_a.append(i)
# #     print(list_a)
#
#
# my_var = 7
# # mesaj = "Set instructiuni #3"
# # if my_var < 6:
# #     mesaj = "Set instructiuni #1"
# # else:
# #     mesaj= "Set instructiuni #2"
# #
# # print(my_var, mesaj)
#
# # mesaj = "set instructiuni 1" if my_var < 6 else "set instructiuni 2"
# # print(my_list, mesaj)
#
# # a= 1
# # b=2
# # impartire=0
# #
# # if a>0 and b >0 and ( impartire := a/b) and impartire >1:
# #     print(impartire)
# # sir = "Ana are mere"
# # sir1 =list(sir)
# # print(sir1)
# #
# # # for i, v in enumerate(sir):
# # #     print(i, "==>", v)
# #
# # for variabila_temporara in range(0, len(sir)):
# #     print(variabila_temporara, '==>',  sir[variabila_temporara])
#
#
# dictionar= { '1' : 'val1', '2': 'val2', '3': 'val3', '2': 'val22'}
# # print(dictionar['2'])
# # print(dictionar.get("4",'val4'))
# # dictionar.update({4: 'val44'})
# # dictionar[5]= 'val5'
# # for i in dictionar.items():
# #     # print(i)
# #     index, value = i
# #     print(i, index,'==>', value)
# # # print(dictionar)
#
# for i in dictionar:
#     print(i, '==>', dictionar[i])
# # print(dictionar)