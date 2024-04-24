import turtle

class Paddle(turtle.Turtle):
    """A class that represents a paddle in a game.

    This class inherits from the turtle.Turtle class and represents a paddle
    object used in a game, such as Pong.

    Attributes:
    - x (int): The x-coordinate of the paddle's initial position.
    - y (int): The y-coordinate of the paddle's initial position.

    Methods:
    - __init__(self, x, y): Initializes a paddle object with the provided x and y coordinates.
    - paddle_up(self): Moves the paddle up by 20 units along the y-axis.
    - paddle_down(self): Moves the paddle down by 20 units along the y-axis.
    """

    def __init__(self, x, y):
        """Initializes the Paddle object.

        Args:
        - x (int): The x-coordinate of the paddle's initial position.
        - y (int): The y-coordinate of the paddle's initial position.
        """
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def paddle_up(self):
        """Moves the paddle up by 20 units along the y-axis."""
        y = self.ycor()
        y += 20
        self.sety(y)

    def paddle_down(self):
        """Moves the paddle down by 20 units along the y-axis."""
        y = self.ycor()
        y -= 20
        self.sety(y)
