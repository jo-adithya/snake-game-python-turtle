from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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

    def move(self, ):
        for index in range(self.length - 1, 0, -1):
            position = self.body[index - 1].pos()
            self.body[index].setpos(position)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
