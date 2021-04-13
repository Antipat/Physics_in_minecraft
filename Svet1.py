import mcpi.minecraft as minecraft
import math

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()

x=cor.x+2
y=cor.y
z=cor.z+2

# Создание модели зеркала (отражающей поверхности)
craft.setBlocks(x-5, y-1,z-5, x+10, y-1, z+5, 79)

# падающий луч света 
for i in range(20):
    
    y1 = 0.5*i
    craft.setBlock(x+i, y+y1,z, 35,1)

# Отражённый луч света    
for i in range(20):
    y1 = 0.5*i
    craft.setBlock(x-i, y+y1,z, 35,3)
    

 
