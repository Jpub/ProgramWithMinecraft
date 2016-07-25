from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
aboveGround = y >= highestBlockY
mc.postToChat("The player is above ground: " + str(aboveGround))
