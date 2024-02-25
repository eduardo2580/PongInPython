import turtle
class Ball(turtle.Turtle):
    """Classe para representar a bola no jogo Pong.

    Atributos:
        dx (float): Velocidade horizontal da bola.
        dy (float): Velocidade vertical da bola.
    """

    def __init__(self):
        """Inicializa a bola."""
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.05
        self.dy = 0.05

    def move(self):
        """Move a bola na tela."""
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def check_collision(self, paddle_a, paddle_b, pen):
        """Verifica e trata as colisões da bola com as paredes e os Paddles.

        Args:
            paddle_a (Paddle): O Paddle esquerdo.
            paddle_b (Paddle): O Paddle direito.
            pen (ScorePen): A caneta de pontuação.
        """
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

        if self.xcor() > 350:
            self.goto(0, 0)
            self.dx *= -1
            pen.update_score("Player A")

        elif self.xcor() < -350:
            self.goto(0, 0)
            self.dx *= -1
            pen.update_score("Player B")

        if (self.xcor() < -340 and paddle_a.ycor() + 50 > self.ycor() > paddle_a.ycor() - 50) or \
           (self.xcor() > 340 and paddle_b.ycor() + 50 > self.ycor() > paddle_b.ycor() - 50):
            self.dx *= -1
