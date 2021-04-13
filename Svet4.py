import mcpi.minecraft as minecraft
import mcpi.block as block

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x + 5
y=cor.y
z=cor.z + 5

x1 = x-10
y1 = y+2

#Создание усечёной стеклянной пирамиды (призма)
def piramide(s, k):
    global x, y, z
    t=s/2
    for i in range(k):
        craft.setBlocks(x,y, z, x+s, y, z+s, 20)
        x=x+1
        y=y+1
        z=z+1
        s=s-2

piramide(11,5)

while True:
    craft.setBlock(x1, y1, z, 35, 0)
    if craft.getBlock(x1+1, y1, z) == 20:
        x1=x1+7
        for i in range(20):
            s1 = 3*i
            craft.setBlock(x1+i, y1-s1,z, 35,14)
        for i in range(20):
            
            s2 = 2*i
            craft.setBlock(x1+i, y1-s2,z, 35,1)
            
        for i in range(20):
            s3 = 1*i
            craft.setBlock(x1+i, y1-s3,z, 35,4)
        for i in range(20):
            
            s4 = 0*i
            craft.setBlock(x1+i, y1-s4,z, 35,5)
            
        for i in range(20):
            s5 = -1*i
            craft.setBlock(x1+i, y1-s5,z, 35,3)
        for i in range(20):
            
            s6 = -2*i
            craft.setBlock(x1+i, y1-s6,z, 35,11)
            
        for i in range(20):
            
            s7 = -3*i
            craft.setBlock(x1+i, y1-s7,z, 35,10)
        break
    x1 = x1+1 
        

    
         
         
