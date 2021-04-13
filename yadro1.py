import mcpi.minecraft as minecraft
import math
import time
import random

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x +5
y=cor.y
z=cor.z

# Создание золотой пластины
craft.setBlocks(x, y,z, x, y+10, z+10, 41)

# Задаём координаты для начального радиоактивных частиц        
x=cor.x -10
y=cor.y + 5
z=cor.z+5

while True:
    # движение радиоактивных частиц
    craft.setBlock(x, y, z, 35,14)
    time.sleep(0.15)
    craft.setBlock(x, y, z, 0)
    x=x+1
    # если частица касается золотой пластины,
    # то отлитает в противоположную сторону
    if craft.getBlock(x+1, y, z)==41:
        # Случайный выбор углового коэффициента
        k = random.randint(-10, 10)
        # траектория движения отражённой частицы
        for i in range(20):
            y1 = 0.1*k*i
            craft.setBlock(x-i, y+y1,z, 35,1)
            time.sleep(0.1)
            craft.setBlock(x-i, y+y1,z, 0)
        
        x=cor.x - 10
        y=cor.y + 5
        

