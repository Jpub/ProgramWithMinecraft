from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

scores = {}

message = ""

while message != "exit":
    print("Click in the Minecraft window")
    time.sleep(10)
    mc.events.clearAll()

    mc.postToChat("Go")

    time.sleep(60)

    hits = mc.events.pollBlockHits()
    numberOfHits = len(hits)
    mc.postToChat("You used your sword " + hits + " times.")

    playerName = input("Enter your name: ")
    scores[playerName] = numberOfHits

    for name in scores:
        print(name + str(scores[name]))

    message = input("Press enter in this window to start ('exit' to quit)")
