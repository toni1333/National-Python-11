# class Catalogue:
#     def __init__(self, nume ,prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.materii = {}
#         self.absente = 0
#
#     def __str__(self):
#         return f"Numarul de absente este {self.absente}"
#
#     def absente_increment(self):
#         self.absente = self.absente + 1
#         return self.absente
#
#     def motivari_validare(self, motivari):
#         if type(motivari) != int or type(motivari) == float:
#             return True
#         return False
#
#     def absente_motivare(self, motivari):
#         if self.motivari_validare(motivari):
#
#             if motivari<= self.absente:
#                 self.absente = self.absente - motivari
#                 return self.absente
#
#         return f"motivari {motivari} nu este o variabila"
#
# class Extensie1(Catalogue):
#
#     def __init__(self, nume, prenume):
#         super().__init__(nume, prenume)
#
#         self.materia = None
#         self.nota = None
#         self.dictionar = {}
#
#
#     def adauga_materie(self, materia, nota):
#         self.dictionar[materia] = nota
#         return self.dictionar
#
#     def afisare_materii(self):
#         return f" Materiile pentru {self.nume} {self.prenume} sunt  {','.join(self.dictionar.keys())}"
#
#
# elev1 = Extensie1('Ion', 'Roata')
# print(elev1.nume, elev1.prenume)
# # elev1 = Extensie1('Ion', 'Roata')
# elev1.absente_increment()
# elev1.absente_increment()
# elev1.absente_increment()
#
# elev1.absente_motivare(2)
#
# print(elev1)
#
# elev2 = Extensie1('George', 'Cerc')
# print(elev2.nume, elev2.prenume)
# elev2.absente_increment()
# elev2.absente_increment()
# elev2.absente_increment()
# elev2.absente_increment()
#
# elev2.absente_motivare(2)
# print(elev2)
#
# elev1.adauga_materie('python',[4,9,2])
# print(elev1.afisare_materii())
# elev2.adauga_materie('python',[3,6,8])
# print(elev2.afisare_materii())
#
# elev1.adauga_materie('romana',[4,9,2])
# print(elev1.afisare_materii())
# elev2.adauga_materie('matematica',[3,6,8])
# print(elev2.afisare_materii())

#------------

# class Catalog:
#
#     def __init__(self, nume, prenume):
#         # this is ALSO called initialization method
#         self.nume = nume
#         self.prenume = prenume
#         # these are values which we have to provide values for when we create instances
#         self.materii = {}
#         self.absente = 0
#     #     once these 2 are defined
#
#     def __str__(self):
#         return f"Numarul de absente este {self.absente}"
#     # every time we write __str__ in another child class, it OVERRIDES the one in parent class
#
#
#     def absenste_increment(self):
#         self.absente = self.absente + 1
#         return self.absente
#
#
#     def motivari_validare(self, motivari):
#         if type(motivari) == int or type(motivari) == float:
#             return True
#         return False
#
#     def absente_motivare(self, motivari):
#         if self.motivari_validare(motivari):
#
#         #     we write the method with self in front as ti is defined within the class,
#         # just like 'absente_motivare(self, motivari)'
#
#             if  motivari <= self.absente:
#                 self.absente = self.absente - motivari
#                 return self.absente
#
#
#         return f"motivari {motivari} nu este o variabila valida"
#
#
# class Extensie_1(Catalog):
#
#     def __init__(self, nume, prenume):
#         # this is ALSO called initialization method
#         super().__init__(nume, prenume)
#
#         self.materia = None
#         self.nota = None
#         self.dictionar = {}
#     #     extra variables that exist BESIDES the ones inherited from Catalogue
#
#     #     once these 2 are defined
#
#     def adauga_materie(self, materia, nota):
#
#         self.dictionar[materia] = nota
#         return self.dictionar
#         #     whenever we use methods/variables from constructor, we have to mentions
#     # SELF in front, ALWAYS
#
#     def afisare_materii(self):
#         return f" Materiile pentru {self.nume} {self.prenume} sunt {','.join(self.dictionar.keys())}"
#
#     def medie_aritmetica(self):
#         medie = {}
#         lista_temporara = []
#         print(self.dictionar)
#         for i,v in self.dictionar.items():
#             lista_temporara = v.copy()
#             for item in lista_temporara:
#                 if str(item).isdigit() is False:
#                     lista_temporara.remove(item)
#             medie[f"media.{i}"] = sum(lista_temporara) / len(lista_temporara)
#         return medie
#
#
# elev1 = Extensie_1('Ion', 'Roata')
# print(elev1.nume, elev1.prenume)
#
#
# elev1.absenste_increment()
# elev1.absenste_increment()
# elev1.absenste_increment()
#
# elev1.absente_motivare(2)
#
# print(elev1)
#
#
# elev2 = Extensie_1('George', 'Cerc')
# print(elev2.nume, elev2.prenume)
# print(elev2.__dict__)
#
# elev2.absenste_increment()
# elev2.absenste_increment()
# elev2.absenste_increment()
# elev2.absenste_increment()
#
# elev2.absente_motivare(2)
# print(elev2)
#
# elev1.adauga_materie('python', [4, 9, 2])
# print(elev1.afisare_materii())
#
# elev2.adauga_materie('python', [3, 6, 8, "string"])
# print(elev2.afisare_materii())
# # whatever we want to print as is NOT part of the __print__ method, which is defautl for
# # print, HAS to eb specified as a method within the print brackets
#
# elev1.adauga_materie('romana', [4, 9, 2])
# print(elev1.afisare_materii())
#
# elev2.adauga_materie('matematica', [3, 6, 8])
# print(elev2.afisare_materii())
# print(elev2.medie_aritmetica())
# print(elev2.__dict__)
#
# # we either specify the values we want to see when printing the object IN the print, OR make another display method within the catalog class
# # for EACH value we want to see, we have to mention object name for it

#-----------------------------------------

# class Prajituri:
#     variabila = []
#     def __init__(self, nume , pret, gramaj):
#         self.nume = nume
#         self.pret = pret
#         self.gramaj = gramaj
#
#         lista = [self.nume, self.pret, self.gramaj]
#         Prajituri.variabila.append(lista)
#
#     def afisare_gramaj(self):
#         return sorted(self.variabila, key=lambda x: x[2])
#
#     def afisare_pret(self):
#         return sorted(self.variabila, key=lambda x: x[1])
#
#     def __str__(self):
#         return f'Prajitura este {self.nume}, costa {self.pret} si are un gramaj de {self.gramaj}'
#
# class Tort(Prajituri):
#     def __init__(self, etajat = False, glazura = 'ciocolata'):
#         super().__init__(self.nume, self.pret, self.gramaj)
#         self.etajat = etajat
#         self.glazura = glazura
#
#
#     def __str__(self):
#         return f'Tortul este {self.nume}, costa {self.pret} si are un gramaj de {self.gramaj}, are glazura de {self.glazura} si este etajat {self.etajat}'
#
#
#
#
#
# obj_1 = Prajituri('Amandina', 2, 300)
# obj_2 = Prajituri('Briosa', 3 , 300)
# obj_3 = Prajituri('Gogoasa', 4, 400)
#
# print(obj_1)
# print(obj_2)
# print(obj_3)
# print(obj_3.afisare_gramaj())
# print(obj_3.afisare_pret())
#
# obiect_1 = Tort('Elena', 10, 100, glazura='vanilie')
# obiect_2 = Tort('Ana', 20, 200,True, glazura='capsuni')
# obiect_3 = Tort('Ema', 30, 300, True)
#
# print(obiect_1)
# print(obiect_2)
# print(obiect_3)
#
# obiect_1.etajat=True
# print(obiect_1)
# obiect_1.glazura= 'cacao'
# print(obiect_1)

#---------------------------------------------------------

class Prajituri:

    variabila = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj

        lista = [self.nume, self.pret, self.gramaj]
        Prajituri.variabila.append(lista)

    def afisare_gramaj(self):
        return sorted(self.variabila, key= lambda x:[2])
        # print([item2 for item2 in Prajituri.variabila])  # este echivalent cu randul de mai sus

    def afisare_pret(self):
        return sorted(self.variabila, key= lambda x:[1])

    def __str__(self):
        return f"Prajitura este {self.nume}, costa {self.pret} lei si are un gramaj de {self.gramaj} grame"

class Tort(Prajituri):

    def __init__(self, nume, pret, gramaj, etajat=False, glazura="ciocolata"):
        super().__init__(nume, pret, gramaj)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f"Tortul este {self.nume}, costa {self.pret} lei si are un gramaj de {self.gramaj} grame, are glazura de {self.glazura} si este etajat {self.etajat}"

class Fursec(Prajituri):
    pass




obj_1 = Prajituri('Amandina', 2, 200)
obj_2 = Prajituri('Briosa', 3, 300)
obj_3 = Prajituri('Gogoasa', 4, 400)

print(obj_1)
print(obj_2)
print(obj_3)
print(obj_3.afisare_gramaj())
print(obj_3.afisare_pret())

obiect_1 = Tort('Elena', 10, 100, glazura='vanilie')
obiect_2 = Tort('Ana', 20, 200, True, glazura='capsuni')
obiect_3 = Tort('Ema', 30, 300, True)

print(obiect_1)
print(obiect_2)
print(obiect_3)

obiect_1.etajat=True
print(obiect_1)
obiect_1.glazura='cacao'
print(obiect_1)

obj7 = Fursec('Fursec ciocolata',20,100)
obj8 = Fursec('Fursec vanilie',40,500)
obj9 = Fursec('Fursec capsuni',60,300)


print(obj7)
print(obj8)
print(obj9)




#------------_______________________-------------------


