from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()

long=20
big=10
high=7

block=79
air=0

LC.setBlocks(x,y,z,x+long,y+high,z+big,block)
LC.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+big-1,air)
