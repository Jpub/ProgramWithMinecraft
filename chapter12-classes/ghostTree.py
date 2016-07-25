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


class Tree(Building):
    def build(self):
        """Creates a tree at the coordinates given"""
        wood = 17
        leaves = 18

        # trunk
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 5, self.z, wood)

        # leaves
        mc.setBlocks(self.x - 2, self.y + 6, self.z - 2, self.x + 2, self.y + 6, self.z + 2, leaves)
        mc.setBlocks(self.x - 1, self.y + 7, self.z - 1, self.x + 1, self.y + 7, self.z + 1, leaves)

    def clear(self):
        """Clears a tree at the coordinates given"""
        wood = 0
        leaves = 0

        # trunk
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y + 5, self.z, wood)

        # leaves
        mc.setBlocks(self.x - 2, self.y + 6, self.z - 2, self.x + 2, self.y + 6, self.z + 2, leaves)
        mc.setBlocks(self.x - 1, self.y + 7, self.z - 1, self.x + 1, self.y + 7, self.z + 1, leaves)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostTree = Tree(x, y, z, 10, 6, 8)
ghostTree.build()

time.sleep(10)

ghostTree.clear()
