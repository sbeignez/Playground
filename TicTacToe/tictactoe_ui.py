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

    COLOR_O = (63, 200, 243)
    COLOR_O_SHADOW = (36, 126, 158)
    COLOR_X = (255, 95, 95)
    COLOR_X_SHADOW = (180, 70, 70)



    def __init__(self, theme="default"):

        # self.game = game

        self.theme = theme

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


    def draw_ui(self, game, state):

        # Erase
        self.erase_ui()

        # Draw UI elements
        self.draw_board(theme=self.theme)
        self.draw_pieces(game, theme=self.theme)
        self.draw_score(game)

        # self.get_keyboard_events()
        # Update Diplay
        pygame.display.update()


    def erase_ui(self):
        pygame.display.get_surface().fill(self.COLOR_BOARD)


    def draw_board(self, theme="default"):
        # draw board
        if not theme == "default":
            size_x_px, size_y_px = UI.SCALE * self.cols, UI.SCALE * self.rows
            try:
                image_board = pygame.image.load(f"TicTacToe/img/board-{theme}.png")
                image_board = pygame.transform.scale(image_board, (size_x_px, size_y_px))
                self.window.blit(image_board, (0,0))
            except:
                pass
        # draw cells
        for r in range(self.rows):
            for c in range(self.cols):
                even = ((r + c) % 2) == 0 
                self.draw_cell(c, r, even, theme)


    def draw_cell(self, x, y, even, theme):
        if theme == "default":
            color = self.COLOR_CELL_EVEN if even else self.COLOR_CELL_ODD
            pygame.draw.rect(self.window, color, pygame.Rect(x * UI.SCALE, y * UI.SCALE, UI.SCALE, UI.SCALE))
            pygame.draw.rect(self.window, self.COLOR_CELL_BORDER, pygame.Rect(x * UI.SCALE, y * UI.SCALE, UI.SCALE, UI.SCALE),1)
        else:
            try:
                cell = "even" if even else "odd"
                image = pygame.image.load(f"TicTacToe/img/cell-{theme}-{cell}.png")
                image = pygame.image.scale(image, (UI.SCALE, UI.SCALE))
                self.draw_cell_image(x,y,image)
            except:
                pass


    def draw_cell_image(self, x, y, image):
        self.window.blit(image, (x * UI.SCALE, y * UI.SCALE,))

    def draw_pieces(self, game, theme="default"):
        for r in range(self.rows):
            for c in range(self.cols):
                if game.board[r][c] == 'O':
                    self.draw_O(c, r, theme)
                elif game.board[r][c] == 'X':
                    self.draw_X(c, r, theme)

    def draw_O(self, x, y, theme):

        if self.theme == "default":
            size_px, offset = (UI.SCALE) * 0.8, 3
            x_center_px, y_center_px, radius_px = x * UI.SCALE + UI.SCALE / 2, y * UI.SCALE + UI.SCALE / 2, size_px / 2
            pygame.draw.circle(self.window, self.COLOR_O_SHADOW, (x_center_px -offset , y_center_px + offset ), radius_px, int(radius_px/2))
            pygame.draw.circle(self.window, self.COLOR_O, (x_center_px, y_center_px), radius_px, int(radius_px/2)) 
        else:
            x_corner_px, y_corner_px = x * UI.SCALE , y * UI.SCALE
            O = pygame.image.load(f'TicTacToe/img/O-{theme}.png')
            O = pygame.transform.scale(O, (UI.SCALE, UI.SCALE))
            O = O.convert_alpha()
            self.window.blit(O, (x_corner_px, y_corner_px))


    def draw_X(self, x, y, theme):
        if self.theme == "default":
            size_px = (UI.SCALE) * 0.8
            offset = 3
            x_corner_px, y_corner_px = x * UI.SCALE + (UI.SCALE - size_px) / 2, y * UI.SCALE + (UI.SCALE - size_px) / 2
            pygame.draw.rect(self.window, self.COLOR_X, pygame.Rect(x_corner_px -offset, y_corner_px +offset, size_px, size_px), int(size_px/4)) 
            pygame.draw.rect(self.window, self.COLOR_X_SHADOW, pygame.Rect(x_corner_px, y_corner_px, size_px, size_px), int(size_px/4))      
        else:
            x_corner_px, y_corner_px = x * UI.SCALE , y * UI.SCALE
            X = pygame.image.load(f'TicTacToe/img/X-{theme}.png')
            X = pygame.transform.scale(X, (UI.SCALE, UI.SCALE))
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