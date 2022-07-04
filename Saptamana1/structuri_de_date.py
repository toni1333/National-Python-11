# structuri de date
# LISTE - ordonate / mutabile (pot fi modificate, si indexate)
# my_list = [8, 2, 'a', '4']
# print('mesaj')
# print(type(my_list)) # tipul unei variabile
# print(my_list[2])
# print(my_list[3])
# print(my_list[-1])
# print(len(my_list))
# my_list.append('ANA')
# print(my_list)
# print(my_list.index(8))
# my_list.insert(-1, 'A')
# print(my_list[-2: ])
# print(my_list[7:9])
# my_list.append(['A' , 'B', 3, 'x', [4, 7,'w']])
# print(my_list)
# print(my_list[7][4][2])
# print(my_list[7:8])
# print(len(my_list))
# print(my_list[len(my_list)-1])
# print(my_list)
# lista_1 = [2,3]
# lista_2 = [5,6]
# lista_3 = lista_2 + lista_1
# print(lista_3)
# # TUPLURI - ordonate / immutabile (nu poate fi modificat)
#
# my_tuple = (8, 2, 'a' ,8, '4')
# zilele_anului= ('luni')
# zilele_anului=tuple()
# print(type(zilele_anului))
# lista_1= (1, )
lista_1 = ('George', 'Ion' , 'Mihai')
# lista_2 = list(lista_1)
# lista_2[1]= 'Razvan'
# lista_1 =tuple(lista_2)
# print(lista_1)
# # print(type(lista_1))
# print(lista_1[1])
# lista_2 =('Razvan', )
# lista_1 += lista_2
# print(lista_1)

# lista_1 = ('George', 'Ion', 'Mihai')
# (name_1, name_2, name_3) = lista_1
# print(name_1)
# print(name_2)
#
# choices = [(40, 'Bucuresti'), ]

lista_1 = ('Ana', 'Ion', 'Mihai', 'Bogdan', 'Ovidiu')
(name_1, *name_2, name_3) = lista_1
print(name_1)
print(name_2)
print(name_3)