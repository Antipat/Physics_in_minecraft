import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x + 15
y=cor.y + 3
z=cor.z + 5

x1 = cor.x+15
z1 = cor. z+20
y1 = y 

def crc1(k1):
    global x, y, z
    for j in range(180):
        z = z+k1*math.sin((math.pi*j)/180)
        x = x+ k1*math.cos((math.pi*j)/180)
        craft.setBlock(x, y, z, 57)
    y=cor.y + 3
    z=cor.z + 5
    
def crc2(k2):
    global x1, y1, z1
    for j in range(180):
        z1 = z1+k2*math.sin((math.pi*j)/180)
        x1 = x1+ k2*math.cos((math.pi*j)/180)
        craft.setBlock(x1, y1, z1, 45)
    
    z1 = cor. z+15
    y1 = y
    
k1=k2=0.01

while True:

    crc1(k1)
    crc2(k2)        
    x = x + 2
    x1 = x1 + 2
    k1=k1+0.02
    k2 = k1   
        
    time.sleep(0.5)
    if k1 >=1:
        break
         
         
