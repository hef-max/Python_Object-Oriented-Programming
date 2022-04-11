# abc = abstarct base class

from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button): #memaksa button class

    def click(self):
        print("Go to : {}".format(self.link))

    @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return  self.__link


tombol = PushButton("www.abc.com")
tombol.click()



