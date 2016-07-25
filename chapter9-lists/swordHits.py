from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

#Wait 60 seconds
time.sleep(60)

#Get the list of block hits
blockHits = mc.events.pollBlockHits()

#Display the length of the block hits list to chat
blockHitsLength = len(blockHits)
mc.postToChat("Your score is " + str(blockHitsLength))
