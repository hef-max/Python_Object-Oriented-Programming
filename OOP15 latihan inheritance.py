class Hero:

    def __init__(self,nama):
        self.__nama = nama
        self.health_pol = [0,100,200,300,400,600]
        self.damage_pol = [0,10,15,20,25,35]
        self.armor_pol = [0,1,2,3,4,5,10]
        self.__level = 0
        self.__exp = 0

    def show_info(self):
        print("{} :\n\tlevel : {}\n\thealth : {}\n\tarmor : {}\n\tdamage : {}".format(
            self.__nama,
            self.__level,
            self.__health,
            self.__armor,
            self.__damage
        ))

    @property
    def health_pol(self):
        pass

    @property
    def armor_pol(self):
        pass

    @property
    def damage_pol(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pol.setter
    def health_pol(self, input):
        self.__health_pol = input

    @armor_pol.setter
    def armor_pol(self, input):
        self.__armor_pol = input

    @damage_pol.setter
    def damage_pol(self, input):
        self.__damage_pol = input

    @gainExp.setter
    def gainExp(self, input):
        self.__exp = input
        if(self.__exp >= 100):
            self.levelUp = self.__exp//100
            self.__exp -= 100

    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_pol[self.__level]
        self.__armor = self.__armor_pol[self.__level]
        self.__damage = self.__damage_pol[self.__level]


class HeroMage(Hero):
    def __init__(self, nama):
        super().__init__(nama)
        self.health_pol = [0,100,200,300,400,500]
        self.damage_pol = [0,15,20,25,30,35]
        self.armor_pol = [0,1,2,3,4,5,6]
        self.levelUp = 1

class HeroTank(Hero):
    def __init__(self, nama):
        super().__init__(nama)
        self.health_pol = [0,200,300,400,500,600]
        self.damage_pol = [0,10,15,20,25,30]
        self.armor_pol = [0,2,4,6,7,8,10]
        self.levelUp = 1

lunox = HeroMage('lunox')
thunder = HeroTank('thunder')

lunox.show_info()
thunder.show_info()

#up
lunox.gainExp = 150
thunder.gainExp = 160

lunox.show_info()
thunder.show_info()

