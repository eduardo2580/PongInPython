import turtle

class Paddle(turtle.Turtle):
    """Uma classe que representa uma raquete em um jogo.

    Esta classe herda da classe turtle.Turtle e representa um objeto de raquete
    usado em um jogo, como Pong.

    Atributos:
    - x (int): A coordenada x da posição inicial da raquete.
    - y (int): A coordenada y da posição inicial da raquete.

    Métodos:
    - __init__(self, x, y): Inicializa um objeto de raquete com as coordenadas x e y fornecidas.
    - paddle_up(self): Move a raquete para cima por 20 unidades ao longo do eixo y.
    - paddle_down(self): Move a raquete para baixo por 20 unidades ao longo do eixo y.
    """

    def __init__(self, x, y):
        """Inicializa o objeto Paddle.

        Args:
        - x (int): A coordenada x da posição inicial da raquete.
        - y (int): A coordenada y da posição inicial da raquete.
        """
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def paddle_up(self):
        """Move a raquete para cima por 20 unidades ao longo do eixo y."""
        y = self.ycor()
        y += 20
        self.sety(y)

    def paddle_down(self):
        """Move a raquete para baixo por 20 unidades ao longo do eixo y."""
        y = self.ycor()
        y -= 20
        self.sety(y)