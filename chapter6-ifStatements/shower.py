from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = -14
shwrY = 74
shwrZ = 518

width = 5
height = 5
length = 5

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and shwrY <= y < shwrY + height and shwrZ <= z < shwrZ + length:
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                 shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY, shwrZ,
                 shwrX + width, shwrY + height, shwrZ + length, 0)
