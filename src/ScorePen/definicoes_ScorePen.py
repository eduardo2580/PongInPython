import turtle

class ScorePen(turtle.Turtle):
    """Class to manage the display and updating of the Pong game score.

    Attributes:
        game (PongGame): An instance of the PongGame class.
    """

    def __init__(self):
        """Initialize the score pen."""
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self, player):
        """Updates the player's score and displays it on the screen.

        Args:
            player (str): The player who scored (Player A or Player B).
        """
        if player == "Player A":
            self.game.score_a += 1
        else:
            self.game.score_b += 1
        self.clear()
        self.write("Player A: {}  Player B: {}".format(self.game.score_a, self.game.score_b), align="center",
                   font=("Courier", 24, "normal"))
