from mcpi.minecraft import Minecraft
mc = Minecraft.create()
answer = input("Create a crater? Y/N ")

if answer == "Y":
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z - 1, 0)
    mc.postToChat("Boom!")
