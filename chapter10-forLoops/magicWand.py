from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(60)

hits = mc.events.pollBlockHits()
block = 103

for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.setBlock(x, y, z, block)
