#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Set x, y, and z variables to represent coordinates
x = 10.0
y = 110.0
z = 12.0

#Change the player's position
mc.player.setPos(x, y, z)
