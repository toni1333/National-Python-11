#PROBLEMA 1:

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

patches = [[5,14,'Conquistador'],[26,31,'King'],[43,49,'Palace']]

def funct_lista(*args):
    lista_string = list(string)
    for x in sorted(args[0], reverse=True):
        lista_string[x[0] - 1:x[1]] = x[2]

    return "".join(lista_string)


print("Stringul Original: ", string)
print("Stringul Prelucrat: ",funct_lista(patches))


#     string_lista=list(string)
#     string_lista[1]=patches[0][2]
#     string_lista[4]=patches[1][2]
#     string_lista[8]=patches[2][2]
#     string_lista=' '.join(string_lista)
#
# print("Stringul dat:      ",string)
# print("Stringul prelucrat:", string_lista)
#
# lista_nume= ['Maria', 'Irina', 'Claudiu', 'Ionut','Matei','Irina','Maria','Claudiu']
# lista_sortata=lista_nume
# lista_sortata.sort()
# print("1.Lista nume sortate: ",lista_sortata)


# count=lista_nume[0]
# # count = lista_nume.count(search)
#
# print(count)
#________________________________________________

#Varianta2 1 exercitiu:

#string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
#
# string_mod =string.replace('Inquisitor', "Conquistador")
# string_mod1 =string_mod.replace('Varric', "King")
# string_mod2 =string_mod1.replace("Skyhold's", "Palace")
# print(string)
# print(string_mod2)


#PROBLEMA 2:
lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
lista_sortata=lista_nume
lista_sortata.sort()
print("1.Lista nume sortate: ",lista_sortata)

# print(sorted(lista_nume, key=lambda x: x[2]))   // VARIANTA A 2 A SORTARE
numarat = dict()
for line in lista_nume:
    cuvinte =line.split()
    for cuvant in cuvinte:
        numarat[cuvant] = numarat.get(cuvant, 0) + 1
print('2.Numarul de aparitii: ', numarat)

list_clear= []


fin_max = max(numarat, key=numarat.get)
for item, element in numarat.items():
    if numarat[fin_max] == element:
        list_clear.append(item)
print("3.Nume care apare de cele mai multe ori: ",list_clear)

list_clear1= []

fin_min = min(numarat, key=numarat.get)
for item, element in numarat.items():
    if numarat[fin_min] == element:
        list_clear1.append(item)
print("4.Nume care apare de cele mai putine ori: ",list_clear1)