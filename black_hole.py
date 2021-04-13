#Чёрная дыра

import mcpi.minecraft as minecraft
import time
import math
import random

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

# координаты координаты чёрной дыры
x = cor.x+30
y = cor.y
z = cor.z

# переменная повысоте для притяжения персонажа
y0=cor.y+20
# Очистка пространства
craft.setBlocks(x-10,y,z-10,x+10, y+10,z+10, 0)

# радиус чёрной дыры
r=20
# логическая переменная длядвижения персонажа
bb=False

# Создание чёрной дыры
for i in range (20):
    for j in range (360):
        x1 = r*math.cos((math.pi *j)/180)
        z1 = r*math.sin((math.pi *j)/180)
        craft.setBlock(x+x1,y,z+z1, 119)
    r=r-1
# Первоначальное положение персонажа
craft.player.setTilePos(x-35, y+50,z)

# траектория притяжения небесных тел и персонажа
r1 =20
def aster(x,y,z,r1):
    global bb, r0, y0
    k1 = random.randint(0,15)
    k2 = random.randint(0,15)
    k3 = random.randint(0,15)
    # движение по спирали Архимеда
    for h in range (2000):
        
        cor=craft.player.getTilePos()
        x01=cor.x
        z01 =cor.z
        print(math.fabs(x-cor.x))
        # проверяем нахождение персонажа, непосредственно рядом с чёрной дырой
        if math.fabs(x-cor.x)<=22 and math.fabs(x-cor.x)>=0 and cor.y>y0-19:
            
            craft.postToChat("Вас притягивает чёрная дыра")
            bb=True
        else:
            bb==False
        # вычисление координат движения притянутых небесных тел    
        x2 = r1*math.cos((math.pi *h)/180)
        z2 = r1*math.sin((math.pi *h)/180)
        x3 = 1.2*r1*math.cos((math.pi *h)/180)
        z3 = 1.2*r1*math.sin((math.pi *h)/180)
        x4 = 0.75*r1*math.cos((math.pi *h)/180)
        z4 = 0.75*r1*math.sin((math.pi *h)/180)
        
        y2=h*0.025
        y3=h*0.1
        
        craft.setBlock(x+x2,y-y2,z+z2, 35,k1)
        craft.setBlock(x+x3,y-y2,z+z3, 35,k2)
        craft.setBlock(x+x4,y-y2,z+z4, 35,k3)
        time.sleep(0.001)
        r1=r1-0.01

        # движение персонажа по спирали к чёрной дыре, если он оказался рядом
        #if bb==True:
                                   
            #craft.player.setTilePos(x+x4,y-y3,z+z4)
        #Прерывание цикла, если персонаж или небесные тела приблизились в плотную
        # к чёрной дыре
        #if math.fabs(x-cor.x)<=15 and cor.y<=y0-19:
           #break
        if craft.getBlock(x+x2,y-y2-1,z+z2)==119 or craft.getBlock(x+x3,y-y2-1,z+z3)==119 or craft.getBlock(x+x4,y-y2-1,z+z4)==119:
            break

# движение трёх небесных тел к чёрной дыре
while True:
    #craft.postToChat(str(y0-19))
    aster(x, y+ 40, z, r1)
    # если персонаж достиг чёрной дыры, то прерываем цикл.
    #if cor.y<=y0-19:
            #break
    
    
        
    
