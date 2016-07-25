from mcpi.minecraft import Minecraft
mc = Minecraft.create()


points = int(input("Enter your points: "))
if points > 6:
    mc.player.setPos(32, 18, -38)
elif points > 4:
    mc.player.setPos(60, 20, 32)
elif points > 2:
    mc.player.setPos(112, 10, 112)
elif points <= 2:
    mc.player.setPos(0, 12, 20)
else:
    mc.postToChat("I don't know what to do with that information.")
