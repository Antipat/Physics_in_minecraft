import mcpi.minecraft as minecraft
import time
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()
# координаты для Луны
x = cor.x+44
y = cor.y+10
z = cor.z-22

# координаты для Солнце
x0=x+100
y0=y+20
z0=z+22

# очистка пространства

craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

# Построение Луны
def moon(a,c, b):
    
    for k in range(-250,250):
        # создаём дробный шаг по Y для плотного заполнения поверхности
        y1=0.07*k
        # проверяем условие на то что значения y1 не будет превышать значение c
        if math.fabs (y1)<= c:
            r = math.sqrt(c**2 - y1**2)
            # полное покрытие обсидианом
            
            
            for j in range (360):
                x1 = (c/a)*r*math.cos((math.pi *j)/180)
                z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                craft.setBlock(x+x1,y+y1,z+z1, 246)

# Построение Солнце
def sun(a,c, b):
    
    for k in range(-400,400):
        # создаём дробный шаг по Y для плотного заполнения поверхности
        y1=0.0755*k
        # проверяем условие на то что значения y1 не будет превышать значение c
        if math.fabs (y1)<= c:
            r = math.sqrt(c**2 - y1**2)
            
            for j in range (360):
                x1 = (c/a)*r*math.cos((math.pi *j)/180)
                z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                craft.setBlock(x0+x1,y0+y1,z0+z1, 89)

              
sun(30,30,30)

for i in range (40):
    moon(10,10,10)
    time.sleep(0.2)
    craft.setBlocks(x-15,y-15, z-15, x+15, y+15, z+15, 0)
    z=z+2
    # если Луна перекрыла Солнце
    if z==z0:
        craft.postToChat("СОЛНЕЧНОЕ ЗАТМЕНИЕ!")
        

