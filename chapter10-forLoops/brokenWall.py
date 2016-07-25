from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10

# create the list of broken blocks
for row in range(height):
    brokenWall.append([])
    for column in range(width):
        block = brokenBlock()
        brokenWall[row].append(block)

# set the blocks
for row in brokenWall:
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x
