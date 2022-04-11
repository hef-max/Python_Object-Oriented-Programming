class Hero:
    #class var
    jumlah_hero = 0

    def __init__(self, inputName, inputJenis, inputHealth, inputArmor):
        # instance var
        self.Name = inputName
        self.Hero = inputJenis
        self.Health = inputHealth
        self.Armor = inputArmor

        Hero.jumlah_hero += 1
        print('membuat hero dengan nama:', inputName)

hero1 = Hero('aluacard', 'assasin', 100, 50)
print(Hero.jumlah_hero)
hero2 = Hero('miya', 'maskamas', 100, 20)
print(Hero.jumlah_hero)