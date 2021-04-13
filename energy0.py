import mcpi.minecraft as minecraft
import mcpi.block as block
import time

craft = minecraft.Minecraft.create()
cor= craft.player.getTilePos()
x = cor.x+1
y = cor.y
z = cor.z

m = 1
v = 0
g = 9.81
H = 100
y1 = y+H
t = 0
s = 0
y11 = H

#функция, описывающая движение тела

def telo1():
    global x, y1, z, t, s, y11, v, g, H
    Ep = m*g*y11
    Ek = (m*(v**2))/2
    craft.postToChat("Потенциальная энергия золотого блока = "+str(Ep))
    craft.postToChat("Кинетическая энергия золотого блока = "+str(Ek))
    y11 = H-s
    craft.setBlock(x,y1-s,z, 2)
    
    if 49<y11<51:
        craft.setBlock(x,y1-s,z, 35,2)
        print("Ep = "+str(Ep))
        print("Ek = "+ str(Ek))
        
    time.sleep(0.5)
    print("y = "+ str(y11))
    t=t+0.01
    s=(g*(t**2))/2
    v=g*t
   




while True:
    telo1()
          
    if y11<=1:
        break
        

            


    
    
    
