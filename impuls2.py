import mcpi.minecraft as minecraft
import mcpi.block as block
import time

craft = minecraft.Minecraft.create()
cor= craft.player.getTilePos()
x = cor.x
y = cor.y
z = cor.z
m = 1
v = 1
x1=x+25 # координата для расположения второго тела
#функция, описывающая движение первого тела
def telo1():
    global x, y, z
    craft.setBlock(x,y,z, 0)
    x=x+1
    craft.setBlock(x,y,z, 41)
    time.sleep(0.5)
    print("x = "+str(x))
#функция, описывающая движение второго тела
def telo2():
    global x1, x, y, z
    craft.setBlock(x1,y,z, 0)
    x1=x1-5
    craft.setBlock(x1,y,z, 57)
    time.sleep(0.5)
    print("x1 = "+str(x1))
#функция, описывающая движение первого тела после столкновения
def telo11():
    global x, y, z
    craft.setBlock(x,y,z, 0)
    x=x+2
    craft.setBlock(x,y,z, 41)
    time.sleep(0.5)
    print("x = "+str(x))
#функция, описывающая движение второго тела после столкновения
def telo22():
    global x1, x, y, z
    craft.setBlock(x1,y,z, 0)
    x1=x1+2
    craft.setBlock(x1,y,z, 57)
    time.sleep(0.5)
    print("x1 = "+str(x1))

while True:
    telo1()
    telo2()
    p1=3*m*1*v
    p2=m*5*v
    craft.postToChat("Импульс золотого блока = "+str(p1))
    craft.postToChat("Импульс алмазного блока = "+str(p2))
    f=craft.getBlock(x+1, y, z)
    print(f)
    if x1-x<=1:
        while True:
            telo11()
            telo22()
            p1=p2=4*2*v
            craft.postToChat("Импульс золотого блока = "+str(p1))
            craft.postToChat("Импульс алмазного блока = "+str(p2))

            
    

            


    
    
    
