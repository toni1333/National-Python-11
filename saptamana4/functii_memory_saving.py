# # # #functii lambda - se mai numesc si functii fara nume fara definire sau anonime
# # #
# # # element = lambda x: x*10 # unde x este arg si x *10 e expresia
# # #
# # # # def element(x):
# # # #     return x*10
# # #
# # # element_2 = lambda X, Y: X+ Y
# # #
# # #
# # # """ FILTER"""
# # #
# # # # PROGR CARE SA RETURNEZE O LISTA CU NR PARE DINTR O LISTA INITIALA
# # # # functia filter intoarce un obiect al clasei filter care e un iterator rez prin aplic unei fnct fiercarui elem dintr un obiect lista tuplu set etc...
# # list_1 = [1,5,4,6,8,11,3,12]
# # # # list_2=list(filter(lambda x: (x % 2 == 0), list_1))
# # # # print(list_2)
# # #
# # # # ex cu loop:
# # # lista_forloop = []
# # # for i in list_1:
# # #     if i % 2 == 0:
# # #         lista_forloop.append(i)
# # # print(lista_forloop)
# # #
# # # #ex cu funct clasica:
# # #
# # # def filtrare(var):
# # #     if var % 2 == 0:
# # #         return True
# # #     else:
# # #         return False
# # #
# # #
# # # filtered = filter(filtrare, list_1)
# # # print(list(filtered))
# # #
# # #
# # # """MAP"""
# #
# #
# # list_3=list(map(lambda x: x*2, list_1))
# # print(list_3)
# #
# # """ZIP"""
# #
# # list_with_int = [1,2,3,4]
# # list_with_str = ['one', 'two', 'three', 'four']
# # # list_with_decimal = [1.1, 2.2 ,3.3, 4.4]
# #
# # result =zip(list_with_int, list_with_str,""" list_with_decimal""")
# # print(result)
# # # result_list = list(result)
# # # print(result_list)
# #
# # val_1, val_2,val_3 = zip(*result)
# # print('val_1= ',val_1)
# # print('val_2= ',val_2)
# # print('val_3= ',val_3)
# #
# # print(val_3)
# #
# # """COMPREHENSION LIST"""
# # CASE LOOP
# var = 'comprehension'
# list_for_loop = []
# for character in var:
#     list_for_loop.append(character)
# print(list_for_loop)
#
# # CASE LAMBDA
# list_map = list(map(lambda x: x, var))
# print(list_map)
#
# # CASE COMPREHENSION
# list_string = [character for character in var] # expresie for item in lista
# print(list_string)
#
# number_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0 if 20 <=x <= 70]
# print(number_list)
#
# obj = ['par' if i %2 ==0 else 'impar' for i in range(10)]
# print(obj)
#
#
# COMPREHENSION DICTIONARY

# my_dict = {1: "car", 2: 'bike'}
square_dict = dict()
for num in range(1,11):
    square_dict[num] = num*num
print(square_dict)

square_dict = {num: num*num for num in range(1,11)}
print(square_dict)