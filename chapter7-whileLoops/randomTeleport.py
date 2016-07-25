import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0
while count < 5:
    x = random.randrange(-127, 128)
    y = random.randrange(0, 64)
    z = random.randrange(-127, 128)

    mc.player.setTilePos(x, y, z)
    count += 1
    time.sleep(10)
    