import turtle

class Ball(turtle.Turtle):
    """Class to represent the ball in the Pong game.

    Attributes:
        dx (float): The horizontal speed of the ball.
        dy (float): The vertical speed of the ball.
    """

    def __init__(self):
        """Initialize the ball."""
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.05  # Set the initial horizontal speed
        self.dy = 0.05  # Set the initial vertical speed

    def move(self):
        """Move the ball on the screen."""
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def check_collision(self, paddle_a, paddle_b, pen):
        """Check and handle collisions of the ball with the walls and paddles.

        Args:
            paddle_a (Paddle): The left Paddle.
            paddle_b (Paddle): The right Paddle.
            pen (ScorePen): The score pen.
        """
        # Check for collision with the top and bottom walls
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

        # Check for collision with the right wall
        if self.xcor() > 350:
            self.goto(0, 0)
            self.dx *= -1
            pen.update_score("Player A")

        # Check for collision with the left wall
        elif self.xcor() < -350:
            self.goto(0, 0)
            self.dx *= -1
            pen.update_score("Player B")

        # Check for collision with paddles
        if (self.xcor() < -340 and paddle_a.ycor() + 50 > self.ycor() > paddle_a.ycor() - 50) or \
           (self.xcor() > 340 and paddle_b.ycor() + 50 > self.ycor() > paddle_b.ycor() - 50):
            self.dx *= -1

