from mcpi.minecraft import Minecraft
mc = Minecraft.create()

class Location(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


bedroom = Location(64, 52, -8)
mc.player.setTilePos(bedroom.x, bedroom.y, bedroom.z)
