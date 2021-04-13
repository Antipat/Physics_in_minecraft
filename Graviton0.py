import mcpi.minecraft as minecraft
#import mcpi.block as block
import time
import math


craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x+10
y=cor.y + 10
z=cor.z +10
 
x1=x+1
z1=z
y1=y

s= 1.5*(10**11)
G = 6.67 *(10**(-11))
Ms = 1.99*(10**30)
Mz = 5.97*(10**24)


F = G*(Ms*Mz)/(s**2)

def sun(a,b,c):
    for k in range(-250,250):
    # создаём дробный шаг по Y для плотного заполнения поверхности
        y1=0.07*k
    # проверяем условие на то что значения y1 не будет превышать значение c
        if math.fabs (y1)<= c:
            r = math.sqrt(c**2 - y1**2)
    
            for j in range (360):
                x1 = (c/a)*r*math.cos((math.pi *j)/180)
                z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                craft.setBlock(x+x1,y+y1,z+z1, 35,4)
            
    
    
def earth(x1, z1,a, b, c):
    for k in range(-250,250):
    # создаём дробный шаг по Y для плотного заполнения поверхности
        y1=0.07*k
    # проверяем условие на то что значения y1 не будет превышать значение c
        if math.fabs (y1)<= c:
            r = math.sqrt(c**2 - y1**2)
    
            for j in range (360):
                x1 = (c/a)*r*math.cos((math.pi *j)/180)
                z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                craft.setBlock(x+x1,y+y1,z+z1, 57)
sun(10,10,10)

y=cor.y + 10
z=cor.z -40
z1 = z
x1 = x+1

while True:
    craft.postToChat("Сила притяжения равна " + str(F)+ " H ")
    #определяем координаты положения земли после каждого шага
    for k in range(360):
        z = z+1*math.sin((math.pi*k)/180)
        x = x+ 1.2*math.cos((math.pi*k)/180)
        z1 = z
        x1 = x+1
        s=k%10
        if s==0:
            earth (x1, z1, 5, 5, 5)
        
            
            
        
       
   
