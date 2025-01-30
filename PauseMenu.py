import pygame
import sys


class PauseMenu:
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

        # List of buttons
        resume_button = pygame.Rect((self.winDims[0]-200)/2, 350, 200, 50)
        restart_button = pygame.Rect((self.winDims[0]-200)/2, 450, 200, 50)
        quit_button = pygame.Rect((self.winDims[0]-200)/2, 550, 200, 50)

        self.resume = False  # if the user wants to resume
        self.restart = False  # if the user wants to restart the game
        self.quit = False

        while not self.resume and not self.restart and not self.quit:
            self.window.fill(BGCOLOR)
            self.draw_text("Pause", font, GREEN, (self.winDims[0]-100)/2, 100)

            # Show the buttons
            pygame.draw.rect(self.window, BGREEN, resume_button)
            self.draw_text("Resume", font, WHITE, (self.winDims[0]-130)/2, resume_button.y + 10)

            pygame.draw.rect(self.window, TFCOLOR, restart_button)
            self.draw_text("Restart", font, WHITE, (self.winDims[0]-115)/2, restart_button.y + 10)

            pygame.draw.rect(self.window, TFCOLOR, quit_button)
            self.draw_text("Home", font, WHITE, (self.winDims[0]-90)/2, quit_button.y + 10)

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # When user clicks on resume button
                    if resume_button.collidepoint(event.pos):
                        self.resume = True
                    # When user clicks on restart button
                    if restart_button.collidepoint(event.pos):
                        self.restart = True
                    # When user clicks on quit button
                    if quit_button.collidepoint(event.pos):
                        self.quit = True


            pygame.display.flip()

    def draw_text(self, text, font, color, x, y):
        """Affiche un texte à l'écran."""
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

