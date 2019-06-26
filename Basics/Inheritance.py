#Inheritance

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal): #Inherit all the methods Mammal Class
    #pass
    def bark(self):
        print("bark")


class Cat(Mammal):
    #pass
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()