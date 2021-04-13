import mcpi.minecraft as minecraft

import mcpi.block as block

import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z

g=9.81
y1=0
z1 = 2

v=10
t=0.5
k=0.01
while True:
    
    
    for i in range(20):
        craft.setBlock(x+5*v, y+y1, z+z1, 35, 3) # создание блока определения пройденного расстояния
        
        craft.setBlock(x,y,z, 35,4)
        time.sleep(t)
        
        y=y+v #увеличение высоты с течением времени
        
        y1 = y1+v*0.001 # параметр, отвечающий за начертания графика прохождения блока
        
        k=k+0.01
        craft.postToChat(" скорость блока v = "+ str(v)) # вывод значения скорости
         
        v=v-g*k # изменение скорости под действием ускорения g
        if v<=1:
            break
    if v<1:
        break

