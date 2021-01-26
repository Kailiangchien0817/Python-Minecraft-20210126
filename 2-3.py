from mcpi.minecraft import Minecraft
LC = Minecraft.create()

import random,time
while True:
    x,y,z = LC.player.getTilePos()

    color=random.randrange(0,16)
    LC.setBlocks(x+10,y,z+10,x-10,y,z-10,95,color)
    time.sleep(3)
