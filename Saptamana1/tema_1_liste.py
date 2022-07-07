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
