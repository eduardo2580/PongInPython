import turtle
class ScorePen(turtle.Turtle):
    """Classe para gerenciar a exibição e atualização da pontuação do jogo Pong.

    Attributes:
        game: Uma instância da classe PongGame.
    """

    def __init__(self):
        """Inicializa a caneta de pontuação."""
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self, player):
        """Atualiza a pontuação do jogador e exibe-a na tela.

        Args:
            player (str): O jogador que marcou ponto (Player A ou Player B).
        """
        if player == "Player A":
            self.game.score_a += 1
        else:
            self.game.score_b += 1
        self.clear()
        self.write("Player A: {}  Player B: {}".format(self.game.score_a, self.game.score_b), align="center",
                   font=("Courier", 24, "normal"))
