import time

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

    def build(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z + self.depth, 4)

        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,
                     self.x + self.width - 1, self.y + self.height - 1, self.z + self.depth - 1, 0)

        self.buildWindows()
        self.buildDoor()

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z + self.depth, 0)

    def buildWindows(self):
        mc.setBlock(self.x + (self.width / 4 * 3), self.y + 2, self.z, 0)
        mc.setBlock(self.x + (self.width / 4), self.y + 2, self.z, 0)

    def buildDoor(self):
        mc.setBlocks(self.x + (self.width / 2), self.y + 1, self.z, self.x + (self.width / 2), self.y + 2, self.z, 0)


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostHouse = Building(x, y, z, 10, 6, 8)
shop = Building(x + 12, y, z, 8, 12, 10)
hospital = Building(x + 25, y, z - 1, 30, 40, 30)
bakery = Building(x - 12, y - 5, z, 9, 11, 13)


ghostHouse.build()
shop.build()
hospital.build()
bakery.build()

time.sleep(30)

ghostHouse.clear()
shop.clear()
hospital.clear()
bakery.clear()
