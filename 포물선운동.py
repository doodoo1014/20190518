import turtle as t
import math

tm = 0.3
vx = 0
vy = 0
dx = 0
dy = 0
g = 9.8
velo = 0
ang = 0

def draw_pos(x,y):
    velo = t.numinput("입력 : ", "속도 : ",50,10,100)
    ang = math.radians(t.numinput("입력 : ", "각도 : ",45,0,360))
    t.clear()
    t.hideturtle()
    t.setpos(x,y)
    t.showturtle()
    t.stamp()
    
    hl = -(t.window_height()/2)
    vx = velo * math.cos(ang)
    vy = velo * math.sin(ang)

    while True:
        vy = vy + (-9.8) * tm
        dy = t.ycor() + (vy * tm) - (g*tm**2)/2
        dx = t.xcor() + (vx * tm)

        if dy>hl:
            t.goto(dx,dy)
            t.stamp()
        else:
            break

t.setup(600,600)
t.shape("circle")
t.shapesize(0.3,0.3,0)
t.penup()
s = t.Screen()
s.onscreenclick(draw_pos)
s.listen()
