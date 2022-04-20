# Small pong python game
import turtle
from pprint import pprint
from functools import partial

# var to control if the game is still in play or not
play_game = True

# Defaults
left_score = 0
right_score = 0
total_to_win = 5
default_ball_speed = 1.5

window = turtle.Screen();
window.title("Pong by Mistfel")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Stop the game
def stop_game():
	global play_game
	play_game = False

# Restart the game
def restart_game():
	global play_game
	global left_score
	global right_score
	
	play_game = True
	left_score = 0
	right_score = 0

	update_score(pen, left_score, right_score)

# Update the score
def update_score(pen, left_score, right_score):
	pen.clear()
	if left_score == total_to_win:
		pen.write("Player A Wins! Press Return to restart.", align="center", font=("Courier", 24, "normal"))
		stop_game()
	elif right_score == total_to_win:
		pen.write("Player B Wins! Press Return to restart.", align="center", font=("Courier", 24, "normal"))
		stop_game()
	else:
		pen.write("Player A: {}  Player B: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

# Update the ball speed
def reset_ball_speed():
	ball.direction_x = default_ball_speed;

# Paddle Creation
def paddle_creation(paddle_side):
	paddle = turtle.Turtle()
	paddle.speed(0)
	paddle.shape('square')
	paddle.color('white')
	paddle.shapesize(stretch_wid=5, stretch_len=1)
	paddle.penup()
	if paddle_side == "left":
  		paddle.goto(-350, 0)
	else:
		paddle.goto(350, 0)
	return paddle

# Left Paddle
left_paddle = paddle_creation('left')

# Right Paddle
right_paddle = paddle_creation('right')

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.direction_x = default_ball_speed
ball.direction_y = default_ball_speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
update_score(pen, left_score, right_score)

# Function
def paddle_move(paddle, direction):
	if direction == "up":
		paddle.sety(paddle.ycor() + 20)
	else:
		paddle.sety(paddle.ycor() - 20)

# Keyboard Binding
window.listen()
window.onkeypress(partial(paddle_move, left_paddle, "up"), "w")
window.onkeypress(partial(paddle_move, left_paddle, "down"), "s")
window.onkeypress(partial(paddle_move, right_paddle, "up"), "Up")
window.onkeypress(partial(paddle_move, right_paddle, "down"), "Down")
window.onkeypress(partial(restart_game), "Return")

# Main game loop
while True:
	if play_game:
		window.update()

		# Move the ball
		ball.setx(ball.xcor() + ball.direction_x)
		ball.sety(ball.ycor() + ball.direction_y)

		# Y - Border checking
		if ball.ycor() > 290:
			ball.sety(290)
			ball.direction_y *= -1
		elif ball.ycor() < -290:
			ball.sety(-290)
			ball.direction_y *= -1

		# X - Border checking
		if ball.xcor() > 390:
			ball.goto(0, 0)
			ball.direction_x *= -1
			left_score += 1
			reset_ball_speed()
			update_score(pen, left_score, right_score)
		elif ball.xcor() < -390:
			ball.goto(0, 0)
			ball.direction_x *= -1
			right_score += 1
			reset_ball_speed()
			update_score(pen, left_score, right_score)

		# Paddle collision detection
		if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
			ball.setx(340)	
			ball.direction_x *= -1.25

		if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
			ball.setx(-340)	
			ball.direction_x *= -1.25
	else:
		window.update()
