import mcpi.minecraft as minecraft
import time
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x
y = cor.y+20
z = cor.z

# очистка пространства

craft.setBlocks(x-50,y,z-50,x+50,y+50, z+50, 0)

# Построение Луны
def moon_loop(a,c, b, n):
    for k in range(-250,250):
        # создаём дробный шаг по Y для плотного заполнения поверхности
        y1=0.07*k
        # проверяем условие на то что значения y1 не будет превышать значение c
        if math.fabs (y1)<= c:
            r = math.sqrt(c**2 - y1**2)
            # полное покрытие обсидианом
            if n==1:
                craft.postToChat("НОВОЛУНИЕ")
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)
            # малая часть I и IV четверти покрываем снегом (1/4) 
            elif n==2:
                craft.postToChat("РАСТУЩАЯ ЛУНА")
                for j in range (-45,45):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)
                
                for j in range (90,270):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)

            # Половина Луны покрыта снегом
            elif n==3: 
                
                craft.postToChat("РАСТУЩАЯ ЛУНА")
                for j in range (-90,90):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)
                for j in range (90,270):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)

            # 3/4 части Луны покрыты снегом
            elif n==4: 
            
                craft.postToChat("РАСТУЩАЯ ЛУНА")
                for j in range (-135,135):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)
                for j in range (135,225):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)

            # полное заполнение снегом Луны        
            elif n==5:
                craft.postToChat("ПОЛНОЛУНИЕ")
                for j in range (360):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)
            # Покрытие обсидианом 1/4 части Луны
            elif n==6:
                craft.postToChat("СТАРЕЮЩАЯ ЛУНА")
                for j in range (-45,45):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)
                for j in range (90,270):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)

            # Покрытие 1/2 Луны обсидианом    
            elif n==7:
                craft.postToChat("СТАРЕЮЩАЯ ЛУНА")
                for j in range (-90,90):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)
                for j in range (90,270):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)
            # Покрытие Луны 3/4 части обсидианом
            elif n==8:
                craft.postToChat("СТАРЕЮЩАЯ ЛУНА")
                for j in range (-135,135):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 0)
                for j in range (135, 225):
                    x1 = (c/a)*r*math.cos((math.pi *j)/180)
                    z1 = (c/b)*r*math.sin((math.pi *j)/180)
        
                    craft.setBlock(x+x1,y+y1,z+z1, 80)
            
n=1
while True:       
    moon_loop(7,7, 7, n)
    time.sleep(0.5)
    n=n+1
    if n>9:
        n=1

