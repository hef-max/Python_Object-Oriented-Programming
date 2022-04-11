class Hero:

    def __init__(self, nama, health):
        self.nama = nama
        self.health = health

    def showInfo(self):
        print("{} dengan health : {}".format(self.nama,self.health))

class Hero_asssasin(Hero):
    def __init__(self, nama):
        super().__init__(nama, 100)
        super().showInfo()

class Hero_mage(Hero):
    def __init__(self, nama):
        super().__init__(nama, 200)
        super().showInfo()

lunox = Hero_asssasin("Lunox")
ruby = Hero_mage("ruby")


