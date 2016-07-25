from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def growTree(x, y, z):
    """Creates a tree at the coordinates given"""
    wood = 17
    leaves = 18

    # trunk
    mc.setBlocks(x, y, z, x, y + 5, z, wood)

    # leaves
    mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
    mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z


growTree(x + 1, y, z)
growTree(x + 3, y, z)
growTree(x + 5, y, z)
growTree(x + 7, y, z)
growTree(x + 9, y, z)
growTree(x + 11, y, z)
growTree(x + 13, y, z)
growTree(x + 15, y, z)
growTree(x + 17, y, z)
