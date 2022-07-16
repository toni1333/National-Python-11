def validare_variabile(variabila):
    while variabila.isdigit() is False:
        variabila = int("Reintrodu numar: ")
    return int(variabila)


def validare_operator(operator):
    while operator not in ['+', '-', '*', '/']:
        operator = input('Reintrodu operatorul: ')
    return operator


def calculator(a, b, c):
    """
    :param a: primul nr
    :param b: al doilea nr
    :param c: operatorul ( + - * /)
    :return: calculeaza operatia dintre doua numere
    """
    if c == '+':
        return a + b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    else:
        while b == 0:
          b = validare_variabile(input('Ati incercat sa imparti la 0! Introdu un numar diferit de 0: '))
        return a/b
    print('Nu ati selectat operatorul corect')
    return True

primul_numar = validare_variabile(input("Numar: "))

al_doilea_numar = validare_variabile(input("Numar: "))

operator = input ('Operator: ')

total = calculator(primul_numar, al_doilea_numar, operator )
print(f"Rezultatul este: {total}")
