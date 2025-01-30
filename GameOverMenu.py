import pygame
import sys


class GameOverMenu:
    def __init__(self, window, win_dims):
        self.window = window
        self.winDims = win_dims

        # Colors
        WHITE = (255, 255, 255)
        BGCOLOR = (17, 22, 25)
        TFCOLOR = (60, 50, 105)
        GREEN = (100, 240, 130)
        BGREEN = (70, 160, 110)

        # Fonts
        font = pygame.font.Font(None, 50)

        # Play button
        play_button = pygame.Rect((self.winDims[0]-200)/2, 350, 200, 50)
        self.play_again = False
        # Quit button
        quit_button = pygame.Rect((self.winDims[0]-200)/2, 450, 200, 50)
        self.quit = False

        while not self.play_again and not self.quit:
            self.window.fill(BGCOLOR)
            self.draw_text("You loose", font, GREEN, (self.winDims[0]-160)/2, 100)

            # Show buttons
            pygame.draw.rect(self.window, BGREEN, play_button)
            self.draw_text("Play", font, WHITE, (self.winDims[0]-70)/2, play_button.y + 10)

            pygame.draw.rect(self.window, TFCOLOR, quit_button)
            self.draw_text("Home", font, WHITE, (self.winDims[0]-90)/2, quit_button.y + 10)

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # When user clicks on play again
                    if play_button.collidepoint(event.pos):
                        self.play_again = True
                    # When user clicks on home button
                    if quit_button.collidepoint(event.pos):
                        self.quit = True

            pygame.display.flip()

    def draw_text(self, text, font, color, x, y):
        """Affiche un texte à l'écran."""
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

