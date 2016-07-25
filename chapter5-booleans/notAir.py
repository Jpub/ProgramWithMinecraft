from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
notAir = blockType != 0
mc.postToChat("The player is not standing in air: " + str(notAir))
