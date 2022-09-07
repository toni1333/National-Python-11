# Max este o pisica mare care doarme toata ziua.
# object name = Max (substantiv)
# class name = Pisica (substantiv)
# property = marime pisica (mare) /atributul (adjectiv)
# activity = doarme /verbul (verb)

# O masina Dacia merge repede.
# object name = Dacia
# class name = masina
# property = repede
# activity = merge

# Catelul Max are 4 picioare si latra tare!
# object= Max
# class = Catelul
# property = 4 picioare , tare (latra)
# activity = latra


# class Dog:
#     pass
#
# obiect_1 = Dog()
# print(obiect_1)

# stackList = []
#
# def push(val):
#     stackList.append(val)
#
# push(3)
# push(2)
# push(1)
# print(stackList)
#
# def pop():
#     valoare = stackList[-1]
#     del stackList[-1]
#     return valoare
#
# print(pop())
# print(pop())
# print(pop())

class Stack:
    def __init__(self, *val1):       # dupa self variabila de instanta

        # print("HI")
        # self.__stackList = []  / am facut private / encapsulation
        self.__stackList = []
        self.valoare1 = val1

    def push(self):
        self.__stackList = [val for val in self.valoare1]
        # print(self.valoare1)
        # self.__stackList.append(self.valoare1)
        print(self.__stackList)

    def pop(self):
        valoare = self.__stackList[-1]
        del self.__stackList[-1]
        return  valoare



obiect_stiva = Stack(3, 4, 5)
# obiect_stiva_1 = Stack(2)
# obiect_stiva_2 = Stack(1)
# print(obiect_stiva.__stackList)
obiect_stiva.push()
# obiect_stiva.push()
# obiect_stiva.push()

# obiect_stiva_1.push()
# obiect_stiva_2.push()

# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
