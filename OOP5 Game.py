class Hero():

    def __init__(self, name, health, power_attack, armor):
        self.Name =  name
        self.Health = health
        self.Attack = power_attack
        self.Armor = armor

    def serang(self, lawan):
        print(self.Name + " menyerang " + lawan.Name)
        lawan.diserang(self, self.Attack)

    def diserang(self, lawan, damage_lawan):
        print(self.Name + ' diserang ' + lawan.Name)
        damage_diterima = damage_lawan/self.Armor
        print('damage yang di terima', self.Name, ':' , damage_diterima)
        self.Health -= damage_diterima
        print('darah', self.Name, 'tersisa:', str(self.Health))

riku = Hero('Riku', 100, 50, 10)
yuki = Hero('Yuki', 100, 40, 20)

riku.serang(yuki)
print('\n')
yuki.serang(riku)
