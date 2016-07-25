from mcpi.minecraft import Minecraft
mc = Minecraft.create()

userName = input("Enter your username: ")
message = input("Enter your message: ")
mc.postToChat(userName + ": " + message)
