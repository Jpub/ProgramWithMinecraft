class Cat(object):
    owner = "Craig"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def eat(self, food):
        self.weight = self.weight + 0.05
        print(self.name + " is eating " + food)
    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping...")
    def getWeightInGrams(self):
        return self.weight * 1000

fluff = Cat("Fluff", 4.5)
print(fluff.owner)

stella = Cat("Stella", 3.9)
print(stella.owner)
print(fluff.weight)

fluff.eat("tuna")
fluff.eatAndSleep("tuna")

print(fluff.getWeightInGrams())
print(fluff.name)
print(stella.name)

fluff.eat("tuna")
stella.eat("cake")
stella.owner = "Matthew"

print(stella.owner)
print(fluff.owner)
