# print('Ana are mere')

# var1 = input ('Adauga un numar: ')
# print('var1')
# numar_mere = 3
# numar_pere = 2
# var1 = f"Ana are {numar_mere} mere "
# var1 = "Ana are \'3\' mere"
# var1 = "Ana are {1} mere si {1} pere".format(numar_mere, numar_pere)
# var1 = "Ana are " + str(numar_mere) + " mere si " + str(numar_pere) + " pere "
# print(var1)

def my_function(a:int=0, b:int=0, c:int=0, *args) -> (int, dict):
    return a + b + c, {'diferenta' : a- b- c}

# suma, diferenta = my_function( 4, c=3, b=2)
# print(suma, diferenta)

def suma(a, b,*args, **kwargs):

    '''

    :param a:
    :param b:
    :param args:
    :param kwargs:
    :return:
    '''

    total = 0
    var_temp = a+b
    for i, v in kwargs.items():
        print(i,v)
        total = total + v
        total += i
        # if total == 12:
        #     return 'Gigi'
        return var_temp + total
        # print('Ana are mere')

# variabila = suma(1,2, c=4 , d=7, e=9, f=3, g=4,k=5)
# print(variabila)

my_var = input('Adauga un numar: ')
try:
    my_int = int(my_var)
    print(my_int)
except Excwprion as e:
    print('exceptie', e)