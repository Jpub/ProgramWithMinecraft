from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

depth = 50

for deep in range(depth):
    block = mc.getBlock(x, y - deep, z)
    if block == 56:
        mc.postToChat("A diamond ore is " + str(deep) + " blocks below you.")
        break
else:
    mc.postToChat("There are no diamond ore blocks below you")
