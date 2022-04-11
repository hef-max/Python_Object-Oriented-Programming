class Hero:
    def __init__(self, nama, health, armor):
        self.__Nama = nama
        self.__Health = health
        self.__Armor = armor
        self.__info = "nama : {} \nhealth : {}".format(self.__Nama, self.__Health)

    @property
    def info(self):
        return self.__info
#-------------------------------------------------
    @property
    def armor(self):
        pass

    @armor.getter # for called like this, have to ada property di atas
    def armor(self): # getter just for called
        return self.__Armor

    @armor.setter
    def armor(self, value):
        self.__Armor = value
#-----------------------------------------------------------------------

arcer = Hero("Arcer", 100, 10)

print(arcer.info) # menggunakan @property menjadikan info ini like var, so tidak usah menggunakan [.info()]

print(arcer.armor) # getter

arcer.armor = 50 # setter
print(arcer.armor)