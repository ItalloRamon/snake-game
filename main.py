from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

## Create the snake body, by creating 3 turtles as squares 
snake = Snake()
food = Food()

##Create the scoreboard fixed and moving
score_fixed = ScoreBoard()
sc = 0
score_move = ScoreBoard()
score_move.add_score(sc)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision btw the snake and the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

        ##Update the scoreboard
        sc += 1
        score_move.clear()
        score_move.add_score(sc)
    
    #Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_fixed.game_over()

    #Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_fixed.game_over()
                
screen.exitonclick()