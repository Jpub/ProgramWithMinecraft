class Bird(object):
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
    def birdcall(self):
        print("chirp")
    def fly(self):
        print("flap")
class Penguin(Bird):
    def swim(self):
        print("swimming")
    def birdcall(self):
        print("sort of a quack")
    def fly(self):
        print("Penguins cannot fly :(")
class Parrot(Bird):
    def __init__(self, name, wingspan, color):
        self.name = name
        self.wingspan = wingspan
        self.color = color

gardenBird = Bird("Geoffrey", 12)
gardenBird.birdcall()
gardenBird.fly()
sarahThePenguin = Penguin("Sarah", 10)
sarahThePenguin.swim()
sarahThePenguin.fly()
sarahThePenguin.birdcall()
freddieTheParrot = Parrot("Freddie", 12, "blue")

print(freddieTheParrot.color)
freddieTheParrot.fly()
freddieTheParrot.birdcall()
