import csv
import datetime
#
#
# def introducere_categorii():
#
#     while True:
#         with open('categorii.txt', 'a', newline = '') as file:
#             file.write(f'{input("Adauga categoria: ")} \n')
#             decizie = input("Doriti sa introduceti o alta categorie? (Y/N)").lower()
#             if decizie == 'n':
#                 break
#     return True
#
# introducere_categorii()
#
# def validare_data(data_limita):
#     try:
#         datetime.datetime.strptime(data_limita, '%d-%m-%Y %H:%M')
#         return True
#     except Exception:
#         return False
#
# def introducerea_taskurilor():
#     while True:
#         with open('taskuri.csv', 'a', newline = '') as file:
#             csv_writer = csv.writer(file, delimiter=',')
#             task = input('Adauga un task: ')
#             data_limita = input('Adauga o data limita: ')
#             validarea_datei = validare_data(data_limita)
#             while validarea_datei is False:
#                 print("Data nu are formatul corect")
#                 data_limita= input('Adaugati o noua data: ')
#                 validarea_datei = validare_data(data_limita)
#                 if validarea_datei is True:
#                     break
#             responsabil = input('Adauga persoana responsabila: ')
#             categoria = input("Adauga categoria: ")
#             with open('categorii.txt', 'r') as file:
#                line = file.readlines()
#             verificare = categoria.strip()
#             new_list = [x.strip() for x in line]
#             while verificare not in new_list:
#                 intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
#                 if intr_categ:
#                     categoria = intr_categ
#                 if intr_categ.strip() in new_list:
#                     break
#             csv_writer.writerow([task, data_limita, responsabil, categoria])
#         decizie = input("Doriti sa introduceti un alt task? (Y/N)").lower()
#         print(decizie)
#         if decizie == 'n':
#             break
#
#     return True
# introducerea_taskurilor()

def afisare_meniu():
        with open('categorii.txt', 'r') as file:
            line_curata = file.read()
            print(line_curata)
            alegere = input('Alege-ti o categorie:')
            if alegere in line_curata:
                with open('taskuri.csv', 'r') as csv_file:
                    rows = csv.reader(csv_file, delimiter=',')
                    lista_rows = []
                    for row in rows:
                        lista_rows.append(row)
                        print(row)
            else:
                print("Categoria nu exista! ")
        variabila_input=input("Alegeti o optiune din cele 8 mai jos: \n"
                              "1.Sortare Ascendenta Task\n"
                              "2.Sortare Descendenta Task\n"
                              "3.Sortare ascendenta data \n"
                              "4.Sortare descendenta data\n"
                              "5.Sortare ascendenta persoana \n"
                              "6.Sortare descendenta persoana \n"
                              "7.Sortare ascendenta categorie\n"
                              "8.Sortare descendenta categorie\n")
        if int(variabila_input) == 1:
            print(sorted(lista_rows, key=lambda x: x[0]))
        elif int(variabila_input) == 2:
            print(sorted(lista_rows, key=lambda x: x[0],reverse = True))
        elif int(variabila_input) == 3:
            print(sorted(lista_rows, key=lambda x: x[1]))
        elif int(variabila_input) == 4:
            print(sorted(lista_rows, key=lambda x: x[1],reverse = True))
        elif int(variabila_input) == 5:
            print(sorted(lista_rows, key=lambda x: x[2]))
        elif int(variabila_input) == 6:
            print(sorted(lista_rows, key=lambda x: x[2],reverse = True))
        elif int(variabila_input) == 7:
            print(sorted(lista_rows, key=lambda x: x[3]))
        elif int(variabila_input) == 8:
            print(sorted(lista_rows, key=lambda x: x[3],reverse = True))











afisare_meniu()
