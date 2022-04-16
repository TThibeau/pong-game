from turtle import Screen, Turtle

def draw_broken_line(WINDOW_HEIGHT):
    tur = Turtle()
    tur.screen.tracer(0)
    tur.hideturtle()
    tur.penup()
    tur.goto(0,-WINDOW_HEIGHT/2)
    tur.penup()
    tur.setheading(90)
    tur.color("white")
    tur.speed("fastest")

    for j in range(0,round(WINDOW_HEIGHT/2),10):
        tur.pendown()
        tur.forward(10)
        tur.penup()
        tur.forward(10)

    tur.hideturtle()

def draw_background(WINDOW_WIDTH,WINDOW_HEIGHT):
    screen = Screen()
    screen.update()
    screen.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
    screen.title(titlestring="Pong game")
    screen.tracer(0)
    screen.bgcolor("black")

    return screen

