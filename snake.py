from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.length = 3
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            body = Turtle(shape="square")
            body.penup()
            body.color("white")
            body.setpos(x_pos, 0)
            self.body.append(body)
            x_pos -= 20
