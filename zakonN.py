import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x + 1
y=cor.y
z=cor.z



F = int(input("Введите значение силы "))

m =int(input("Введите значение массы тела "))

time.sleep(3)

craft.postToChat(" Сила равна "+ str(F)+ " Н ")

craft.postToChat(" Масса равна "+ str(m)+ " кг ")


a1= float(F/m)

a2 = round(a1, 2)

print (a1)
print (a2)

craft.postToChat(" Ускорение равно "+ str(a2)+ " м/с^2 ")
# Начальное время
t=0
# системное время работы программы
t0=time.perf_counter()
print("Время = ", t0)
#указываем начальный промежуток расстояния
s=0
while True:
    # Создание блока
    craft.setBlock(x+s, y, z, 35, 2)
    time.sleep(0.2)
    #Вычисляем расстояние за промежуток времени t
    s=(a2*(t**2))/2
    #получаем системное время работы программы
    t=time.perf_counter()
    #получаем промежуток времени от начала запуска цикла
    t=t-t0
    print(t)
    #Проверка условия по достижению промежутка 10 секунд
    if t>=10:
        break
