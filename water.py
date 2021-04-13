import mcpi.minecraft as minecraft
import time

craft = minecraft.Minecraft.create()
cor= craft.player.getTilePos()
x = cor.x+5
y = cor.y
z = cor.z+2


print ("""

Даны три тела
1 - Лёд 
2 - Вода 
3 - Пар 

""")
d=[[1,1,1,1,1],
   [1,1,1,1,1],
   [1,1,1,1,1],
   [1,1,1,1,1],
   [1,1,1,1,1]]

m = int(input("Выберите тело 1, 2 или 3 "))

def w1():
    global x,y,z
    craft.setBlocks(x,y,z, x+1, y+1, z+1, 35, 4)
    time.sleep(0.05)
    
def w2():
    global x,y,z
    
    craft.setBlocks(x,y,z, x+1, y+1, z+1, 35,3)
    time.sleep(0.05)
    
def w3():
    global x,y,z
    craft.setBlocks(x,y,z, x+2, y+2, z+2, 35, 0)
    time.sleep(0.05)
 
    

if m==1:
    x=cor.x+10
    z=cor.z+10
    y=cor.y+5
    for m in range(10):
        for k in range(5):
            for i in range (5):
                for j in range (5):
                    if d[i][j] == 1:
                        w1()
                    x=x+5
                x=cor.x+10
                y=y+5
            y=cor.y+5
            x=cor.x+10
            z=z+5
        z=cor.z+10

        
elif m==2:
    
        
    for m in range(10):
        for k in range(5):
            for i in range (5):
                
                for j in range (5):
                    if d[i][j] == 1:
                        w2()
                        
                    x=x+8
                                       
                x=cor.x+5
                y=y+8
            y=cor.y
            x=cor.x+5
            z=z+8
        z=cor.z+2
        craft.setBlocks(x,y,z, x+50, y+40, z+50, 0)
        x=cor.x+10
        z=cor.z+10
        y=cor.y+5
        for k in range(5):
            for i in range (5):
                for j in range (5):
                    if d[i][j] == 1:
                        w1()
                    x=x+5
                x=cor.x+10
                y=y+5
            y=cor.y+5
            x=cor.x+10
            z=z+5
        z=cor.z+10
        craft.setBlocks(x,y,z, x+50, y+40, z+50, 0)
            
    
elif m==3:
    for m in range(10):
        for k in range(5):
            for i in range (5):
                for j in range (5):
                    if d[i][j] == 1:
                        w3()
                    x=x+10
                x=cor.x+5
                y=y+10
            y=cor.y
            x=cor.x+5
            z=z+10
        z=cor.z +2
        time.sleep(5)
        craft.setBlocks(x,y,z, x+50, y+50, z+50, 0)
        
        for k in range(5):
            for i in range (5):
                
                for j in range (5):
                    if d[i][j] == 1:
                        w2()
                        
                    x=x+8
                                       
                x=cor.x+5
                y=y+8
            y=cor.y
            x=cor.x+5
            z=z+8
        z=cor.z+2
        time.sleep(5)
        craft.setBlocks(x,y,z, x+50, y+40, z+50, 0)
        x=cor.x+10
        z=cor.z+10
        y=cor.y+5
        for k in range(5):
            for i in range (5):
                for j in range (5):
                    if d[i][j] == 1:
                        w1()
                    x=x+5
                x=cor.x+10
                y=y+5
            y=cor.y+5
            x=cor.x+10
            z=z+5
        z=cor.z+10
        time.sleep(5)
        craft.setBlocks(x,y,z, x+50, y+40, z+50, 0)
            


    
    
    
