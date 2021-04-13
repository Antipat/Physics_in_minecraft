import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()
l=craft.player.getTilePos()

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
