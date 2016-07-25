from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"House": (10, 11, 12),
          "Tower": (20, -2, 3),
          "Store room": (6, 2, 1)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
