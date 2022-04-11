class Hero:

    #private
    __jumlah = 0

    def __init__(self, name):
        self.Nama = name
        Hero.__jumlah += 1

    def getJumlah(self): # berlaku buat object
        return Hero.__jumlah

    def getJumlah1(): # berlaku for class
        return Hero.__jumlah

    @staticmethod # can make two who nya object and class
    def getJumlah2():
        return Hero.__jumlah

    # ada yang lebih efisiens dari staticmethode
    @classmethod
    def getJumlah3(cls):
        return  cls.__jumlah


arcer = Hero('Arcer')
print(arcer.getJumlah()) # 1
gusion = Hero('gusiom')
print(gusion.getJumlah()) # 2
snap = Hero("snap") # 3

print("=========")
print(Hero.getJumlah1()) # class
print(Hero.getJumlah2()) # object class
print(Hero.getJumlah3()) # object class


