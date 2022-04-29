from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake-game/data.txt", "r") as data:
            self.highscore = int(data.read())
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
            with open("snake-game/data.txt", "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()