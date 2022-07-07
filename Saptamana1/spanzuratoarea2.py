print("--INITIALIZARE JOC--\n\n")
cuvant = str()
cuvant = input("Introduce-ti cuvantul secret: ").upper()
print(f"Cuvantul secret are {len(cuvant)} caractere!\n")

lit_x = []

nr_caract_ascunse = int(input("Introduce-ti cate caractere sa NU se afiseze: "))
while nr_caract_ascunse > 0:
    nr_litere_ascunse = int(input("Introduce-ti POZITIILE numerelor care sa se ascunda: "))
    lit_x.append(nr_litere_ascunse)
    nr_caract_ascunse -= 1

cuvant_partial = []
cuvant_partial = list(cuvant).copy()

for i, v in enumerate(lit_x):
    cuvant_partial.insert(v, "_")
    cuvant_partial.pop(v - 1)

print("\n\n--SA INCEAPA JOCUL!!!--\n\n")
print("Cuvantul pe care trebuie sa-l ghiciti este: \n", cuvant_partial, "\n")
incercari = 10
while incercari > 0:
    cuv_de_ghicit = input("Incerca-ti sa ghiciti cuvantul: \n").upper()
    if cuv_de_ghicit == cuvant:
        print("BRAVO ATI GHICIT!!!")
        break
    else:
        print(f"mai incerca-ti odata... mai aveti {incercari - 1} incercari.. \n")
        incercari -= 1
