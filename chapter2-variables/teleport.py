#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Set x, y, and z variables to represent coordinates
x = 10
y = 110
z = 12

#Change the player's position
mc.player.setTilePos(x, y, z)
