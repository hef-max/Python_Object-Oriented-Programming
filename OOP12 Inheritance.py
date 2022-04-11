class Hero:

    def __init__(self, nama, health):
        self.nama = nama
        self.health = health

class Hero_Mage(Hero):
    pass

class Hero_Assasin(Hero):
    pass

#inheritance/pewaris

helix =  Hero("Helix", 100)
blue = Hero_Mage("blue", 100)
roxy = Hero_Assasin("roxy", 100)


print(helix.nama)
print(blue.nama)
print(roxy.nama)