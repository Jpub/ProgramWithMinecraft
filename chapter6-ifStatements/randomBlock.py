import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Generate a random number between 1-10 here
result = random.randrange(1, 11)


if result == 10:  # result is 10
    block = 56  # diamond ore
elif result > 5:  # result is greater than 5, block is iron ore
    block = 15
# otherwise block is lava
else:
    block = 10

pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y - 1, pos.z, block)
