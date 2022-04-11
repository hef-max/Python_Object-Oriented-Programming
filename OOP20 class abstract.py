#membuat class abstract
# abc = abstarct base class

from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass

class PushButton(Button): #memaksa button class

    def click(self):
        print("push button click")

class RadioButton(Button):

    def click(self):
        print("radio button click")


tombol = PushButton()
tombol2 = RadioButton()

tombol.click()
tombol2.click()