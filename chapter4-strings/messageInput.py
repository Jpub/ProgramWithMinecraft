from mcpi.minecraft import Minecraft
mc = Minecraft.create()

message = input("Enter your message: ")
mc.postToChat(message)
