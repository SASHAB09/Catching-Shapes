import turtle
import time
import random
from shapes import Shape
from text import Text


class Game:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.bgcolor("white")
        self.win.title("Catching Circles")
        self.win.tracer(0)
        self.shapes = []
        self.score = 0
        self.start_time = time.time()
        self.duration = 20
        self.score_text = Text(-200, 250, f"Score: {self.score}")
        self.timer_text = Text(200, 250, f"Timer: {self.duration}")

    def create_shape(self):
        x = random.randint(-250, 250)
        y = 250
        random_color = random.choice(['red', 'green', 'blue', 'yellow'])
        random_shape = random.choice(['circle', 'square', 'triangle', 'turtle', 'arrow'])
        new_shape = Shape(random_shape, x, y, random_color)
        new_shape.show()
        self.shapes.append(new_shape)

    def move_shapes(self):
        for shape in self.shapes:
            shape.move()

            if shape.shape.ycor() < -250:
                self.shapes.remove(shape)
                shape.hide()

    def on_click_shape(self, x, y):
        for shape in self.shapes:
            shape_x = shape.x
            # shape_y = shape.y

            if shape.shape.distance(x, y) < 40 and shape.shape.shape() == 'circle':
                self.shapes.remove(shape)
                shape.hide()
                self.score += 10
            elif shape.shape.distance(x, y) < 40 and shape.shape.shape() != 'circle':
                self.shapes.remove(shape)
                shape.hide()
                self.score -= 5

            self.score_text.write_text(f"Score: {self.score}")

            # if x in shape_x + 40 or shape_x - 40:
            #     if y in shape_y + 40 or shape_y - 40:
            #         if shape.shape == "circle":
            #             self.score += 10
            #         else:
            #             self.score -= 5

    def update_timer(self):
        time_passed = int(time.time() - self.start_time)
        time_left = max(0, int(self.duration) - time_passed)
        self.timer_text.write_text(f"Timer: {time_left}")
        return time_left > 0

    def start(self):
        self.win.listen()
        self.win.onclick(self.on_click_shape)

        while self.update_timer():
            self.win.update()
            self.create_shape()
            self.move_shapes()
            time.sleep(.1)

        else:
            self.win.textinput("GAME OVER!", f"HIGH SCORE: {self.score}")
