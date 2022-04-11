class Hero:

    def __init__(self, nama, health):
        self.nama =  nama
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} :\n\thealth : {}".format(self.nama, self.health))

class Hero_tank(Hero):
    def __init__(self, nama):
        super().__init__(nama, 200)

    #override/menumpu yg sudah ada
    def showInfo(self):
        print("showInfo di subclass Hero")
        print("{} :\n\ttype : tank\n\thealth : {}".format(
            self.nama,
            self.health
        )
        )

class Hero_mage(Hero):
    def __init__(self, nama):
        super().__init__(nama, 100)


thunder = Hero_tank("thunder")
ruby = Hero_mage("ruby")

thunder.showInfo()
ruby.showInfo()