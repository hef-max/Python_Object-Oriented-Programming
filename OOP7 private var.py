class Hero:
    jumlah = 0
    def __init__(self, name, health):
        self.Name = name
        self.Health = health

        # var intance private
        self.__private = 'this is private'
        # var instance protected
        self._protected =  'this is protected' # cuman 1 andeskor


hero = Hero('lina', 100)

print(hero.__dict__)
print(hero._protected) # tidak berlaku seperti private
