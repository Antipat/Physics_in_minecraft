import mcpi.minecraft as minecraft
import mcpi.block as block
import time

craft = minecraft.Minecraft.create()
cor= craft.player.getTilePos()
x = cor.x+5
y = cor.y
z = cor.z

x1=x+5
y1=y+5
z1=z+5

print ("""

Даны три тела
1 - дерево (5)
2 - дыня (103)
3 - железо (42)

""")


m = int(input("Выберите материал 1, 2 или 3 "))
g = 9.81
V = 1
k=0
rog=1

if m ==1:
    k=5
    ro=0.5
elif m==2:
    k=103
    ro=1
    
elif m==3:
    k=42
    ro=5

craft.setBlocks(x,y,z, x+10, y+10, z+10, 20)
craft.setBlocks(x+1,y+1,z+1, x+9, y+10, z+9, 9)

craft.setBlock(x1,y1,z1, k)

#функция, описывающая движение первого тела
def telo1():
    global x1, y1, z1
    craft.setBlock(x1,y1,z1, 0)
    y1=y1+1
    craft.setBlock(x1,y1,z1, 5)
    time.sleep(1)
    print("x = "+str(x))


#функция, описывающая движение второго тела
def telo2():
    global x1, y1, z1
    craft.setBlock(x1,y1,z1, 0)
    y1=y1+1
    craft.setBlock(x1,y1,z1, 103)
    time.sleep(0.2)
    craft.setBlock(x1,y1,z1, 0)
    y1=y1-1
    craft.setBlock(x1,y1,z1, 103)
    time.sleep(0.2)
    print("x1 = "+str(x1))
    
#функция, описывающая движение третьего тела
def telo3():
    global x1, y1, z1
    craft.setBlock(x1,y1,z1, 0)
    y1=y1-1
    craft.setBlock(x1,y1,z1, 42)
    time.sleep(1)
    print("x = "+str(x))
#Сила Архимеда
Fa = rog*V*g
# Сила тяжести
Ft= (ro*V)*g

time.sleep(3)
craft.postToChat(" Сила Архимеда равна "+ str(Fa)+ " Н ")
craft.postToChat(" Сила Тяжести равна "+ str(Ft)+ " Н ")

    
if m==1:
    craft.postToChat(" Сила Архимеда больше силы тяжести ")
    for i in range (5):
        telo1()
elif m==2:
    craft.postToChat(" Сила Архимеда равна силы тяжести ")
    for i in range (5):
        telo2()
elif m==3:
    craft.postToChat(" Сила Архимеда меньше силы тяжести ")
    for i in range (4):
        telo3()
            
        
            
            
    

            


    
    
    
