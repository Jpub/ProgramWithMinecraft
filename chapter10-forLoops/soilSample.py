from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
depth = 10

blocks = []

for deep in range(10):
    block = mc.getBlock(x, y - deep, z)
    blocks.append(block)

for block in blocks:
    mc.postToChat(str(block))
