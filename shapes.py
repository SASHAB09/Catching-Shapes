import turtle


class Shape:
    def __init__(self, shape_type, x, y, shape_color):
        self.x = x
        self.y = y
        self.color = shape_color
        self.shape = turtle.Turtle()
        self.shape.speed(0)
        self.shape.penup()
        self.shape.hideturtle()
        self.shape.goto(x, y)   
        self.shape.color(shape_color)
        self.shape.shape(shape_type)
        self.shape.shapesize(2, 2)

    def move(self):
        self.shape.sety(self.shape.ycor() - 20)

    def hide(self):
        self.shape.hideturtle()

    def show(self):
        self.shape.showturtle()
