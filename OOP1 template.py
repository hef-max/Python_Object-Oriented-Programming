class Hero: # template
    pass

hero1 = Hero() # object / intance
hero2 = Hero()

hero1.name = 'rachel'
hero1.health = 100

hero2.name = 'anbu'
hero2.health = 200

print(hero1.__dict__)
print(hero2.__dict__)