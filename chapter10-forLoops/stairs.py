from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

stairBlock = 53

for step in range(10):
    mc.setBlock(x + step, y + step, z, stairBlock)
