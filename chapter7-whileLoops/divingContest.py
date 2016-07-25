from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

# repeat the following code while blockAbove is water (8) or flowing water (9)
while blockAbove == 8 or blockAbove == 9:
    # make the loop sleep for 1 seconds
    time.sleep(1)
    pos = mc.player.getPos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    score = score + 1
    # Display the current score
    mc.postToChat("Current score: " + str(score))
    
    
# display the final score after the loop
mc.postToChat("Final Score: " + str(score))
# Use an if statement to check score is greater than or equal to 6
if score > 6:
    # create flowers above them if they are
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
