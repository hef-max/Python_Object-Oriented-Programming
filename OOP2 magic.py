class Hero:
    def __init__(self, inputName, inputJenis, inputHealth, inputArmor):
        # instance var
        self.Name = inputName
        self.Hero = inputJenis
        self.Health = inputHealth
        self.Armor = inputArmor

hero1 = Hero('aluacard', 'assasin', 100, 50)
hero2 = Hero('miya', 'maskamas', 100, 20)

print(hero1.__dict__)
print(hero2.__dict__)