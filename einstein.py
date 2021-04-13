import mcpi.minecraft as minecraft
import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

# координаты для первого саженца
x=cor.x
y=cor.y
z=cor.z

# координаты для второго саженца
x1=x
y1=y
z1=z+10

# алгоритм движения второго саженца
def raceta(x1,y1,z1):
    craft.setBlocks(x1,y1,z1, x1+2,y1+2,z1+2, 20)
    craft.setBlock(x1+1,y1+1,z1+1,6)
    time.sleep(0.5)
    craft.setBlocks(x1,y1,z1, x1+2,y1+2,z1+2,0)
    
time.sleep(5)

# полёт саженца вверх со световой скоростью
for i in range(25):
    time.sleep(0.1)
    raceta(x1,y1,z1)
    y1=y1+1
    # рост дерева на Земле
    if i<=10:
        craft.setBlock(x-2,y,z,6)
    elif i>=10 and i<15:
        craft.setBlocks(x-2,y,z,x-2,y+3, z, 17)
    elif i>=15 and i<20:
        craft.setBlocks(x-7,y+4,z-5,x+3,y+4, z+5, 18)
    elif i>=20 and i<=25:
        craft.setBlocks(x-6,y+5,z-4,x+2,y+5, z+4, 18)

# полёт саженца к Земле со световой скоростью
for i in range (25):
    y1=y1-1
    raceta(x1,y1,z1)
    # рост дерева на Земле
    if i>=0 and i<10:
        craft.setBlocks(x-5,y+6,z-3,x+1,y+6, z+3, 18)
    elif i>=10 and i<15:
        craft.setBlocks(x-4,y+7,z-2,x,y+7, z+2, 18)
    elif i>=15 and i<20:
        craft.setBlocks(x-3,y+8,z-1,x-1,y+8, z+1, 18)
    elif i>=20 and i <=25:
        craft.setBlocks(x-2,y+9,z,x-2,y+9, z, 18)
        
# зафиксируем прилетевший саженец       
craft.setBlocks(x1,y1,z1, x1+2,y1+2,z1+2, 20)
craft.setBlock(x1+1,y1+1,z1+1,6)   
