class Hero:
    __jumlah = 0

    def __init__(self, nama, health, armor, damage):
        self.__nama = nama
        self.__health = health
        self.__armor = armor
        self.__damage = damage
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__health * self.__level
        self.__damageBase = self.__damage * self.__level
        self.__armorBase = self.__armor * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property #yg bisa dilihat client
    def info(self):
        return "{} : \n\tLevel : {}\n\tHealth : {}/{}\n\tArmor : {}\n\tDamage : {} ".format(self.__nama,self.__level, self.__health, self.__healthMax, self.__armor, self.__damage)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp +=  addExp
        if (self.__exp >= 100):
            print(self.__nama, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__health * self.__level
            self.__damageBase = self.__damage * self.__level
            self.__armorBase = self.__armor * self.__level

    def attcak(self, musuh):
        self.gainExp = 50


arcer = Hero("arcer", 100, 25, 7)
luois = Hero("Luis", 100, 30, 5)

print(arcer.info)

arcer.attcak(luois)
arcer.attcak(luois)
arcer.attcak(luois)