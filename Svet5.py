import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x + 5
y=cor.y
z=cor.z + 5

x1 = cor.x
z1 = cor. z
y1 = y + 10


craft.setBlocks(x-10,y, z-10, x+10, y, z+10, 42)
       
i=0.1
while True:
    craft.setBlock(x1, y1, z, 35, 0)
    if craft.getBlock(x1-1, y1-1, z) == 42:
        
        for j in range(20):
            x2 = random.randint(-2, 2)
            y2 = random.randint(0, 3)
            z2 = random.randint(-2, 2)
            
            craft.setBlock(x1+x2, y1+y2,z+z2, 35,14)
            time.sleep(0.5)
        break
    x1 = x1+1
    i=i+0.1
    y1 = y1 - 2*i    
    time.sleep(0.5)
    
         
         
