# Author:  Amy Salley
# Date:  14 June 2020
# Description:  This program plays an abstract board game called Gess. Gess is
# a variant of the games Go and Chess. The complete rules for the game can be
# found here:  https://www.chessvariants.com/crossover.dir/gess.html

import pygame


class GessGame:
    """
    The GessGame class represents an abstract board game called Gess. Has methods
    to get the game board, game state, current player, and to make a move.
    Communicates with the GamePiece class to determine a valid game piece and move
    direction. Communicates with the Move class to determine a valid move and update
    the board.
    """

    def __init__(self):
        """
        Initializes the playing board, the state of the game to "UNFINISHED", and
        the current player to the player with the black stones, represented by 'x'.
        The player with white stones is represented by 'o'.
        """
        self._board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "o", " ", "o", " ", "o", "o", "o", "o",
                        "o", "o", "o", "o", " ", "o", " ", "o", " ", " "],
                       [" ", "o", "o", "o", " ", "o", " ", "o", "o", "o",
                        "o", " ", "o", " ", "o", " ", "o", "o", "o", " "],
                       [" ", " ", "o", " ", "o", " ", "o", "o", "o", "o",
                        "o", "o", "o", "o", " ", "o", " ", "o", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "o", " ", " ", "o", " ", " ", "o", " ",
                        " ", "o", " ", " ", "o", " ", " ", "o", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "x", " ", " ", "x", " ", " ", "x", " ",
                        " ", "x", " ", " ", "x", " ", " ", "x", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", "x", " ", "x", " ", "x", "x", "x", "x",
                        "x", "x", "x", "x", " ", "x", " ", "x", " ", " "],
                       [" ", "x", "x", "x", " ", "x", " ", "x", "x", "x",
                        "x", " ", "x", " ", "x", " ", "x", "x", "x", " "],
                       [" ", " ", "x", " ", "x", " ", "x", "x", "x", "x",
                        "x", "x", "x", "x", " ", "x", " ", "x", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                        " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                       ]
        self._game_state = "UNFINISHED"
        self._current_player = "x"

    def get_board(self):
        """ Returns the current board configuration. """
        return self._board

    def get_game_state(self):
        """ Returns the current state of the game. """
        return self._game_state

    def get_current_player(self):
        """ Returns the current player. """
        return self._current_player

    def pygame_board(self, board):
        """
        Uses Pygame to create a board. Gets user input from the mouse to
        move the player's game piece and play the game.
        """
        # Initialize the board dimensions.
        width = 30
        height = 30
        margin = 2
        frame = 75

        # Define the board and game piece colors.
        brown = (143, 82, 9)
        dark_brown = (92, 65, 13)
        black = (0, 0, 0)
        gray = (53, 69, 94)
        white = (255, 255, 255)
        off_white = (235, 241, 250)
        green = (147, 219, 167)

        pygame.init()

        # Initialize the display.
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Gess Game")

        # Set background images.
        bamboo = pygame.image.load("bamboo.png")
        bamboo = pygame.transform.scale(bamboo, (800, 800))
        screen.blit(bamboo, (0, 0))
        pygame.draw.rect(screen, dark_brown, (72, 72, 647, 647))
        wood = pygame.image.load("wood.png")
        wood = pygame.transform.scale(wood, (638, 638))
        screen.blit(wood, (77, 77))

        playing = True
        click_1 = True

        # Draw the game board.
        for row in range(20):
            for col in range(20):

                pygame.draw.line(screen, brown, ((frame + (width+margin)*col), frame),
                                 ((frame + (width+margin)*col), (800 - frame - 10)), 2)

                pygame.draw.line(screen, brown, (frame, (frame + (width + margin) * col)),
                                 ((800 - frame - 10), (frame + (width + margin) * col)), 2)

                # Draw the black stones.
                if board[row][col] == "x":
                    pygame.draw.circle(screen, black,
                                       [int(frame + ((margin + width) * col + margin) + width / 2),
                                        int(frame + ((margin + height) * row + margin) + height / 2)], 12)
                    pygame.draw.circle(screen, gray,
                                       [int(frame + ((margin + width) * col + margin) + width / 2),
                                        int(frame + ((margin + height) * row + margin) + height / 2)], 10)

                # Draw the white stones.
                if board[row][col] == "o":
                    pygame.draw.circle(screen, black,
                                       [int(frame + ((margin + width) * col + margin) + width / 2),
                                        int(frame + ((margin + height) * row + margin) + height / 2)], 13)
                    pygame.draw.circle(screen, off_white,
                                       [int(frame + ((margin + width) * col + margin) + width / 2),
                                        int(frame + ((margin + height) * row + margin) + height / 2)], 11)

        # Create a text display to show the current player or if the game has been won.
        font = pygame.font.Font("CaviarDreams.ttf", 20)

        turn = self.get_current_player()
        won = self.get_game_state()

        if turn == "x":
            text_to_print = "Black's turn"
        else:
            text_to_print = "White's turn"

        if won != "UNFINISHED":
            if won == "BLACK_WON":
                text_to_print = "Black won! Game over"
            else:
                text_to_print = "White won! Game over"

        text = font.render(text_to_print, True, black, white)
        text_rect = text.get_rect()
        text_rect.center = (120, 40)
        screen.blit(text, text_rect)

        pygame.display.update()

        # Play the game!
        while playing:
            event = pygame.event.wait()

            # End the game if the Pygame window is closed.
            if event.type == pygame.QUIT:
                playing = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEWHEEL:
                pass

            # First click selects game piece to move.
            if event.type == pygame.MOUSEBUTTONDOWN and click_1:
                click_1 = False
                pos1 = pygame.mouse.get_pos()

                # Convert the mouse position to board coordinates.
                x1 = (pos1[0] - frame) // (width + margin)
                y1 = (pos1[1] - frame) // (height + margin)

                # Highlight the selected game piece.
                pygame.draw.rect(screen, green, (int((pos1[0]-(1.5 * width))),
                                                 int((pos1[1]-(1.5 * height))), 3 * width,
                                                 3 * height), 4)
                pygame.display.update()

            # Second click selects position to move game piece.
            elif event.type == pygame.MOUSEBUTTONDOWN and not click_1:
                pos2 = pygame.mouse.get_pos()

                # Convert mouse position to board coordinates.
                x2 = (pos2[0] - frame) // (width + margin)
                y2 = (pos2[1] - frame) // (height + margin)

                # Highlight the selected move
                pygame.draw.rect(screen, green, (int(pos2[0]-(1.5 * width)),
                                                 int(pos2[1]-(1.5 * height)), 3 * width,
                                                 3 * height), 4)
                pygame.display.update()

                # Call the make_move method to complete the move if it is valid.
                if self.get_game_state() == "UNFINISHED":
                    self.make_move(x1, y1, x2, y2)
                else:
                    playing = False

    def make_move(self, x1, y1, x2, y2):
        """
        Takes as parameters the coordinates of the piece being moved and the desired
        location of the move. Communicates with the GamePiece class to validate the
        game piece and move direction.  Communicates with the Move class to validate
        the move and make the move.  Updates the game board, the game state, and the
        current player after a valid move. Returns True for a valid move. Returns False
        if the move is invalid.
        """
        # Make sure the piece is moving.
        if x1 == x2 and y1 == y2:
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        # Make sure current and new piece centers are on the board.
        if x1 <= 0 or x2 <= 0:
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        elif x1 >= 19 or x2 >= 19:
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        elif y1 <= 0 or y1 >= 19:
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        elif y2 <= 0 or y2 >= 19:
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        player = self.get_current_player()

        #  Make sure both players have valid rings.
        if not self.check_ring(self.get_board())[0]:
            self._game_state = "WHITE_WON"
            print("White won. Game over")
            return False

        if not self.check_ring(self.get_board())[1]:
            self._game_state = "BLACK_WON"
            print("Black won. Game over")
            return False

        #  Check if a player has won.
        if self._game_state != "UNFINISHED":
            return False

        game_piece = GamePiece(self.get_board(), player, x1, y1)
        new_game_piece = GamePiece(self.get_board(), player, x2, y2)

        # Check for a valid piece
        if not game_piece.valid_piece():
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        # Find the move direction
        x_change = x2 - x1
        y_change = y2 - y1

        move_spaces = max(abs(x_change), abs(y_change))

        # Check for a 3 square limit on the move.
        # If more than a 3 square move is attempted, but the game piece
        # does not allow it, the move is invalid, and False is returned.
        if game_piece.move_three() and move_spaces > 3:
            print("Invalid")
            self.pygame_board(self.get_board())
            return False

        piece = game_piece.playing_piece()
        move = Move(piece, player)

        # Create a copy of the board.
        new_board = [[i for i in row] for row in self.get_board()]

        # Move diagonally up and left.
        if x_change < 0 and y_change < 0:
            if abs(y_change / x_change) != 1.0:
                print("Invalid")
                self.pygame_board(self.get_board())
                return False

            if not game_piece.move_up_left():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.up_left(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move up.
        if x_change == 0 and y_change < 0:
            if not game_piece.move_up():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.up(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move diagonally up and right.
        if x_change > 0 and y_change < 0:
            if abs(y_change / x_change) != 1.0:
                print("Invalid")
                self.pygame_board(self.get_board())
                return False

            if not game_piece.move_up_right():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.up_right(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move left.
        if x_change < 0 and y_change == 0:
            if not game_piece.move_left():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.left(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move right.
        if x_change > 0 and y_change == 0:
            if not game_piece.move_right():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.right(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move diagonally down and left.
        if x_change < 0 and y_change > 0:
            if abs(y_change / x_change) != 1.0:
                print("Invalid")
                self.pygame_board(self.get_board())
                return False

            if not game_piece.move_down_left():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.down_left(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move down.
        if x_change == 0 and y_change > 0:
            if not game_piece.move_down():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.down(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        # Move diagonally down and right.
        if x_change > 0 and y_change > 0:
            if abs(y_change / x_change) != 1.0:
                print("Invalid")
                self.pygame_board(self.get_board())
                return False

            if not game_piece.move_down_right():
                print("Invalid")
                self.pygame_board(self.get_board())
                return False
            else:
                if not move.down_right(new_board, x1, y1, move_spaces):
                    print("Invalid")
                    self.pygame_board(self.get_board())
                    return False
                self._board = new_board

        #  See if the current player won.
        if not self.check_ring(self.get_board())[0]:
            self._game_state = "WHITE_WON"
            print("White won. Game over")

        if not self.check_ring(self.get_board())[1]:
            self._game_state = "BLACK_WON"
            print("Black won. Game over")

        # Change players at the end of the turn.
        if player == "x":
            self._current_player = "o"
        else:
            self._current_player = "x"

        self.pygame_board(self.get_board())
        return True

    def check_ring(self, board):
        """
        Checks to see if both players have rings remaining.  Takes the game board to
        check as a parameter.  Returns a Boolean tuple for the existence of a black
        ring and a white ring.
        """
        white_ring = False
        black_ring = False

        for row in range(1, 19):
            for column in range(1, 19):

                if board[row][column] == " ":

                    center = board[row][column]
                    up_left = board[row - 1][column - 1]
                    up = board[row - 1][column]
                    up_right = board[row - 1][column + 1]
                    left = board[row][column - 1]
                    right = board[row][column + 1]
                    down_left = board[row + 1][column - 1]
                    down = board[row + 1][column]
                    down_right = board[row + 1][column + 1]

                    piece = [[up_left, up, up_right],
                             [left, center, right],
                             [down_left, down, down_right]]

                    if piece == [['o', 'o', 'o'], ['o', ' ', 'o'], ['o', 'o', 'o']]:
                        white_ring = True

                    if piece == [['x', 'x', 'x'], ['x', ' ', 'x'], ['x', 'x', 'x']]:
                        black_ring = True

        return black_ring, white_ring


class Move:
    """
    The Move class represents a move in the Gess Game.  Has methods to move in each
    of the eight directions.  Communicates with the GessGame class to determine a
    valid move and complete the move if it is valid.
    """

    def __init__(self, piece, player):
        """
        Takes as parameters and initializes the 3x3 game piece and the current player.
        """
        # self._new_board = new_board
        self._piece = piece
        self._player = player

    def up_left(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece up and to the left.
        Returns the new game board if the move was valid. Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y - 2][old_x - 2],
                      new_board[old_y - 2][old_x - 1],
                      new_board[old_y - 2][old_x],
                      new_board[old_y - 1][old_x - 2],
                      new_board[old_y][old_x - 2]]
        if new_spaces != [" ", " ", " ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y - 2][old_x - 2] = self._piece[0][0]
        new_board[old_y - 2][old_x - 1] = self._piece[0][1]
        new_board[old_y - 2][old_x] = self._piece[0][2]
        new_board[old_y - 1][old_x - 2] = self._piece[1][0]
        new_board[old_y - 1][old_x - 1] = self._piece[1][1]
        new_board[old_y - 1][old_x] = self._piece[1][2]
        new_board[old_y][old_x - 2] = self._piece[2][0]
        new_board[old_y][old_x - 1] = self._piece[2][1]
        new_board[old_y][old_x] = self._piece[2][2]
        new_board[old_y - 1][old_x + 1] = " "
        new_board[old_y][old_x + 1] = " "
        new_board[old_y + 1][old_x - 1] = " "
        new_board[old_y + 1][old_x] = " "
        new_board[old_y + 1][old_x + 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.up_left(new_board, old_x - 1, old_y - 1, move_spaces - 1)

    def up(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece up. Returns the new
        game board if the move was valid.  Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y - 2][old_x - 1],
                      new_board[old_y - 2][old_x],
                      new_board[old_y - 2][old_x + 1]]
        if new_spaces != [" ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y - 2][old_x - 1] = self._piece[0][0]
        new_board[old_y - 2][old_x] = self._piece[0][1]
        new_board[old_y - 2][old_x + 1] = self._piece[0][2]
        new_board[old_y - 1][old_x - 1] = self._piece[1][0]
        new_board[old_y - 1][old_x] = self._piece[1][1]
        new_board[old_y - 1][old_x + 1] = self._piece[1][2]
        new_board[old_y][old_x - 1] = self._piece[2][0]
        new_board[old_y][old_x] = self._piece[2][1]
        new_board[old_y][old_x + 1] = self._piece[2][2]
        new_board[old_y + 1][old_x - 1] = " "
        new_board[old_y + 1][old_x] = " "
        new_board[old_y + 1][old_x + 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.up(new_board, old_x, old_y - 1, move_spaces - 1)

    def up_right(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece up and to the right.
        Returns the new game board if the move was valid. Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y - 2][old_x],
                      new_board[old_y - 2][old_x + 1],
                      new_board[old_y - 2][old_x + 2],
                      new_board[old_y - 1][old_x + 2],
                      new_board[old_y][old_x + 2]]
        if new_spaces != [" ", " ", " ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y - 2][old_x] = self._piece[0][0]
        new_board[old_y - 2][old_x + 1] = self._piece[0][1]
        new_board[old_y - 2][old_x + 2] = self._piece[0][2]
        new_board[old_y - 1][old_x] = self._piece[1][0]
        new_board[old_y - 1][old_x + 1] = self._piece[1][1]
        new_board[old_y - 1][old_x + 2] = self._piece[1][2]
        new_board[old_y][old_x] = self._piece[2][0]
        new_board[old_y][old_x + 1] = self._piece[2][1]
        new_board[old_y][old_x + 2] = self._piece[2][2]
        new_board[old_y - 1][old_x - 1] = " "
        new_board[old_y][old_x - 1] = " "
        new_board[old_y + 1][old_x - 1] = " "
        new_board[old_y + 1][old_x] = " "
        new_board[old_y + 1][old_x + 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.up_right(new_board, old_x + 1, old_y - 1, move_spaces - 1)

    def left(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece to the left. Returns
        the new game board if the move was valid.  Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y - 1][old_x - 2],
                      new_board[old_y][old_x - 2],
                      new_board[old_y + 1][old_x - 2]]
        if new_spaces != [" ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y - 1][old_x - 2] = self._piece[0][0]
        new_board[old_y - 1][old_x - 1] = self._piece[0][1]
        new_board[old_y - 1][old_x] = self._piece[0][2]
        new_board[old_y][old_x - 2] = self._piece[1][0]
        new_board[old_y][old_x - 1] = self._piece[1][1]
        new_board[old_y][old_x] = self._piece[1][2]
        new_board[old_y + 1][old_x - 2] = self._piece[2][0]
        new_board[old_y + 1][old_x - 1] = self._piece[2][1]
        new_board[old_y + 1][old_x] = self._piece[2][2]
        new_board[old_y - 1][old_x + 1] = " "
        new_board[old_y][old_x + 1] = " "
        new_board[old_y + 1][old_x + 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.left(new_board, old_x - 1, old_y, move_spaces - 1)

    def right(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece to the right.
        Returns the new game board if the move was valid.  Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y - 1][old_x + 2],
                      new_board[old_y][old_x + 2],
                      new_board[old_y + 1][old_x + 2]]
        if new_spaces != [" ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y - 1][old_x] = self._piece[0][0]
        new_board[old_y - 1][old_x + 1] = self._piece[0][1]
        new_board[old_y - 1][old_x + 2] = self._piece[0][2]
        new_board[old_y][old_x] = self._piece[1][0]
        new_board[old_y][old_x + 1] = self._piece[1][1]
        new_board[old_y][old_x + 2] = self._piece[1][2]
        new_board[old_y + 1][old_x] = self._piece[2][0]
        new_board[old_y + 1][old_x + 1] = self._piece[2][1]
        new_board[old_y + 1][old_x + 2] = self._piece[2][2]
        new_board[old_y - 1][old_x - 1] = " "
        new_board[old_y][old_x - 1] = " "
        new_board[old_y + 1][old_x - 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.right(new_board, old_x + 1, old_y, move_spaces - 1)

    def down_left(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece down and to the
        left. Returns the new game board if the move was valid. Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y][old_x - 2],
                      new_board[old_y + 1][old_x - 2],
                      new_board[old_y + 2][old_x - 2],
                      new_board[old_y + 2][old_x - 1],
                      new_board[old_y + 2][old_x]]
        if new_spaces != [" ", " ", " ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y][old_x - 2] = self._piece[0][0]
        new_board[old_y][old_x - 1] = self._piece[0][1]
        new_board[old_y][old_x] = self._piece[0][2]
        new_board[old_y + 1][old_x - 2] = self._piece[1][0]
        new_board[old_y + 1][old_x - 1] = self._piece[1][1]
        new_board[old_y + 1][old_x] = self._piece[1][2]
        new_board[old_y + 2][old_x - 2] = self._piece[2][0]
        new_board[old_y + 2][old_x - 1] = self._piece[2][1]
        new_board[old_y + 2][old_x] = self._piece[2][2]
        new_board[old_y - 1][old_x - 1] = " "
        new_board[old_y - 1][old_x] = " "
        new_board[old_y - 1][old_x + 1] = " "
        new_board[old_y][old_x + 1] = " "
        new_board[old_y + 1][old_x + 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.down_left(new_board, old_x - 1, old_y + 1, move_spaces - 1)

    def down(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center.  Moves the game piece down. Returns the
        new game board if the move was valid.  Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y + 2][old_x - 1],
                      new_board[old_y + 2][old_x],
                      new_board[old_y + 2][old_x + 1]]
        if new_spaces != [" ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y][old_x - 1] = self._piece[0][0]
        new_board[old_y][old_x] = self._piece[0][1]
        new_board[old_y][old_x + 1] = self._piece[0][2]
        new_board[old_y + 1][old_x - 1] = self._piece[1][0]
        new_board[old_y + 1][old_x] = self._piece[1][1]
        new_board[old_y + 1][old_x + 1] = self._piece[1][2]
        new_board[old_y + 2][old_x - 1] = self._piece[2][0]
        new_board[old_y + 2][old_x] = self._piece[2][1]
        new_board[old_y + 2][old_x + 1] = self._piece[2][2]
        new_board[old_y - 1][old_x - 1] = " "
        new_board[old_y - 1][old_x] = " "
        new_board[old_y - 1][old_x + 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.down(new_board, old_x, old_y + 1, move_spaces - 1)

    def down_right(self, new_board, old_x, old_y, move_spaces):
        """
        A recursive function that takes as parameters a copy of the game board and
        the coordinates of the piece center. Moves the game piece down and to the right.
        Returns the new game board if the move was valid. Otherwise returns False.
        """
        # Check if a stone blocks the move. Returns False if the piece
        # encounters a stone before the end of the move.
        new_spaces = [new_board[old_y][old_x + 2],
                      new_board[old_y + 1][old_x + 2],
                      new_board[old_y + 2][old_x + 2],
                      new_board[old_y + 2][old_x - 1],
                      new_board[old_y + 2][old_x]]
        if new_spaces != [" ", " ", " ", " ", " "]:
            if move_spaces > 1:
                return False

        ggame = GessGame()
        new_board[old_y][old_x] = self._piece[0][0]
        new_board[old_y][old_x + 1] = self._piece[0][1]
        new_board[old_y][old_x + 2] = self._piece[0][2]
        new_board[old_y + 1][old_x] = self._piece[1][0]
        new_board[old_y + 1][old_x + 1] = self._piece[1][1]
        new_board[old_y + 1][old_x + 2] = self._piece[1][2]
        new_board[old_y + 2][old_x] = self._piece[2][0]
        new_board[old_y + 2][old_x + 1] = self._piece[2][1]
        new_board[old_y + 2][old_x + 2] = self._piece[2][2]
        new_board[old_y - 1][old_x - 1] = " "
        new_board[old_y - 1][old_x] = " "
        new_board[old_y - 1][old_x + 1] = " "
        new_board[old_y][old_x - 1] = " "
        new_board[old_y + 1][old_x - 1] = " "

        # Remove any stones on the edges of the board.
        for index in range(0, 20):
            new_board[0][index] = " "
            new_board[19][index] = " "
            new_board[index][0] = " "
            new_board[index][19] = " "

        # Check if the move will leave the current player without a ring.
        if self._player == "x" and not ggame.check_ring(new_board)[0]:
            return False

        if self._player == "o" and not ggame.check_ring(new_board)[1]:
            return False

        if move_spaces == 1:
            return new_board

        else:
            return self.down_right(new_board, old_x + 1, old_y + 1, move_spaces - 1)


class GamePiece:
    """
    The GamePiece class represents a game piece. Has methods to determine a 3x3 game
    piece, if the game piece is valid, if the game piece is limited to moving three
    spaces, and in which directions the game piece can move. Communicates with the
    GessGame class to determine a valid game piece and move.
    """

    def __init__(self, board, player, center_x, center_y):
        """
        Takes as parameters the current board and player from the GessGame class, and
        the coordinates that represent the center of the player's game piece.
        """

        self._board = board
        self._player_turn = player
        self._center_x = center_x
        self._center_y = center_y

    def playing_piece(self):
        """ Defines and returns a 3x3 playing piece. """
        # Define the piece.
        center = self._board[self._center_y][self._center_x]
        up_left = self._board[self._center_y - 1][self._center_x - 1]
        up = self._board[self._center_y - 1][self._center_x]
        up_right = self._board[self._center_y - 1][self._center_x + 1]
        left = self._board[self._center_y][self._center_x - 1]
        right = self._board[self._center_y][self._center_x + 1]
        down_left = self._board[self._center_y + 1][self._center_x - 1]
        down = self._board[self._center_y + 1][self._center_x]
        down_right = self._board[self._center_y + 1][self._center_x + 1]

        piece = [[up_left, up, up_right],
                 [left, center, right],
                 [down_left, down, down_right]]

        return piece

    def valid_piece(self):
        """
        Returns True if the game piece is valid.  Otherwise returns False.
        """
        # Initialize a Boolean value to keep track if the piece has at least
        # one square owned by the current player.
        player_stone = False
        piece = self.playing_piece()

        for row in piece:
            for column in row:

                if column == self._player_turn:
                    # At least one square is owned by current player.
                    player_stone = True

                # Return False if the piece contains a square owned
                # by the opposing player.
                if column != self._player_turn and column != " ":
                    return False

        # Return False if the piece does not contain at least one square
        # owned by the current player
        if not player_stone:
            return False

        return True

    def move_three(self):
        """
        Returns True if move is limited to three squares. Returns False for any distance.
        """
        if self._board[self._center_y][self._center_x] == " ":
            return True
        else:
            return False

    def move_up_left(self):
        """
        Returns True for valid move up and to the left. Otherwise returns False.
        """
        if self._board[self._center_y - 1][self._center_x - 1] == self._player_turn:
            return True
        else:
            return False

    def move_up(self):
        """
        Returns True for valid move up. Otherwise returns False.
        """
        if self._board[self._center_y - 1][self._center_x] == self._player_turn:
            return True
        else:
            return False

    def move_up_right(self):
        """
        Returns True for valid move up and to the right. Otherwise returns False.
        """
        if self._board[self._center_y - 1][self._center_x + 1] == self._player_turn:
            return True
        else:
            return False

    def move_left(self):
        """
        Returns True for valid move to the left. Otherwise returns False.
        """
        if self._board[self._center_y][self._center_x - 1] == self._player_turn:
            return True
        else:
            return False

    def move_right(self):
        """
        Returns True for valid move to the right. Otherwise returns False.
        """
        if self._board[self._center_y][self._center_x + 1] == self._player_turn:
            return True
        else:
            return False

    def move_down_left(self):
        """
        Returns True for valid move down and to the left. Otherwise returns False.
        """
        if self._board[self._center_y + 1][self._center_x - 1] == self._player_turn:
            return True
        else:
            return False

    def move_down(self):
        """
        Returns True for valid move down. Otherwise returns False.
        """
        if self._board[self._center_y + 1][self._center_x] == self._player_turn:
            return True
        else:
            return False

    def move_down_right(self):
        """
        Returns True for valid move down and to the right. Otherwise returns False.
        """
        if self._board[self._center_y + 1][self._center_x + 1] == self._player_turn:
            return True
        else:
            return False


gg = GessGame()
gg.pygame_board(gg.get_board())
