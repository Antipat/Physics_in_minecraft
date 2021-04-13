import mcpi.minecraft as minecraft
import mcpi.block as block
import time

craft = minecraft.Minecraft.create()
cor= craft.player.getTilePos()
x = cor.x+2
y = cor.y
z = cor.z+1

g = 9.81

tren = float(input ("Введите коэффициент трения "))
m = float(input ("Введите значение массы тела "))
F = float(input ("Введите значение силы, действующей на тело "))

#функция, описывающая движение тела
def telo1():
    global x, y, z, s
    craft.setBlocks(x-3,y,z,x, y+2, z+3, 0)
    
    craft.setBlocks(x,y,z,x+3, y+2, z+3, 35, 4)
    time.sleep(0.5)
   
#функция, описывающая вектор силы воздействия
def sila1():
    craft.setBlocks(x-6,y+1,z+1,x-3, y+1, z+1, 0)
    craft.setBlocks(x-3,y+1,z+1,x, y+1, z+1, 35, 2)
    time.sleep(0.3)

#функция, описывающая вектор силы трения
def sila2():
    craft.setBlocks(x+3,y+1,z+1,x+8, y+1, z+1, 0)
    craft.setBlocks(x+8,y+1,z+1,x+3, y+1, z+1, 35, 3)
    time.sleep(0.3)
    
Ftr= tren*g*m    
while True:
    telo1()
          
    if F>=Ftr:
        craft.postToChat("Сила воздействия больше силы трения на "+ str(F-Ftr)+ " Н ")
        for i in range (10):
            telo1()
            sila1()
            sila2()
            x=x+1
            
          
    else:
        telo1()
        

            


    
    
    
