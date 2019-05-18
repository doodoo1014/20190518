import turtle as t

def draw_land():
    lx = -(t.window_width()/2 - 10)
    ly = -(t.window_height()/2 - 20)
    dist = t.window_width() - 20
    t.penup()
    t.setpos(lx,ly)
    t.pendown()
    t.forward(dist)
    t.penup()

def draw_pos(x,y):
    t.clearstamps()
    t.setpos(x,y)
    t.stamp()

    hl = -(t.window_height()/2-20)
    tm = 0

    while True:
        d = (9.8*tm**2)/2
        ny = y - int(d)

        if ny>hl:
            t.goto(x,ny)
            t.stamp()
            t.write("y:%d, d:%d"%(ny,d),False)
            tm += 0.3

        else:
            break

def t_goto(x,y):
    t.goto(x,y)
    t.stamp()
    t.write("x:%d, y:%d"%(x,y))

def clear_screen(x,y):
    t.goto(x,y)
    t.clear()

t.setup(500,600)
t.shape("circle")
t.shapesize(0.3,0.3,0)
t.hideturtle()
t.penup()
#draw_land()
s = t.Screen()
s.onscreenclick(draw_pos,2)
s.onscreenclick(t_goto,1)
s.onscreenclick(clear_screen,3)
s.listen()
