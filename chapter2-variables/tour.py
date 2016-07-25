#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

#Set x, y, and z variables to represent coordinates
x = 64
y = 0
z = -43

#Change the player's position
mc.player.setTilePos(x, y, z)

#Wait 10 seconds
time.sleep(10)

#Set x, y, and z variables to represent coordinates
x = 70
y = 0
z = 144

#Change the player's position
mc.player.setTilePos(x, y, z)
