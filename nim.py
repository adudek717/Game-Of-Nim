"""
Gra:
    Game of Nim[https://pl.wikipedia.org/wiki/Nim]
    Mozliwosc zagrania[TODO]

Autorzy:
    Aleksander Dudek s20155
    Jakub Słomiński  s18552

Zasady w skrócie:
    Na planszy są 4 rzędy zapałek, w kazdym kolejno 1,3,5 i 7 zapałek. Kazdy gracz wybiera, 
    z którego rzędu bierze zapałki oraz ile (1 lub 2). Przegrywa gracz, który weźmie ostatnią.

Przygotowanie środowiska:
    Język Python oraz bibliioteka easyAI[https://zulko.github.io/easyAI/installation.html]
    UWAGA: Nalezy pobrać wersję 1.0.0.4 - komenda[pip install easyAI==1.0.0.4]

Instruckja
    Wpisujemy python3 nim.py
    W kazdej turze wybieramy rząd oraz ilość zapałek w następującym formacie bez cudzysłowiów: "rząd-zapałki"
    Jeśli chcemy: 
        - z pierwszego rzędu wziąć jedną zapałkę wpisujemy: "0-1"
        - z drugiego rzędu dwie zapałki: "1-2"

"""

from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax


class GameOfNim(TwoPlayersGame):
    def __init__(self, players):
        """
        Initialization of the game and all parameters

        Parameters:
        players ([easyAI.Player.AI_Player, easyAI.Player.AI_Player]):
            2 element list of players, can be Human (Human_Player())
            or AI AI_Player(ai) with artifical inteligence of our choice

        """
        self.players = players
        self.nplayer = 1    # player 1 starts
        self.rows = [1, 3, 5, 7]    # number of matches in each row at start

    def possible_moves(self):
        """
        Calculate possible moves for a player

        Returns:
        list(str):
            Return list of possible moves

        """
        moves = []
        idx = 0
        for matches in self.rows:
            if matches > 1:
                moves.append("{}-2".format(idx))
            if matches > 0:
                moves.append("{}-1".format(idx))
            idx += 1
        return moves

    def make_move(self, move):
        """
        What happens when making a move

        Parameters:
        move list(str):
            Take the row and number of matches separated by '-'
            and remove the amount of matches from the chosen row

        """
        chosenRow = int(move[0])    # set the chosen row
        chosenMatches = int(move[2])    # set the chosen number of matches
        self.rows[chosenRow] -= int(chosenMatches)  # remove matches from a row

    def win(self):
        """
        Checking if a player has won

        Returns:
            bool:
                Player loses if condition is true, wins if false

        """
        matchesLeft = 0
        for matches in self.rows:
            matchesLeft += matches
        return matches <= 0     # who takes the last match wins

    def is_over(self):
        """
        Function checking if the game should not end.

        Returns:
            bool:
                Game ends if true, keeps running when false

        """
        return self.win()   # game stops when a player wins

    def show(self):
        """
        Display the whole game:
            - Instruction
            - Row numbers
            - Matches numbers
            - Actual matches

        """
        # print("Make a move \"row-matches\" for example \"0-1\"")
        print("Rows         Matches")
        for i in range(4):
            print('{}    '.format(i), end='')
            print('|' * self.rows[i], end='')
            print(' ' * (10 - int(self.rows[i])), end='')
            print(self.rows[i])

    def scoring(self):
        """
        Scoring function required by easyAI

        Returns:
            int:
                Between 0 and 100, in our case returns 100 if
                player wins, otherwise returns 0

        """
        return 100 if self.win() else 0  # Scoring for the AI


# Start a match (and store the history of moves when it ends)
ai = Negamax(13)  # The AI will think 13 moves in advance
game = GameOfNim([Human_Player(), AI_Player(ai)])
history = game.play()
