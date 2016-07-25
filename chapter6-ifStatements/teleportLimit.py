from mcpi.minecraft import Minecraft
mc = Minecraft.create()

valid = True

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if not -127 < x < 127:
    valid = False
# check if y is not between -63 and 63
if not -63 < y < 63:
    valid = False
# check if z is not between -127 and 127
if not -127 < z < 127:
    valid = False

if valid:
    mc.player.setPos(x, y, z)
else:
    mc.postToChat("Please enter a valid location")
