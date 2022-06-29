"""Dezvoltarea unui program care sa calculeze venitul saptamanal al unui angajat"""
"""Venitul saptamanal = venitul/ora * nr ore"""
"""venit_saptamnal = 35 lei * 40 ore"""


# venit saptamanal ----> Float
# venit ora -------> Float
# nr_ore -----> Float

"""  1 obtinem venitul pe ora
     2 obtinem nr ore lucrate
     3 calcul venit saptamanal
     4 afisare rezultate
"""

venit_pe_ora = float(input("Introduce-ti venitul pe ora:"))
nr_ore =float(input("Introduce-ti nr de ore:"))
venit_saptamanal = venit_pe_ora * nr_ore
print("Venitul saptamanal este de " + str(venit_saptamanal) + " lei")
