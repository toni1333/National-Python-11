"""Dezvoltarea unui program care sa calculeze venitul saptamanal al unui angajat"""
"""Venitul saptamanal = venitul/ora * nr ore"""
"""venit_saptamnal = 35 lei * 40 ore"""


# venit saptamanal ----> Float
# venit ora -------> Float
# # nr_ore -----> Float
#
# """  1 obtinem venitul pe ora
#      2 obtinem nr ore lucrate
#      3 calcul venit saptamanal
#      4 afisare rezultate
# """
#
# # venit_pe_ora = float(input("Introduce-ti venitul pe ora:"))
# # # nr_ore =float(input("Introduce-ti nr de ore:"))
# # venit_saptamanal = venit_pe_ora * nr_ore
# # print("Venitul saptamanal este de " + str(venit_saptamanal) + " lei")
#
#
# # teste acasa...
#
# a= 1 ; b= 2 ; c= a % b
# if a is a and b< c:
#     print('True')
# else:
#     print('False')
# print('-\n-\n-')
# print (c)
# print('-\n-\n-')
#
# # s=b"Hello World"
# # n=[1,2,3,4,5,6]
# # # if 'o' in s or 0 in n:
# # #     print('              True ')
# # # else:
# # #     print('              False')
# # print(s)
# #
# #
# # s1=b"Hello World"
# # if s << s1:
# #     print('biti true')
# # else:
# #     print('biti false')
#
#
# a=3
# child_age=3
# print(id(child_age))
#
# print('-\n-\n-')
#
# my_var=100
# my_var >>= 1
# print(my_var)
# print(ord('z'))
# print(chr(33))
#
# print('-\n-\n-')
#
# print('Si Dumnezeu a zis: \"Sa se faca lumina!\"')
#
# print("'\t' aaaa")
# print('-\n-\n-')
#
# print(F"For only {49:.2f} dollars! {1}".format(49 ,'Have a nice day!'))
#
# # print(f"For only {A} dollars! {B}".format(A=49, B='Have a nice day!'))
#
# print('2022 "in litere doua mii.." iar Gigel a zis: \"ma numesc Gigel \"')
# print(""" Gigel a zis: "ma numesc Gigel!"
# """)
#
# my_list= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# my_sliced_list=my_list[2:-5]
# my_sliced_list2=my_list[::]
# print(my_sliced_list2)
# print([].__sizeof__())
# print(a.__sizeof__())
#
# my_dict = {
#     "key" : " value    1"
# }
#
# print(my_dict["key"])
# print(my_dict.get("key_2", "MyValue"))
# print(my_dict)

my_first_list = [ 7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('Lista originala: ', my_first_list)
print('Lista ordonata ascendent: ',sorted(my_first_list))
order_list= sorted(my_first_list)
descendent_list=order_list
descendent_list.reverse()
my_sliced_list_odd=my_first_list[1::1]
print('Lista ordonata descendent: ',descendent_list)
order_list.reverse()
my_sliced_list_even=order_list[1::2]
my_sliced_list_odd=order_list[0::2]
multiply_list=order_list[2::3]
print('lista cu numerele pare din lista: ',my_sliced_list_even)
print('lista cu numerele impare din lista: ',my_sliced_list_odd)
print('lista cu numerele multiplu de 3 din lista: ',multiply_list)
