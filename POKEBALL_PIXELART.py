import turtle

t = turtle.Turtle()
t.speed(0)
t.color('black')
t.shape('arrow')
t.showturtle()


def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)


def draw_rect(x0, y0, length, height, colour):
    t.color(colour)
    t.fillcolor(colour)
    t.pendown()
    t.begin_fill()

    draw_line(x0, y0, x0 + length, y0)
    draw_line(x0 + length, y0, x0 + length, y0 + height)
    draw_line(x0 + length, y0 + height, x0, y0 + height)
    draw_line(x0, y0 + height, x0, y0)
    t.end_fill()
    t.penup()


# PIXEL SIZE
p = 20


for x in range(-60, 80, 20):
    draw_rect(x, 140, p, p, 'black')


draw_rect(-100, 120, p, p, 'black')
draw_rect(-80, 120, p, p, 'black')

draw_rect(80, 120, p, p, 'black')
draw_rect(100, 120, p, p, 'black')


draw_rect(-120, 100, p, p, 'black')
draw_rect(120, 100, p, p, 'black')

draw_rect(-140, 80, p, p, 'black')
draw_rect(140, 80, p, p, 'black')


for y in range(-60, 80, 20):
    draw_rect(-160, y, p, p, 'black')
    draw_rect(160, y, p, p, 'black')


draw_rect(-140, -80, p, p, 'black')
draw_rect(140, -80, p, p, 'black')

draw_rect(-120, -100, p, p, 'black')
draw_rect(120, -100, p, p, 'black')


draw_rect(-100, -120, p, p, 'black')
draw_rect(-80, -120, p, p, 'black')

draw_rect(80, -120, p, p, 'black')
draw_rect(100, -120, p, p, 'black')


for x in range(-60, 80, 20):
    draw_rect(x, -140, p, p, 'black')


for x in range(-60, 80, 20):

    
    draw_rect(x, 120, p, p, 'red')

for x in range(-80, 100, 20):
    draw_rect(x, 100, p, p, 'red')

for x in range(-100, 120, 20):
    draw_rect(x, 80, p, p, 'red')

for x in range(-120, 140, 20):
    draw_rect(x, 60, p, p, 'red')

for x in range(-140, 160, 20):
    draw_rect(x, 40, p, p, 'red')

for x in range(-140, 160, 20):
    draw_rect(x, 20, p, p, 'red')


for x in range(-140, 160, 20):
   
    
    draw_rect(x, 0, 20, 20, 'black')


for x in range(-40, 40, 20):
    draw_rect(x, 20, 20, 20, 'black')

draw_rect(-60, 0, 20, 20, 'black')

for x in range(-40, 40, 20):
    
    
    draw_rect(x, 0, 20, 20, 'white')


draw_rect(40, 0, 20, 20, 'black')


draw_rect(-60, -20, 20, 20, 'black')


draw_rect(40, -20, 20, 20, 'black')


for x in range(-40, 40, 20):
    draw_rect(x, -40, 20, 20, 'black')

t.goto(-90,-229)
t.color("#FF4F4F")
t.write('POKÉBALL', font = ('Arial', 25 ,'bold'))

t.hideturtle()
turtle.mainloop()