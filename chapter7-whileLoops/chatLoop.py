from mcpi.minecraft import Minecraft
mc = Minecraft.create()

userName = input("Enter your username: ")

while True:
    message = input("Enter your message: ")
    if message == "exit":
        break
    mc.postToChat(userName + ": " + message)
