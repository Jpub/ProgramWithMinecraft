from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import shelve


def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2


def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    structure = []

    print("Please wait...")

    # Copy the structure
    for row in range(height):
        structure.append([])
        for column in range(width):
            structure[row].append([])
            for depth in range(length):
                block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)

    return structure

input("Move to the first position and press ENTER in this window")
pos1 = mc.player.getTilePos()

# get the position of the first corner
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

input("Move to the opposite corner and press ENTER in this window")
pos2 = mc.player.getTilePos()

# get the position of the second corner
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

structure = copyStructure(x1, y1, z1, x2, y2, z2)

# name the structure
structureName = input('What do you want to call the structure? ')

# store the structure in a file
shelveFile = shelve.open("shelveFile.db")
shelveFile[structureName] = structure
shelveFile.close()
