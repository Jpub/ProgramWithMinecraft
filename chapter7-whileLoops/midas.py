# connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
water = 9

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)

    if blockBelow != air and blockBelow != water:
        # change the block below the player to gold
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
