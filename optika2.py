import mcpi.minecraft as minecraft
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


    
