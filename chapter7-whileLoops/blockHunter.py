from mcpi.minecraft import Minecraft
import math
import time
import random
mc = Minecraft.create()

destX = random.randint(-127, 127)
destZ = random.randint(-127, 127)
destY = mc.getHeight(destX, destZ)

print(destX, destY, destZ)

block = 57
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Block set")

while True:
    pos = mc.player.getPos()
    distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)

    if distance == 0:
        break

    if distance > 100:
        mc.postToChat("Freezing")
    elif distance > 50:
        mc.postToChat("Cold")
    elif distance > 25:
        mc.postToChat("Warm")
    elif distance > 12:
        mc.postToChat("Boiling")
    elif distance > 6:
        mc.postToChat("On fire!")
    elif distance == 0:
        mc.postToChat("Found it")
