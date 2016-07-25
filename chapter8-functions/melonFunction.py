from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time


def makeMelon(x, y, z):
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y, z, 103)
    time.sleep(10)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

makeMelon(x, y + 1, z)
makeMelon(x, y + 3, z)
makeMelon(x + 2, y, z)
makeMelon(x, y, z)
makeMelon(x, y + 1, z + 2)
makeMelon(x, y, z + 3)
