# print("Ana are mere")
# var1 = input("Adauga un numar: ")
# print(var1)
# var1 = 'Ana are \'3\' mere'
# var1 = "Ana are \"3\" mere"
numar_mere = 3
numar_pere = 2
numar_prune = 2
# var1 = f"Ana are {'22' if numar_mere > 4 else '33'} mere {numar_pere}"
# var1 = "Ana are {1} mere si {0} pere".format(numar_mere, numar_pere)
# var1 = "Ana are " + str(numar_mere) + " mere si " + str(numar_pere) + " pere"
# print(var1)


def my_function(a: int, b: int = 0, c: int = 0, *args) -> (int, dict):
    return a + b + c, {'diferenta': a - b - c}


# suma = my_function(b=10, a=5)
# suma, diferenta = my_function(numar_mere, c=numar_pere, b=2)
# print(suma, diferenta)

def suma(a, b, c = 3, *args, **dublu_steluta):
    """
    :param c: al treilea parametru
    :param a: primul parametru
    :param b: al doilea parametru
    :param args: argumente tip tuple
    :param dublu_steluta: argumente tip cheie - valoare
    :return: suma tuturor parametrilor
    """
    total = 0
    variabila_temp = a + b + c
    for i in args:
        total = total + i  # total += i
        # return total
    print(type(dublu_steluta))
    for i, v in dublu_steluta.items():
        print(i, v)
        total = total + v
    # if total == 12:
    #     return 'Gigi'

    return variabila_temp + total
    # print('Ana are mere')

# dictionar = {'nume': 'Ana'}

# variabila = suma(c=4, d=7, e=9, a=1, b=2)


# variabila = suma(1, 2)
# print(variabila)

# var1 = "Ana are {1} mere si {0} pere".format(numar_mere, numar_pere)
# print(var1)

my_var = input('Adauga un numar: ')
try:
    my_int = int(my_var)
    print(my_int)
    # print(variabila_nedefinita)
except NameError:
    print('variabila nu este definita')
    variabila_nedefinita = 0
except ValueError:
    print('eroare de valoare')
except Exception as e:
    print('exceptie', Exception)
else:
    print('nu sunt exceptii')

# print(variabila_nedefinita)