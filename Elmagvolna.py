import mcpi.minecraft as minecraft
import math

craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos()

x = cor.x +5
y = cor.y
z = cor.z + 5

# Построение графика sin вдоль оси y
for i in range (2880):
    craft.setBlock(x, y, z, 35, 5)
    
    x=x+0.1
    y=y+0.2*math.sin((math.pi*i)/180)
    #вычисления центра графика по оси Y
    if i ==90:
        y1 = y
# вычисление центра для второго графика по оси Z
for j in range (180):
    z=z-0.2*math.sin((math.pi*j)/180)
    if j ==90:
        z1 = z

x = cor.x+5

# построение второго графика sin вдоль оси Z
for i in range (2880):
    craft.setBlock(x, y1, z1, 35, 14)
    
    x=x+0.1
    z1=z1+0.2*math.sin((math.pi*i)/180)
    
x = cor.x+5
z = cor.z+5

