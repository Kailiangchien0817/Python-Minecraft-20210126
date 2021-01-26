from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()
LC.setBlock(x,y,z+1,7)
LC.setBlock(x,y,z-1,7)
LC.setBlock(x-1,y,z,7)
LC.setBlock(x+1,y,z,7)
LC.setBlock(x+1,y,z+1,7)
LC.setBlock(x-1,y,z+1,7)
LC.setBlock(x+1,y,z-1,7)
LC.setBlock(x+1,y,z-1,7)