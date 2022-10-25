people = []
person = []


def ali():
    r = True
    r2 = True
    while r:
        person = []
        try:
            x = input('introduce-ti nume:\n')
            person.append(x)
            while r2:
                y = input('introduce-ti numar:\n')
                if y.isdigit() == False:
                    print("Introduce-ți un numar, mai încercați odata...")
                    continue
                else:
                    person.append(str(y))
                    print(person)
                    people.append(person)
                    r = False
                    r2 = False
        except ValueError:
            print('ati gresit caracterul, mai incercati odata: \n')


def memorare_ag():
    with open("phone_agenda.txt", "w") as fp2:
        fp2.write(str(people))


def sli():
    c = 1
    print("Numar de contacte: " + str(len(people)))
    for x in people:
        print(str(c) + ")" + x[0] + "-->" + x[1])
        c += 1
        print("=======")
    while True:
        sterge = int(input("Alege-ti numarul de sters:\n"))
        if sterge > len(people):
            print("nr prea mare,incearca mai odata...")
            continue
        elif sterge <= 0:
            print("nr prea mic...")
            continue
        else:
            del (people[sterge - 1])
            break


def af():
    print('===' * 4)
    print("""1.Adaugă\n2.Șterge\n3.Afișează\n4.Ieșire """)
    print('===' * 4)


def AF():
    if len(people) == 0:
        print("Agenda este goala!!!")
    else:
        for x in people:
            print("---------")
            print("Nume: " + x[0] + "\n")
            print("numar: " + x[1] + "\n")
            print("---------")


"""----------------aici ruleaza-------------"""
while True:
    with open('phone_agenda.txt', 'r+') as f:
        lines = f.read()
        if len(lines) == 0:
            break
        else:
            people = eval(lines)
            print("■" * 5, "AGENDA", "■" * 5)
            c = 1
            for x in people:
                print(str(c) + ")" + "Nume: ", x[0], "\n", "numar: ", x[1], "\n")
                c += 1
                print("■" * 15)
        break

af()

r1 = True
while r1:
    try:
        z = int(input("Alege-ti optiunea:\n"))
        if z > 5: print("prea mare..")
        if z == 0: print("nu poate fi 0...")
        if z == 1: ali()
        if z == 2: sli()
        if z == 3: AF()
        if z == 4:
            r1 = False
    except ValueError:
        print("caracter necunoscut... ")

memorare_ag()
