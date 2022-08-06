import csv
import datetime


def introducere_categorii():

    while True:
        with open('categorii.txt', 'a', newline = '') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
            decizie = input("Doriti sa introduceti o alta categorie? (Y/N)").lower()
            if decizie == 'n':
                break
    return True


def validare_data(data_limita):
    try:
        datetime.datetime.strptime(data_limita, '%d-%m-%Y %H:%M')
        return True
    except Exception:
        return False

def introducerea_taskurilor():
    while True:
        with open('taskuri.csv', 'a', newline = '\n') as file:
            csv_writer = csv.writer(file, delimiter=',')
            task = input('Adauga un task: ')
            data_limita = input('Adauga o data limita: ')
            validarea_datei = validare_data(data_limita)
            while validarea_datei is False:
                print("Data nu are formatul corect... [zi-luna-an ora:minute]")
                data_limita= input('Adaugati o noua data: ')
                validarea_datei = validare_data(data_limita)
                if validarea_datei is True:
                    break
            responsabil = input('Adauga persoana responsabila: ')
            categoria = input("Adauga categoria: ")
            with open('categorii.txt', 'r') as file:
               line = file.readlines()
            verificare = categoria.strip()
            new_list = [x.strip() for x in line]
            while verificare not in new_list:
                intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
                if intr_categ:
                    categoria = intr_categ
                if intr_categ.strip() in new_list:
                    break
            csv_writer.writerow([task, data_limita, responsabil, categoria])
        decizie = input("Doriti sa introduceti un alt task? (Y/N)").lower()
        print(decizie)
        if decizie == 'n':
            break

    return True


# def afisare_meniu():                            VARIANTA A 2 A
#         with open('categorii.txt', 'r') as file:
#             citire_linie = file.read()
#             print(citire_linie)
#             alegere = input('Alege-ti o categorie:')
#             while alegere not in citire_linie:
#                alegere = input("Reintrodu categoria: ")
#             if alegere in citire_linie:
#                 with open('taskuri.csv', 'r') as csv_file:
#                     rows = csv.reader(csv_file, delimiter=',')
#                     lista_rows = []
#                     for row in rows:
#                         lista_rows.append(row)
#                         print(row)
#
#         variabila_input=input("Alegeti o optiune din cele 8 mai jos: \n"
#                               "1.Sortare ascendenta Task\n"
#                               "2.Sortare descendenta Task\n"
#                               "3.Sortare ascendenta data \n"
#                               "4.Sortare descendenta data\n"
#                               "5.Sortare ascendenta persoana \n"
#                               "6.Sortare descendenta persoana \n"
#                               "7.Sortare ascendenta categorie\n"
#                               "8.Sortare descendenta categorie\n")
#         while (int(variabila_input) >len(lista_rows) or int(variabila_input) <1):
#             unu=1
#             variabila_input=input(f"Reintrodu optiunea: (un numar intre {unu} si {len(lista_rows)})")
#         if int(variabila_input) == 1:
#             print(sorted(lista_rows, key=lambda x: x[0]))
#         elif int(variabila_input) == 2:
#             print(sorted(lista_rows, key=lambda x: x[0],reverse = True))
#         elif int(variabila_input) == 3:
#             print(sorted(lista_rows, key=lambda x: x[1]))
#         elif int(variabila_input) == 4:
#             print(sorted(lista_rows, key=lambda x: x[1],reverse = True))
#         elif int(variabila_input) == 5:
#             print(sorted(lista_rows, key=lambda x: x[2]))
#         elif int(variabila_input) == 6:
#             print(sorted(lista_rows, key=lambda x: x[2],reverse = True))
#         elif int(variabila_input) == 7:
#             print(sorted(lista_rows, key=lambda x: x[3]))
#         elif int(variabila_input) == 8:
#             print(sorted(lista_rows, key=lambda x: x[3],reverse = True))
#
#         filtrare_camp=input('Introduce-ti campul dupa care se realizeaza filtrarea:\n'
#                        '1. Task\n'
#                        '2. Data\n'
#                        '3. Persoana responsabila\n'
#                        '4. Categorie\n')
#         while(filtrare_camp.isdigit()==False):
#             filtrare_camp = input('Reintroduce-ti un numar: (intre 1 si 4)\n')
#         while (int(filtrare_camp) > 4 or int(filtrare_camp) < 1):
#             filtrare_camp=input('Reintroduce-ti campul: (intre 1 si 4)\n')
#         with open('taskuri.csv', 'r') as csv_file:
#                             rows = csv.reader(csv_file, delimiter=',')
#                             lista_rows = []
#                             for row in rows:
#                                 lista_rows.append(row)
#         if int(filtrare_camp) == 1:
#             for x in lista_rows:
#                 print(x[0])
#         if int(filtrare_camp) == 2:
#             for x in lista_rows:
#                 print(x[1])
#         if int(filtrare_camp) == 3:
#             for x in lista_rows:
#                 print(x[2])
#         if int(filtrare_camp) == 4:
#             for x in lista_rows:
#                 print(x[3])
#
#         filtrare_string=input('Introduce-ti cautare cuvant: \n')
#         matches=[]
#         for match in lista_rows:
#             if filtrare_string in match:
#                 print("Am gasit:", matches)


def afisare_meniu():
    with open('taskuri.csv', 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        lista_rows = []
        for row in rows:
            lista_rows.append(row)
        print(sorted(lista_rows, key=lambda x: x[3]))
        variabila_input = input("Alegeti din optiunile de mai jos pentru sortare: \n"
                            "1. Ascendenta Task\n"
                            "2. Descendenta Task\n"
                            "3. Ascendenta Data \n"
                            "4. Descendenta Data\n"
                            "5. Ascendenta Persoana \n"
                            "6. Descendenta Persoana \n"
                            "7. Ascendenta Categorie\n"
                            "8. Descendenta Categorie\n"
                            "9. selectati 'N' daca nu doriti sortarea\n").lower()
        if variabila_input == 'n':
            print('nu doriti sortarea')
        elif int(variabila_input) == 1:
            print(sorted(lista_rows, key=lambda x: x[0]))
        elif int(variabila_input) == 2:
            print(sorted(lista_rows, key=lambda x: x[0], reverse=True))
        elif int(variabila_input) == 3:
            print(sorted(lista_rows, key=lambda x: x[1]))
        elif int(variabila_input) == 4:
            print(sorted(lista_rows, key=lambda x: x[1], reverse=True))
        elif int(variabila_input) == 5:
            print(sorted(lista_rows, key=lambda x: x[2]))
        elif int(variabila_input) == 6:
            print(sorted(lista_rows, key=lambda x: x[2], reverse=True))
        elif int(variabila_input) == 7:
            print(sorted(lista_rows, key=lambda x: x[3]))
        elif int(variabila_input) == 8:
            print(sorted(lista_rows, key=lambda x: x[3], reverse=True))
        elif int(variabila_input) > 8:
            print('Optiunea nu exista... ')


def filtrare_date():
    with open('taskuri.csv', 'r') as csv_file:
        rows = csv.reader(csv_file)
        lista_rows = []
        lista_rows1 = []
        lista_rows2 = []
        lista_rows3 = []
        for row in rows:
            lista_rows.append(row[0])
            lista_rows1.append(row[1])
            lista_rows2.append(row[2])
            lista_rows3.append(row[3])
        variabila_input = input("Alegeti din optiunile de mai jos pentru filtrare: \n"
                            "1. Task\n"
                            "2. Data \n"
                            "3. Persoana\n"
                            "4. Categorie\n"
                            "5. Selectati 'N' daca nu doriti sortarea\n").lower()
        if variabila_input == 'n':
            print('NU doriti filtrarea...')
        elif int(variabila_input) == 1:
            print(lista_rows)
        elif int(variabila_input) == 2:
            print(lista_rows1)
        elif int(variabila_input) == 3:
            print(lista_rows2)
        elif int(variabila_input) == 4:
            print(lista_rows3)


# def adaugare_task_nou():
#             task = input('Adauga un task: ')
#             data_limita = input('Adauga o data limita: ')
#             validarea_datei = validare_data(data_limita)
#             while validarea_datei is False:
#                 print("Data nu are formatul corect... [zi-luna-an ora:minute]")
#                 data_limita= input('Adaugati o noua data: ')
#                 validarea_datei = validare_data(data_limita)
#                 if validarea_datei is True:break
#             responsabil = input('Adauga persoana responsabila: ')
#             with open('categorii.txt', 'a', newline='') as file:
#                 categoria=file.write(f'{input("Adauga categoria: ")} \n')
#             with open('taskuri.csv', 'a', newline='\n') as file:
#                 csv_writer = csv.writer(file, delimiter=',')
#                 csv_writer.writerow([task, data_limita, responsabil, categoria])

def editare_task():
    print('-------Meniu Editare Task------')
    with open('taskuri.csv', 'r') as file:
        lines = file.read()
        print('TO-DO LIST:\n', lines)

    file = open('taskuri.csv', 'r')
    reader = csv.reader(file)
    l = []
    uroll = input('Selectati Task-ul dupa categorie:')
    Found = False
    for row in reader:
        if row[3] == uroll:
            Found = True
            stream = input('Schimba-ti taskul')
            row[0] = stream
            stream1 = input('Schimba-ti data')
            validarea_datei = validare_data(stream1)
            while validarea_datei is False:
                print("Data nu are formatul corect")
                stream1 = input('Adaugati o noua data: ')
                validarea_datei = validare_data(stream1)
                if validarea_datei is True:
                    break
            row[1] = stream1
            stream2 = input('Schimbati numele')
            row[2] = stream2
            stream3 = input('Schimbati categoria')
            row[3] = stream3
        l.append(row)
    file.close()

    if Found == False:
        print("Categorie inexistenta")
    else:
        file = open('taskuri.csv', 'w+', newline='')
        writer = csv.writer(file)
        writer.writerows(l)
        file.seek(0)
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()


def stergere_task():
    print('-------Meniu Stergere Task------')
    with open('taskuri.csv', 'r+') as file:
        lines = file.readlines()

        for count, elemente in enumerate(lines,1):
            print(count,elemente,end='')
        print('\n')
    while True:
        try:
            sterge_task=input('Alege-ti task-ul pe care doriti sa-l stergeti dupa numar:\n')
            if int(sterge_task) >len(lines):
                print("Numar prea mare mai incercati odata..")
                continue
            elif int(sterge_task)<=0:
                print("Numar prea mic...")
                continue
            else:
                print("Ati STERS taskul: ",lines[int(sterge_task)-1])
                del(lines[int(sterge_task)-1])
                with open("taskuri.csv",'w') as memorare:
                    for x in lines:
                        memorare.write(x)
                break
        except ValueError: print('Introduce-ti un numar...')



def afisare_meniu_principal():
    print('-'* 30)
    print('-----MENIU PRINCIPAL-----\n'
          '1.Introducere Categorie\n'
          '2.Introducere Task\n'
          '3.Afisare date sortate\n'
          '4.Afisare date filtrate\n'
          '5.Editare task\n'
          '6.Stergere task\n'
          '7.Iesire din program\n')
    print('-'*30)

# ---------------- de aici ruleaza programul ---------------


with open('taskuri.csv','r') as file:
    lines = file.read()

    print('\n')
    print('BINE ATI VENIT LA TO-DO LIST\n')
    if len(lines)==0:
        print('TO-DO LIST este gol')
    else:
        print('TO-DO LIST:\n',lines)

afisare_meniu_principal()

ruleaza=True
while ruleaza:
    try:
        tastatura=int(input('-----MENIU PRINCIPAL-------\n'
                            'Alege-ti optiunea:\n'))
        if tastatura > 7: print('Ati introdus un numar prea mare..')
        if tastatura == 0: print('Nu poate fi 0..')
        if tastatura == 1: introducere_categorii()
        if tastatura == 2: introducerea_taskurilor()
        if tastatura == 3: afisare_meniu()
        if tastatura == 4: filtrare_date()
        if tastatura == 5: editare_task()
        if tastatura == 6: stergere_task()
        if tastatura == 7: ruleaza=False
    except ValueError: print('Caracter invalid...')


