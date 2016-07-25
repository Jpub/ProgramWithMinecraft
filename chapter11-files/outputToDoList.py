from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open("toDoList.txt", "r")

for line in toDoList:
    mc.postToChat(line)
