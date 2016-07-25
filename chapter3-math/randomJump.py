from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x += random.randrange(-10, 11)
y += random.randrange(0, 11)
z += random.randrange(-10, 11)
mc.player.setPos(x, y, z)
