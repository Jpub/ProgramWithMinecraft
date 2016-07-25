import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

time.sleep(10)

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

# Compare the difference between the starting position and ending position
xDistance = x2 - x1
yDistance = y2 - y1
zDistance = z2 - z1

#Post the results to the chat
mc.postToChat("The player has moved x: " + str(xDistance) + ", y: "
    + str(yDistance) + ", and z: " + str(zDistance))
