import mcpi.minecraft as minecraft
import time

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x + 15
y=cor.y
z=cor.z + 5

x1 = cor.x-20
z1 = cor. z+5
y1 = y + 3

# Пластина, имеющая две одинаковые щели
craft.setBlocks(x,y, z-10, x, y+10, z+10, 5)
craft.setBlocks(x,y+1, z-5, x, y+9, z-5, 0)
craft.setBlocks(x,y+1, z+5, x, y+9, z+5, 0)


while True:
    craft.setBlock(x1, y1, z1, 35, 14)
    x1 = x1+2
    f=x1
    # построение двух частиц, которые будут проходить две щели одновременно
    if craft.getBlock(x1+3,y1,z1-2) == 5:
        for i in range (20):
            craft.setBlock(x1, y1, z-5, 35, 14)
            x1 = x1+2
        x1=f
        for i in range (20):
            craft.setBlock(x1, y1, z+5, 35, 14)
            x1 = x1+2
            
           
       
        
    time.sleep(0.5)
    
         
         
