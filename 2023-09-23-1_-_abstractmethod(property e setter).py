from abc import ABC, abstractmethod
class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return 123
    @name.setter
    def name(self, name): ...
class Foo(AbstractFoo):
    def __init__(self, name): #1:
        super().__init__(name)
        print('Sou inútil')
foo = Foo('Bar') #2: #3:
print(foo.name) #4: