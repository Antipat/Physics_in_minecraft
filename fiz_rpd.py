import mcpi.minecraft as minecraft

import mcpi.block as block
import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z

a=2
y1=0
z1 = 2

v=1
t=0.1
k=1
craft.setBlocks(x-50,y,z-50,x+50, y+50, z+50, 0)
for j in range (5):
    for i in range(20):
        craft.setBlock(x, y+y1, z+z1, 35, 3) # построение графика пройденного пути от времени 
            
        craft.setBlock(x,y,z, 35,1) # построение графика изменения скорости с течением времени 
        time.sleep(t)
            
        x=x+(a*k)  # масштабное смещение вдоль оси X -как изменяется значение скорости
            
        y1 = y1+ (a*(k**2)/2)/5 # масштабное изменение по оси Y - как изменяется расстояние с течением времени
            
        k=k+0.2 # параметр отвечающий за отсчёт времени
        craft.postToChat(" скорость блока v = "+ str(a*k))
    a=a+0.001
    z=z+4
    x=cor.x+1
    y1=0
    
