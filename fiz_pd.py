import mcpi.minecraft as minecraft

import mcpi.block as block

import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z

y1=0
z1 = 2


t=2
# очистка пространства
craft.setBlocks(x-50,y,z-50,x+50, y+50, z+50, 0)
    
while True:
    # движение блока с определённой скоростью
    for i in range(10):
           
        craft.setBlock(x,y,z, 35,1)
        time.sleep(t)
        craft.setBlock(x,y,z, 0)
        x=x+1
        
    x=cor.x+1 # обнуляем координату X для блока
    # изменение скорости блока
    t=t-0.2
    
    # проверяем достижение задержки нуля
    if t<=0:
        break


#craft.postToChat(" скорость блока v = "+ str(v))
    
#craft.setBlock(x, y+y1, z+z1, 35, 3)
#y1 = y1+ v*t1 
        
    #y1=0
    #z1=z1+2    
    #x=cor.x+1
