import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

T=0 # Период
R=11 # Радиус окружности
N=0  # Количество оборотов
time.perf_counter() # запуск отсчёта системного времени
while True:
    
    for j in range(360):
        z = z+0.2*math.sin((math.pi*j)/180)
        x = x+ 0.2*math.cos((math.pi*j)/180)
        craft.setBlock(x, y, z, 57)
        
        time.sleep(0.1)
        
        craft.setBlock(x, y, z, 0)
    N=N+1 # Подсчёт количества оборотов
    T=time.perf_counter()/N  # Вычисление перода
    craft.postToChat("Период = " + str(T))
    # Вычисление частоты
    n= 1/T  
    craft.postToChat("Частота = " + str(n))
    # Вычисление угловой скорости
    w = 2*(math.pi)*n
    craft.postToChat("Угловая скорость = " + str(w))
    # Вычисление линейной скорости
    V = w*R
    craft.postToChat("Линейная скорость = " + str(V))
    # Вычисление центростремительного ускорения
    a=(w**2)*R
    craft.postToChat("Ускорение = " + str(a))
