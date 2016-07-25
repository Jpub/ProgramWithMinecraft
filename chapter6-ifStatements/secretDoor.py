from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        mc.setBlocks(5, -2, 5, 6, -1, 6, 0)
    else:
        mc.setBlocks(4, -3, 4, 7, -3, 4, 10)
else:
    mc.postToChat("Place an offering on the pedestal.")
