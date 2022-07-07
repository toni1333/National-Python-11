cuvant = 'o n o m a t o p e e'
cuvant = 'o _ o _ _ _ o _ e e'
#7 incercari
cuvant_initial = 'onomatopee'.lower()
cuvant = list('onomatopee')
for i in range(len(cuvant)):
    if cuvant[i] != cuvant[0] and cuvant [i] != cuvant[-1]:
        cuvant[i] = '_'
print(cuvant)

nr_incercari = 1
litere_incercate = set()
while nr_incercari <= 7:
    litera = input('Alege o litera: ').lower()
    if litera in cuvant_initial and( litera != cuvant_initial[0] and litera != cuvant_initial[-1]):
    # print("Ai incercat prima sau ultima litera")
    # if litera in cuvant_initial:
        for index , valoare in enumerate(cuvant_initial):
            if litera == valoare:
                cuvant[index] = litera
    else:
        if litera == cuvant_initial[0] or litera == cuvant_initial[-1]:
            print("Ai incercat prima sau ultima litera")
        else:
            if litera not in litere_incercaten:
                nr_incercari += 1
                print("litera a fost deja incercata ", ",".join(litere_incercate))
            litere_incercate.add(litera)
            if len(list(litere_incercate)) >= 7:
                print(f"Ai pierdut! cuvantul initial era: {cuvant_initial} ")
                break
    if '_' not in cuvant:
        print("Ai castigat!")
        break
    print(cuvant, f"Mai ai {7 - len(list(litere_incercate))} incercari")
print(cuvant)




