
# def numarare_vocale(param):
#     count=0
#     vocale=['a','e','i','o','u','A','E','I','O','U']
#
#     for lit in param:
#         if lit in vocale:
#             count += 1
#     print("Numarul de vocale: ", count)
#     print("Multumim!\n")
# introducere=""
# ruleaza=True
# while ruleaza:
#         introducere = str(input("Introduce-ti un cuvant ca sa determinam cate vocale are,"
#                     "dar nu mai mare de 10 caractere:\n"))
#         if len(introducere) > 10:
#             print("Ati introdus un cuvant mai mare de 10 caractere, mai odata..")
#             continue
#         else:
#             numarare_vocale(introducere)
#             break


def impartirea_trei_numere(a,b,c):
    impartire = a / b / c
    if a == b == c:
        impartire *= 3
    return impartire

print(impartirea_trei_numere(13,13,13))

# n = [1,2,3,4,5,6,7]
# duble_insert = []
# for x in n:
#     duble_insert.append(x)
#     if x % 2 == 0:
#         x *= 2
#         duble_insert.append(x)
#
# print("Lista originala:  ", n)
# print("Lista prelucrata: ",duble_insert)
#         
