from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def getWoolState(color):
    """Takes a color as a string and returns the wool block state
    for that color"""

    if color == "pink":
        blockState = 6
    elif color == "black":
        blockState = 15
    elif color == "grey":
        blockState = 7
    elif color == "red":
        blockState = 14
    elif color == "green":
        blockState = 5
    elif color == "brown":
        blockState = 0
    elif color == "yellow":
        blockState = 4
    elif color == "blue":
        blockState = 11
    elif color == "light blue":
        blockState = 3
    elif color == "purple":
        blockState = 10
    elif color == "cyan":
        blockState = 9
    elif color == "orange":
        blockState = 1
    elif color == "light grey":
        blockState = 8

    return blockState

colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
