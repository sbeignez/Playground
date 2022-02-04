from math import floor
import pygame
import pygame.gfxdraw

class UI():

    # UI DEFAULTS
    SCALE = 100

    # WINDOW SCORE
    WINDOW_SCORE_W = 300
    FONT_SIZE = 18
    PADDING = 5

    # UI COLORS
    COLOR_BOARD = (40, 40, 44)
    COLOR_CELL_BORDER = (40, 40, 44)
    COLOR_CELL_EVEN = (30, 30, 34)
    COLOR_CELL_ODD = (36, 36, 40)
    COLOR_SCORE = (200, 200, 200)

    COLOR_O = (200, 200, 200)
    COLOR_O_BORDER = (250, 250, 250)
    COLOR_X = (150, 150, 150)
    COLOR_X_BORDER = (250, 250, 250)



    def __init__(self):

        # self.game = game

        self.style = ["flat", "img"][0]

        self.rows = 3
        self.cols = 3

        self.window_x_px = self.cols * UI.SCALE + self.WINDOW_SCORE_W
        self.window_y_px = self.rows * UI.SCALE

        pygame.init()
        pygame.display.set_caption('Tic Tac Toe AI 2022')
        self.window = pygame.display.set_mode( (self.window_x_px , self.window_y_px) )
        
        self.erase_ui()
        pygame.display.update()
        
        # keys = [pygame.KEYDOWN, pygame.QUIT]
        # pygame.event.set_blocked(None)
        # pygame.event.set_allowed(keys)
        pygame.event.get()
        self.action_key = None


    def draw_ui(self, game):

        # Erase
        self.erase_ui()

        # Draw UI elements
        self.draw_board()
        self.draw_pieces(game)
        self.draw_score(game)

        # self.get_keyboard_events()
        # Update Diplay
        pygame.display.update()

    def erase_ui(self):
        pygame.display.get_surface().fill(self.COLOR_BOARD)

    def draw_board(self):
        image_odd = pygame.image.load('TicTacToe/img/wood_1.jpeg')
        image_odd = pygame.transform.scale(image_odd, (100, 100))
        image_even = pygame.image.load('TicTacToe/img/wood_2.jpeg')
        image_even = pygame.transform.scale(image_even, (100, 100))

        for r in range(self.rows):
            for c in range(self.cols):
                color = self.COLOR_CELL_EVEN if ((r + c) % 2) == 0 else self.COLOR_CELL_ODD
                self.draw_cell(c, r, color)

                if self.style == "img":
                    image = image_even if ((r + c) % 2) == 0 else image_odd
                    self.draw_cell_image(c, r, image)



    def draw_cell(self, x, y, color):
        pygame.draw.rect(self.window, color, pygame.Rect(x * UI.SCALE, y * UI.SCALE, UI.SCALE, UI.SCALE))
        pygame.draw.rect(self.window, self.COLOR_CELL_BORDER, pygame.Rect(x * UI.SCALE, y * UI.SCALE, UI.SCALE, UI.SCALE),1)


    def draw_cell_image(self, x, y, image):
        self.window.blit(image, (x * UI.SCALE, y * UI.SCALE,))

    def draw_pieces(self, game):
        for r in range(self.rows):
            for c in range(self.cols):
                if game.board[r][c] == 'O':
                    self.draw_O(c, r)
                elif game.board[r][c] == 'X':
                    self.draw_X(c, r)

    def draw_O(self, x, y, style="flat"):

        if self.style == "default":
            x_center_px, y_center_px, radius_px = x * UI.SCALE + UI.SCALE / 2, y * UI.SCALE + UI.SCALE / 2, (UI.SCALE / 2) * 0.8
            pygame.draw.circle(self.window, self.COLOR_O, (x_center_px, y_center_px), radius_px, 0)
            pygame.draw.circle(self.window, self.COLOR_O_BORDER, (x_center_px, y_center_px), radius_px, 1)
        elif self.style == "flat":
            size_px = (UI.SCALE) * 0.8
            x_corner_px, y_corner_px = x * UI.SCALE + (UI.SCALE - size_px) / 2, y * UI.SCALE + (UI.SCALE - size_px) / 2
            O = pygame.image.load('TicTacToe/img/O.png')
            O = pygame.transform.scale(O, (size_px, size_px))
            O = O.convert_alpha()
            self.window.blit(O, (x_corner_px, y_corner_px))


    def draw_X(self, x, y):
        size_px = (UI.SCALE) * 0.8
        x_corner_px, y_corner_px = x * UI.SCALE + (UI.SCALE - size_px) / 2, y * UI.SCALE + (UI.SCALE - size_px) / 2
        pygame.draw.rect(self.window, self.COLOR_X, pygame.Rect(x_corner_px, y_corner_px, size_px, size_px), 0)
        pygame.draw.rect(self.window, self.COLOR_X_BORDER, pygame.Rect(x_corner_px, y_corner_px, size_px, size_px),1)

        X = pygame.image.load('TicTacToe/img/X.png')
        X = pygame.transform.scale(X, (size_px, size_px))
        X = X.convert_alpha()
        self.window.blit(X, (x_corner_px, y_corner_px))

    def draw_score(self, game):
        font = pygame.font.SysFont('Courier', self.FONT_SIZE, bold=True)

        texts = [
            "TIC TAC TOE",
            f"PLAYER: {game.player[0]} {game.player[1].name}",
        ]

        for line_number, text in enumerate(texts):
            self.window.blit(font.render(text, True, self.COLOR_SCORE), (self.cols * UI.SCALE + self.PADDING, self.PADDING + 25 * line_number))


    def get_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pass
            if event.type == pygame.KEYDOWN:
                # DELETE: Restart game
                if event.key == pygame.K_DELETE:
                    print("Restart()")
                    pass
                # TAB: PRINT INFO
                if event.key == pygame.K_TAB:
                    print("Infos")

                # ENTER: Select cell
                if event.key == pygame.K_RETURN:
                    pass

                # USER ACTION
                if event.key == pygame.K_LEFT:
                    pass    
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x_px, y_px = pygame.mouse.get_pos()
                    return 'cell', (x_px, y_px)
                return None, None

        return None, None
                

    def get_cell(self):
        type, value = self.get_events()
        if type == 'cell':
            x_px, y_px = value
            col = floor(x_px / UI.SCALE)
            row = floor(y_px / UI.SCALE)
            return row, col
        return None, None


if __name__ == '__main__':
    pass