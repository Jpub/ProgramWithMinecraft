from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import shelve


def buildStructure(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x, y, z, block.id, block.data)
                z += 1
            x += 1
            z = zStart
        y += 1
        x = xStart


structureDictionary = shelve.open("shelveFile.db")

structureName = input("Enter the structure's name ")

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

buildStructure(x, y, z, structureDictionary[structureName])
