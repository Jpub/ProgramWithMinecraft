from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time


def calculateMove():
    """ Changes the x and z variables for a block. If the block
    in front of the block is less than 2 blocks higher it will move
    forward, otherwise it will try to move left, then backwards,
    then finally right."""
    global x
    global y
    global z

    currentHeight = mc.getHeight(x, z) - 1

    forwardHeight = mc.getHeight(x + 1, z)
    rightHeight = mc.getHeight(x, z + 1)
    backwardHeight = mc.getHeight(x - 1, z)
    leftHeight = mc.getHeight(x, z - 1)

    if forwardHeight - currentHeight < 3:
        x += 1
    elif rightHeight - currentHeight < 3:
        z += 1
    elif leftHeight - currentHeight < 3:
        z -= 1
    elif backwardHeight - currentHeight < 3:
        x -= 1

    y = mc.getHeight(x, z)


pos = mc.player.getTilePos()
x = pos.x
z = pos.z
y = mc.getHeight(x, z)

while True:
    # calculate block movement
    calculateMove()

    # place block
    mc.setBlock(x, y, z, 103)

    # wait
    time.sleep(1)

    # remove the block
    mc.setBlock(x, y, z, 0)
