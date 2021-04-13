import mcpi.minecraft as minecraft
import math
import time
import random

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x +5
y=cor.y
z=cor.z

# Ядро атома Водорода
craft.setBlocks(x, y,z, x+2, y+2, z+2, 41)
        
# коэффициент эллиптической кривой
c = 0.1

# модель траектории движения электрона вокруг ядра
def traector(c):
    global x, y, z
    for j in range(360):
        z = z+c*math.sin((math.pi*j)/180)
        x = x+ c*math.cos((math.pi*j)/180)
        craft.setBlock(x, y, z, 57)
        time.sleep(0.01)
        craft.setBlock(x, y, z, 0)

      
x=cor.x +6
y=cor.y - 2
z=cor.z 

while True:
    # случайный выбор положения частицы
    f = random.randint(-5, 5)
    # Верхняя часть сферы орбиты электрона
    if f == -5 or f == 5:
        c=0.1        
        y = cor.y+4
        z=cor.z - 4
       
        
    elif f == -4 or f == 4:
        c=0.12        
        y = cor.y+3
        z=cor.z -6
       
        
    elif f == -2 or f == 2:
        c=0.14        
        y = cor.y+2
        z=cor.z -8
        
    elif f == -1 or f == 1:
        c=0.16        
        y = cor.y+1
        z=cor.z -8
        
        
    elif f == 0:
        c=0.18        
        y = cor.y
        z=cor.z -10
        
    
    traector(c)
    
    # Нижняя часть сферы орбиты электрона
    if f == -5 or f == 5:
        c=0.1        
        y = cor.y-4
        z=cor.z - 4
        
        
    elif f == -4 or f == 4:
        c=0.12        
        y = cor.y-3
        z=cor.z -6
       
        
    elif f == -2 or f == 2:
        c=0.14        
        y = cor.y-2
        z=cor.z -8
        
        
    elif f == -1 or f == 1:
        c=0.16       
        y = cor.y-1
        z=cor.z -8
        
        
    elif f == 0:
        c=0.18
        y = cor.y
        z=cor.z -10
        
    traector(c)
   
