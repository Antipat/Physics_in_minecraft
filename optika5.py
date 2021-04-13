import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x +5
y=cor.y
z=cor.z - 5

k=0.1
def ellips1(x, z):
    global   y,k
        
    for j in range(90, 270):
        x = x+k*math.sin((math.pi*j)/180)
        
        y = y+ (k*2)*math.cos((math.pi*j)/180)
        craft.setBlock(x, y, z, 20)
         
def ellips2(x, z):
    global   y,k
        
    for j in range(90, 270):
        x = x-k*math.sin((math.pi*j)/180)
        
        y = y+ (k*2)*math.cos((math.pi*j)/180)
        craft.setBlock(x, y, z, 20) 
        
        
            

for i in range (360):
    ellips1(x, z)
    
    y = cor.y
    z= z+ 0.05*math.cos((math.pi*i)/180)
    x = x+0.05*math.sin((math.pi*i)/180)
    
x=cor.x+15
y=cor.y
z=cor.z - 5

for i in range (360):
    ellips2(x, z)
    
    y = cor.y
    z= z+ 0.05*math.cos((math.pi*i)/180)
    x = x+0.05*math.sin((math.pi*i)/180)
    
x=cor.x-25
y=cor.y-5
z=cor.z - 5

f=-25    
while True:
    craft.setBlock(x, y, z, 35,14)
    x=x+1
    if craft.getBlock(x, y, z)==20:
        x=x+5
        for i in range(50):
            
            y1 = 0.3*f
            craft.setBlock(x+f, y+y1,z, 35,1)
            f=f+1
        
        x=cor.x - 25
        y=cor.y-5
        z=cor.z - 5
        
        for i in range(100):
    
            y1 = -0.15*i
            craft.setBlock(x+i, y+y1,z, 35,3)
        x=cor.x - 25
        y=cor.y-5
        z=cor.z - 5
        craft.setBlocks(x, y,z, x, y-7, z, 35,5)
        x=cor.x+1
        craft.setBlocks(x, y-7,z, x, y-5, z, 35,4)
        break

