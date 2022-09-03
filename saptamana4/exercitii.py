# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls =3
#     num_calls+=1
#     return x*x
#
# print(exercitiu(4))


# def e(var):
#     for letter in 'geeksforgeeks':
#         if letter == 'e' or letter =='s':
#             continue
#         print('Current letter:' ,letter)
#         var = 10
#         return var
#
#
# print(e(20))
#
# def f(a,list=[]):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# f(2,[1,2,3])
# f(2)
# f(3)

# Anagram
lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
print("-------------------------------------------------------")
print(f"Please check if names from below are anagram \n{lista_nume} ")

NO_OF_CHARS = 256
def areAnagram(str1, str2):
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    for i in str1:
        count1[ord(i)] += 1
    for i in str2:
        count2[ord(i)] += 1
    if len(str1) != len(str2):
        return 0
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0
    return 1
str1 = input(f"Please select 1st name from list: ")
str2 = input(f"Please select 2nd name from list: ")

if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")

# # Eliminate duplicates
# print("-------------------------------------------------------")
# print (f"Eliminate duplicates from {lista_nume}")
# result = []
# for i in lista_nume:
#     if i not in result:
#         result.append(i)
# print ("The list after removing duplicates : " + str(result))
# lista_nume = result