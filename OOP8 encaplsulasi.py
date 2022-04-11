class Hero:
    def __init__(self, name, health, attackpower):
        # this is private supaya ga bisa dirubah
        self.__Name = name
        self.__Health = health
        self.__Damage = attackpower

    #getter #called private
    def getName(self):
        return self.__Name
    def getHealth(self):
        return self.__Health
    def getDamage(self):
        return self.__Damage

    #setter (like same up but changed value in var)
    def diserang(self, value):
        self.__Health -= value
    def change(self, newDamage):
        self.__Damage = newDamage


argus = Hero('Argus', 100, 5)

print(argus.__dict__)
print(argus.getName()) # how to call name with getter
print(argus.getHealth())

argus.diserang(5) # no calling, without get
print(argus.getHealth())
print(argus.__dict__)

argus.change(10)
print(argus.__dict__)




