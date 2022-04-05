from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write("Score: ", align=ALIGN, font=FONT)
    
    def add_score(self, add):
        self.goto(60, 270)
        self.write(add, align=ALIGN, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        