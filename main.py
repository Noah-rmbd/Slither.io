from MainGame import MainGame
from StartMenu import StartMenu
import pygame

pygame.init()
winDims = (1000, 700)
window = pygame.display.set_mode(winDims)

start_menu = StartMenu(window, winDims)
user_name = start_menu.user_name
game = MainGame(window, winDims, user_name)
game.init()

# Loop to restart the game when you loose
while (game.quit and game.refresh) or game.home:
    if game.home:
        start_menu = StartMenu(window, winDims)
        user_name = start_menu.user_name
    game = MainGame(window, winDims, user_name)
    game.init()
