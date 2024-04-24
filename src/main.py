from Ball.ball_definitions import Ball
from Paddle.paddle_definitions import Paddle
from ScorePen.score_pen_definitions import ScorePen
import turtle

class PongGame:
    """Class to manage the Pong game."""

    def __init__(self):
        """
        Initializes the Pong game.

        Initializes the game screen, configures the window dimensions and title,
        sets background colors, and the screen update rate. Also initializes
        the score values, creates the objects of game elements (paddles,
        ball, and score pen), and configures keyboard controls.
        """
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        self.score_a = 0
        self.score_b = 0

        self.paddle_a = Paddle(-350, 0)
        self.paddle_b = Paddle(350, 0)
        self.ball = Ball()
        self.pen = ScorePen()

        self.listen_keyboard()

    def listen_keyboard(self):
        """
        Configures keyboard controls.

        Enables keyboard event listening in the game window and associates
        the 'w' and 's' keys to move paddle A up and down, respectively,
        and the up and down arrow keys to move paddle B.
        """
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a.paddle_up, "w")
        self.wn.onkeypress(self.paddle_a.paddle_down, "s")
        self.wn.onkeypress(self.paddle_b.paddle_up, "Up")
        self.wn.onkeypress(self.paddle_b.paddle_down, "Down")

    def run(self):
        """
        Runs the main game loop.

        Continuously updates the game screen, moves the ball, and checks collisions
        with the paddles. This method constitutes the main game loop, which runs
        continuously until the game is terminated.
        """
        while True:
            self.wn.update()
            self.ball.move()
            self.ball.check_collision(self.paddle_a, self.paddle_b, self.pen)

if __name__ == "__main__":
    game = PongGame()
    game.run()
