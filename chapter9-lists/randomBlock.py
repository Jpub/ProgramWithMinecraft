from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

blocks = [57, 41, 22, 42, 103]
block = random.choice(blocks)

mc.setBlock(x, y, z, block)
