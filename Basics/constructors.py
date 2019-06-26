# classes

class Point:
    # This __init__ is a constructor
    def __init__(self, x, y): #self is reference to current opject
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10,20)
print(point.x)

print("\n")

#exercise

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
#john.talk()
#print(john.name)
john.talk()
print("\n")
bob = Person("Bob Smith")
bob.talk()