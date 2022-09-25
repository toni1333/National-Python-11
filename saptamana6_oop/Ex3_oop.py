class Catalog_Auto():
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip
        self.culoare = None

    def adaugare_culoare(self, culoare):
        self.culoare = culoare
        return self.culoare

    def afisare_culoare(self):
        return self.culoare



class Proprietati(Catalog_Auto):
    def __init__(self, marca, tip):
        super().__init__(marca, tip)
        self.scaune_incalzite = True

    def scaune(self, vreau):
        self.scaune_incalzite = vreau
        return self.scaune_incalzite

    def __str__(self):
        return f'Masina este de tip {self.tip}, marca {self.marca}, culoare {self.culoare} si are scaune incalzite {self.scaune_incalzite} '

class Blocuri(Proprietati):
    def __init__(self, marca, tip):
        super().__init__(marca, tip)
        self.blocuri_optice_led = False



    def bloc(self, blocuri_optice_led):
        self.blocuri_optice_led = blocuri_optice_led
        return self.blocuri_optice_led
    def __str__(self):
        return f'Masina este de tip {self.tip}, marca {self.marca} , culoare {self.culoare} si are blocuri optice {self.blocuri_optice_led} '


obj1 = Proprietati('Aro', 'M461')
obj1.scaune(False)
# obj1.scaune_incalzite = True
obj1.adaugare_culoare('rosu')
print(obj1.__dict__)
print(obj1)

obj2 = Blocuri('Dacia', '1310')
obj2.blocuri_optice_led = False
obj2.adaugare_culoare('negru')
print(obj2.__dict__)
print(obj2.blocuri_optice_led, obj2.marca, obj2.tip, obj2.scaune_incalzite)
print(obj1.culoare, obj1.marca, obj1.scaune_incalzite)