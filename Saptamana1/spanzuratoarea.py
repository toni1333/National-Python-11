cuvant = 'o n o m a t o p e e'
cuvant = 'o _ o _ _ _ o _ e e'
#7 incercari
cuvant = list('onomatopee')
for i in range(len(cuvant)):
    print(cuvant[0], cuvant[-1])
    if i != cuvant[0] or i != cuvant[-1]:
        cuvant[i] = '_'
print(cuvant)