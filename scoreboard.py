from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()