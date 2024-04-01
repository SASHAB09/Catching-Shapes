import turtle


class Text:
    def __init__(self, x, y, text):
        self.text = text
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.goto(x, y)
        self.pen.color('black')
        self.x = x
        self.y = y
        self.write_text(text)

    def write_text(self, text):
        self.pen.clear()
        self.pen.write(text, align='center', font=('Arial', 16, 'normal'))