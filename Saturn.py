import mcpi.minecraft as minecraft
import time
import math
import random

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y+40
z = cor.z

# список неоднородности планеты
S=[35,246,46,80,41,24]

# очистка пространства

craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

# Построение Сатурна
def saturn1(a,c, b,n):
    global S
    for k in range(-400,400):
        # создаём дробный шаг по Y для плотного заполнения поверхности
        y1=0.0755*k
        # проверяем условие на то что значения y1 не будет превышать значение c
        if math.fabs (y1)<= c:
            r = math.sqrt(c**2 - y1**2)
            
            if k <-300:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=-300 and k<-250:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=-250 and k<-200:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=-200 and k<-150:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=-150 and k<-50:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, S[4])
            elif k >=-50 and k<50:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=50 and k<100:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, S[4])
            elif k >=100 and k<150:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=150 and k<200:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=200 and k<250:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, S[5])
            elif k >=250 and k<300:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=300 and k<350:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
            elif k >=350 and k<400:
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 46)
    r1=40
    n1=0
    for l in range (n):
        n1 =random.randint(0,5)
        for j in range(360):
            
            x1 = r1*math.cos((math.pi *j)/180)
            z1 = r1*math.sin((math.pi *j)/180)
        
            craft.setBlock(x+x1,y,z+z1, 46)
        h =random.randint(1,3)
        r1 = r1 + h
       
        
            
saturn1(30,30, 30,15)
