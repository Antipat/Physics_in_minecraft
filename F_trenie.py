import mcpi.minecraft as minecraft
import mcpi.block as block
import time

craft = minecraft.Minecraft.create()
cor= craft.player.getTilePos()
x = cor.x
y = cor.y
z = cor.z

F = int(input("Введите значение силы "))

m = int(input("Введите значение массы тела "))

v = float(input("Введите значение коэффициента трения "))

g = 9.81

x1=x+17 # координата для расположения второго тела
craft.setBlock(x1,y,z, 35, 5)

#функция, описывающая движение первого тела
def telo1():
    global x, y, z
    craft.setBlock(x,y,z, 0)
    x=x+2
    craft.setBlock(x,y,z, 41)
    time.sleep(1)
    print("x = "+str(x))


#функция, описывающая движение второго тела после столкновения
def telo2():
    global x1, x, y, z
    craft.setBlock(x1,y,z, 0)
    x1=x1+1
    craft.setBlock(x1,y,z, 35, 5)
    time.sleep(1)
    print("x1 = "+str(x1))

#Вычисление силы трения
F1 = m*v*g

time.sleep(3)
# Вывод введённых значений в чат игры
craft.postToChat(" Сила равна "+ str(F)+ " Н ")
craft.postToChat(" Масса равна "+ str(m)+ " кг ")
craft.postToChat(" коэффициент трения равен "+ str(v))

while True:
    telo1()
    s=x1-x
    craft.postToChat("Растояние = "+ str(s))
    
    if x1-x<=1:
        if F>F1:
            for i in range(5):
                telo2()
            craft.postToChat(" Сила больше силы покоя второго тела на "+ str(F-F1)+ " H ")
                
        else:
            craft.postToChat(" Сила меньше силы покоя второго тела на "+ str(F1-F)+ " H ")
            break
        
            
            
    

            


    
    
    
