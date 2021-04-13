import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x +5
y=cor.y
z=cor.z - 5

k=0
def ellips(x, z):
    global   y,  k
    for p in range (10):
        
        for j in range(361):
            x = x+k*math.sin((math.pi*j)/180)
        
            y = y+ (k*2)*math.cos((math.pi*j)/180)
            craft.setBlock(x, y, z, 20)
        k=k+0.01 
        
        
            

for i in range (360):
    ellips(x, z)
    k=0
    y = cor.y
    z= z+ 0.1*math.cos((math.pi*i)/180)
    x = x+0.1*math.sin((math.pi*i)/180)

x=cor.x - 25
y=cor.y+6
z=cor.z - 5

while True:
    craft.setBlock(x, y, z, 35,14)
    x=x+1
    if craft.getBlock(x, y, z)==20:
        x=x+10
        for i in range(50):
    
            y1 = 0.5*i
            craft.setBlock(x+i, y-y1,z, 35,1)
            
        
        x=cor.x - 25
        y=cor.y+5
        z=cor.z - 5
        for i in range(100):
    
            y1 = -0.15*i
            craft.setBlock(x+i, y+y1,z, 35,3)
        x=cor.x - 25
        y=cor.y
        z=cor.z - 5
        craft.setBlocks(x, y,z, x, y+6, z, 35,5)
        x=cor.x +35
        craft.setBlocks(x, y,z, x, y-3, z, 35,4)
        break

