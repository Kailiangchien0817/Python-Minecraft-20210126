#practice1
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

import random
while True:
  x,y,z = LC.player.getTilePos()
  flowertype = random.randrange(0,9)
  LC.setBlock(x,y,z-1,38,flowertype)
