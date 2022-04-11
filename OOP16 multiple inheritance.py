class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)

class TipeTeam:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Hero(Team, TipeTeam): #multiple inheritance
    def __init__(self, nama, health):
        self.nama = nama
        self.health =  health

rogers = Hero("rogers", 100)
rogers.setTeam("merah")
rogers.setTipe("penyerang")

rogers.showTeam()
rogers.showTipe()