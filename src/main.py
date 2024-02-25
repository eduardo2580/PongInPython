from Ball.definicoes_ball import Ball
from Paddle.definicoes_paddle import Paddle
from ScorePen.definicoes_ScorePen import ScorePen
import turtle

class PongGame:
    """Classe para gerenciar o jogo Pong."""

    def __init__(self):

        """
        Inicializa o jogo Pong.

        Inicializa a tela do jogo, configura as dimensões e título da janela,
        define as cores de fundo e a taxa de atualização da tela. Também inicializa
        os valores dos pontos, cria os objetos dos elementos do jogo (pádelas,
        bola e caneta para pontuação) e configura os controles do teclado.
        """
        ...
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
        Configura os controles do teclado.

        Habilita a escuta de eventos de teclado na janela do jogo e associa
        as teclas 'w' e 's' para mover a pádela A para cima e para baixo,
        respectivamente, e as teclas de seta para cima e para baixo para
        mover a pádela B.
        """

        self.wn.listen()
        self.wn.onkeypress(self.paddle_a.paddle_up, "w")
        self.wn.onkeypress(self.paddle_a.paddle_down, "s")
        self.wn.onkeypress(self.paddle_b.paddle_up, "Up")
        self.wn.onkeypress(self.paddle_b.paddle_down, "Down")

    def run(self):

        """
        Executa o loop principal do jogo.

        Atualiza continuamente a tela do jogo, move a bola e verifica as colisões
        com as pádelas. Este método constitui o loop principal do jogo, que é executado
        continuamente até que o jogo seja encerrado.
        """

        while True:
            self.wn.update()
            self.ball.move()
            self.ball.check_collision(self.paddle_a, self.paddle_b, self.pen)

if __name__ == "__main__":
    game = PongGame()
    game.run()