#2-8
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

username = input("請輸入姓名:")
message = input("請輸入發言:")
LC.postToChat("<" + username + ">" + message)