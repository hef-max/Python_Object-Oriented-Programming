class Hero:

    def __init__(self, inputName, inputJenis, inputHealth, inputArmor):
        # instance var
        self.Name = inputName
        self.Hero = inputJenis
        self.Health = inputHealth
        self.Armor = inputArmor

    # void funct, mothod tanpa return tanpa argument
    def void(self):
        print('hay, nama saya adalah',  self.Name)

    # methode with argument, tanpa return
    def healthup(self, up):
        self.Health += up

    # methode with return
    def gethealth(self):
        return self.Health


hero1 = Hero('alucard', 'assasin', 100, 50)
hero2 = Hero('miya', 'maskamas', 100, 20)

hero1.void()

# hero1.healthup(100)
# print(hero1.gethealth()) # with return
