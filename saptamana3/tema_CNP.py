import  datetime


def validare(variabila):
    """
    :param variabila: CNP introd de utiliz de la tast
    :return: CNP valid
    """
    while len(variabila) != 13 or variabila.isdigit() is False:
        variabila = input("Reintrodu CNP-ul: ")
    return variabila


def validare_sex(a):
    if int(a[0]) in range(1, 10):
        return  True
    return False


def validare_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return  True
    except Exception:
        return False


def validare_judet(cnp):
    judet = int(cnp[7:9])
    if judet < 47 or judet in [51, 52]:
        return True
    return False


def numar_trei_cifre(cnp):
    cifre = int(cnp[9:12])
    if cifre >= 1 and cifre < 999:
        return True
    return False


def validator_cnp(cnp):
    """
    :param cnp: cnp -ul introdus de util de la tastatura
    :return: mesaj "Valid" in cazul in care CNP -ul este valid, "Invalid" in cazul in care nu e valid CNP -ul
    """
    if cnp and validare_sex(cnp) and validare_data_nastere(cnp) \
            and validare_judet(cnp) and numar_trei_cifre(cnp):
        return "Valid"
    return "Invalid"


def cifra_de_control():
    # CIFRA DE CONTROL - ultima parte a ValidatoruluiCNP
    print('=' * 40)
    print('CNP-ul dat initial: "279146358279" ')
    cnp_fara_n = variabila_cnp[0:12] # cnp este variabila_cnp fara ultima cifra
    print(cnp_fara_n)
    cnp_explicit = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma_cifre_cnp = 0
    for x in cnp_explicit:
        suma_cifre_cnp += (int(cnp_explicit[x]) * int(cnp_fara_n[x]))
    numar_verificat = suma_cifre_cnp % 11
    if numar_verificat == 10:
        cifra_control = 1
    else:
        cifra_control = numar_verificat
    cnp_explicit.append(cifra_control)
    print(f'CNP-ul prelucrat: {cnp_explicit} iar cifra de control este: {cifra_control}')


variabila_cnp = validare(input("Introdu CNP-ul: "))
validator = validator_cnp(variabila_cnp)
print(validator)
cifra_de_control()