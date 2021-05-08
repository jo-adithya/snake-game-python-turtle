from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.score = 0
        with open('high_score.txt', mode='r') as f:
            self.high_score = int(f.read())
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as f:
                f.write(str(self.score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
