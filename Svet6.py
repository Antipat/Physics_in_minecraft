import mcpi.minecraft as minecraft
import random
import time

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x + 15
y=cor.y
z=cor.z + 5

x1 = cor.x-20
z1 = cor. z+5
y1 = y + 1

# пластина со щелью
craft.setBlocks(x,y, z-10, x, y+10, z+10, 5)
craft.setBlocks(x,y+1, z, x, y+9, z, 0)
       
s=0
while True:
    craft.setBlocks(x1, y1, z1-2, x1, y1+8, z1+2, 35, 0)
    x1 = x1+1
    f=x1
    if craft.getBlock(x1,y1,z1-2) == 5:
        for i in range (20):
            craft.setBlocks(x1, y1, z1, x1, y1+8, z1+1, 35, 0)
            x1 = x1+1
        x1=f
        for i in range (20):
            craft.setBlocks(x1, y1, z1+s, x1, y1+8, z1+s, 35, 0)
            x1 = x1+1
            s =0.5*i
        x1=f    
        for i in range (20):
            craft.setBlocks(x1, y1, z1+s, x1, y1+8, z1+s, 35, 0)
            x1 = x1+1
            s =-0.5*i
        x1=f
        break
    time.sleep(0.5)
    
         
         
