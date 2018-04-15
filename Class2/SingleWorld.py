class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingleWorld(metaclass=Singleton):

    def sayHello(self):
        print("I am HelloWorld object and i live at: " + self.__repr__() + "\n")


x = SingleWorld()
x.sayHello()

y = SingleWorld()
y.sayHello()

z = SingleWorld()
z.sayHello()