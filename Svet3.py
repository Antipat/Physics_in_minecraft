import mcpi.minecraft as minecraft
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x+7
y=cor.y
z=cor.z+7
# стеклянная среда
craft.setBlocks(x-5, y-1,z-5, x+10, y+10, z+5, 20)

y=y+10
# луч падающий
for i in range(20):
    
    y1 = 0.577*i
    craft.setBlock(x+i, y+y1,z, 35,1)
# луч преломленный    
for i in range(20):
    y1 = 2.82*i
    craft.setBlock(x-i, y-y1,z, 35,3)
    

 
