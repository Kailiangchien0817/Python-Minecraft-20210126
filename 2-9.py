#2-9
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()
LC.setSign(x,y,z+1,63,0,"我愛Minecraft","也愛Python")