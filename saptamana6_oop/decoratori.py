# class Dog:
#
#     legs_no = 4 # variabila de clasa sau atribut de clasa
#
#     def __init__(self,name):
#         self.__name = name
#
#
#     # def __str__(self):
#     #     return str(self.name)
#     @property
#     def nume(self):
#         return self.__name
#
#     @nume.setter
#     def nume(self, prenume):
#         self.__name = prenume
#
#     @nume.deleter
#     def nume(self):
#         del self.__name
#
#
#     # def change_name(self,name):
#     #     self.name = name
#     #     return self.name
#     #
#     # @staticmethod
#     # def speak():                         # metoda statica
#     #     return 'Ham ham!'
#     #
#     def __str__(self):
#         return str(self.nume)
#
#
# caine = Dog('Rex')
# rasa = Dog('Max')
# # print(caine.speak())
# print(caine.__dict__, 'inainte')
# # print(rasa)
# caine.nume = 'John'
#
# print(caine.nume)
# print(caine.__dict__, 'dupa')
# del caine.nume
# print(caine.nume)
# print(rasa.nume)
# print(caine.change_name('<<rename Rex1>>'))

# caine.legs_no = 3
# Dog.legs_no = 3
# print('caine',caine.legs_no,'Dog class',Dog.legs_no)
# print('rasa',rasa.legs_no,'Dog class', Dog.legs_no)

# print(caine._Dog__nume)

# print(Dog.speak())
# print(Dog.change_name('Rex2'))   nu functioneaza nu are self change name...


# def decorator_simplu(parametru):
#     print(f'Apelam functia {parametru.__name__}')
#     return parametru
#
# @decorator_simplu
# def functie_simpla():
#        return 'Buna seara'
#
# @decorator_simplu
# def functie_complexa():
#     return "Noapte buna"
#
# print(functie_simpla())
# print(functie_complexa())

# def decorator_depozit(functia_noastra):
#     def ambalaj_no(carti):
#         return f'Ambalam produse din {functia_noastra.__name__} care contine cartea {carti}'
#     return ambalaj_no
#
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume


# print(impachetare_carti('Amintiri din copilarie','Baltagul'))

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def ambalaj_intern(*carte):
#             return f"Ambalam produse din {functia_noastra.__name__} cu {material} care contine cartea "\
#                     f" cartea {', '.join(x for x in carte)}"
#
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit('hartie')
# def impachetare_carti(*nume):
#     return nume
#
#
# print(impachetare_carti('Amintiri din copilarie','Baltagul'))


# def decorator(simbol):
#     def adauga_simbol(functie):
#         def functia_upper(parametru):
#             return  parametru.upper() if parametru.upper()[-1] == '.' else parametru.upper() + simbol
#         return functia_upper
#     return adauga_simbol
#
# @decorator(".")
# def functie(propozitie):
#     return propozitie
#
#
# print(functie('Ana are mere'))
# import time
#
#
# def calculeaza_timpul(functia):
#     def functie_interioara(*param):
#         inceput = time.time()
#         functia(*param)
#         sfarsit = time.time()
#         print(f"Timp total de executie: {sfarsit - inceput}")
#         return functia(*param)
#     return functie_interioara
#
# @calculeaza_timpul
# def adunare(*args):
#     suma = 0
#     for i in args:
#         suma += i
#     return suma
#
# print(adunare(1,2,3))
import time

def calculeaza_timpul(functia):
    def functie_interioara(param):
        inceput = time.time()
        functia(param)
        sfarsit = time.time()
        print(f"Timp total de executie: {sfarsit - inceput}")
        return functia(param)
    return functie_interioara

@calculeaza_timpul
def adunare(number):
    suma = 0
    for i in range(number):
        suma += i
    return suma

print(adunare(100098600))