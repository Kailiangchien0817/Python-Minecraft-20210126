#2-5
from mcpi.minecraft import Minecraft
LC = Minecraft.create()
while True:
    x,y,z = LC.player.getTilePos()
    block1 = LC.getBlock(x,y-1,z)
    block2 = LC.getBlock(x+1,y-1,z)
    block3 = LC.getBlock(x-1,y-1,z)
    block4 = LC.getBlock(x,y-1,z+1)
    block5 = LC.getBlock(x,y-1,z-1)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9 or block3 == 8 or block3 == 9 or block4 == 8 or block4 == 9 or block5 == 8 or block5 == 9:
        LC.setBlock(x,y-1,z,79)
        LC.setBlock(x+1,y-1,z,79)
        LC.setBlock(x-1,y-1,z,79)
        LC.setBlock(x,y-1,z+1,79)
        LC.setBlock(x,y-1,z-1)
        
        