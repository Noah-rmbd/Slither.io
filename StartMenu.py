import pygame
import sys


class StartMenu:
    def __init__(self, window, win_dims):
        self.window = window
        self.winDims = win_dims

        # Colors
        WHITE = (255, 255, 255)
        GRAY = (200, 200, 200)
        BGCOLOR = (17, 22, 25)
        TFCOLOR = (60, 50, 105)
        GREEN = (100, 240, 130)
        BGREEN = (70, 160, 110)

        # Fonts
        font = pygame.font.Font(None, 50)
        input_font = pygame.font.Font(None, 40)

        # Text field
        input_box = pygame.Rect((self.winDims[0]-200)/2, 350, 200, 50)
        self.user_name = ""
        active = False

        # Play button
        play_button = pygame.Rect((self.winDims[0]-200)/2, 450, 200, 50)
        self.game_running = False  # Pour savoir si le jeu est lancé

        while not self.game_running:
            self.window.fill(BGCOLOR)
            self.draw_text("Slither.py", font, GREEN, (self.winDims[0]-160)/2, 100)

            # Dessiner le champ de texte
            pygame.draw.rect(self.window, GRAY if active else TFCOLOR, input_box)
            self.draw_text(self.user_name, input_font, WHITE, input_box.x + 10, input_box.y + 10)

            # Dessiner le bouton "Jouer"
            pygame.draw.rect(self.window, BGREEN, play_button)
            self.draw_text("Jouer", font, WHITE, (self.winDims[0]-100)/2, play_button.y + 10)

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifier si on clique dans le champ de texte
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                    # Vérifier si on clique sur le bouton "Jouer"
                    if play_button.collidepoint(event.pos) and self.user_name.strip():
                        self.game_running = True

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            self.game_running = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.user_name = self.user_name[:-1]
                        else:
                            if len(self.user_name)<11:
                                self.user_name += event.unicode  # Ajouter la lettre tapée

            pygame.display.flip()

    def draw_text(self, text, font, color, x, y):
        """Affiche un texte à l'écran."""
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

