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


def validator_cnp(cnp):
    """
    :param cnp: cnp -ul introdus de util de la tastatura
    :return: mesaj "Valid" in cazul in care CNP -ul este valid, "Invalid" in cazul in care nu e valid CNP -ul
    """
    if cnp and validare_sex(cnp) and validare_data_nastere(cnp):
        return "Valid"
    return "Invalid"


variabila_cnp = validare(input("Introdu CNP-ul: "))
validator = validator_cnp(variabila_cnp)
print(validator)
