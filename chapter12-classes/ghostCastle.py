from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time


class NamedBuilding(object):
    def __init__(self, x, y, z, width, height, depth, name):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

        self.name = name

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

    def getInfo(self):
        return self.name + "'s location is at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def buildWindows(self):
        mc.setBlock(self.x + (self.width / 4 * 3), self.y + 2, self.z, 0)
        mc.setBlock(self.x + (self.width / 4), self.y + 2, self.z, 0)

    def buildDoor(self):
        mc.setBlocks(self.x + (self.width / 2), self.y + 1, self.z, self.x + (self.width / 2), self.y + 2, self.z, 0)


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostCastle = NamedBuilding(x, y, z, 10, 16, 16, "Ghost Castle")
ghostCastle.build()
mc.postToChat(ghostCastle.getInfo())

time.sleep(30)

ghostCastle.clear()
