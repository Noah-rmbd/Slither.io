import pygame
from Player import Player
from Orb import Orb
from Camera import Camera
from AI import AI
from FontRenderer import FontRenderer
from GameOverMenu import GameOverMenu
from PauseMenu import PauseMenu
import random

START_W = 50
START_H = 50

PLAYER_START_X = 0
PLAYER_START_Y = 0
PLAYER_TEXTURE = "textures/body_red.png"

MAX_ORB_SIZE = 40

FPS = 60
NUM_ORBS = 1000
NUM_AI = 60

class MainGame:
    def __init__(self, window, winDims, user_name):

        self.winDims = winDims
        self.window = window
        self.winColor = (75,75,75)

        self.quit = False
        self.pause = False
        self.refresh = False
        self.alive = True
        self.home = False
        self.clock = pygame.time.Clock()
        self.user_name = user_name

        self.camera = Camera(PLAYER_START_X,PLAYER_START_Y,(START_W,START_H), self.winDims)

        self.textures = ["textures/blue_orb.png", "textures/green_orb.png", "textures/purple_orb.png",
                         "textures/red_orb.png", "textures/yellow_orb.png", "textures/orange_orb.png"]

        self.player = Player(PLAYER_START_X,PLAYER_START_Y,START_W,START_H,random.choice(self.textures),self.winDims)
        self.orbs = []
        self.snakes = []
        self.fontRenderer = FontRenderer()

    def init(self):

        for i in range(NUM_ORBS):
            randX = random.randint(-self.winDims[0] * 3,self.winDims[0] * 3)
            randY = random.randint(-self.winDims[1] * 3,self.winDims[1] * 3)
            randR = random.randint(10,MAX_ORB_SIZE)

            randTexture = random.choice(self.textures)

            newOrb = Orb(randX,randY,randR, randTexture)
            self.orbs.append(newOrb)

        self.snakes.append(self.player)

        for i in range(NUM_AI):
            randX = random.randint(-self.winDims[0] * 3,self.winDims[0] * 3)
            randY = random.randint(-self.winDims[1] * 3,self.winDims[1] * 3)

            randTexture = random.choice(self.textures)

            newAI = AI(randX,randY,START_W,START_H,randTexture)
            self.snakes.append(newAI)

        self.play()

    def play(self):
        timer_add_players = 0

        # The game stops when the window is closed
        while self.quit is False:
            # Game loop when anything is right
            while self.pause is False and self.quit is False and self.alive is True:
                self.update()
                self.render()
                timer_add_players += 1

                if timer_add_players > 60:
                    timer_add_players = 0

                    randX = random.randint(-self.winDims[0] * 3, self.winDims[0] * 3)
                    randY = random.randint(-self.winDims[1] * 3, self.winDims[1] * 3)

                    randTexture = random.choice(self.textures)

                    newAI = AI(randX, randY, START_W, START_H, randTexture)
                    self.snakes.append(newAI)

                    for i in range(30):
                        randX = random.randint(-self.winDims[0] * 3, self.winDims[0] * 3)
                        randY = random.randint(-self.winDims[1] * 3, self.winDims[1] * 3)
                        randR = random.randint(10, MAX_ORB_SIZE)

                        randTexture = random.choice(self.textures)

                        newOrb = Orb(randX, randY, randR, randTexture)
                        self.orbs.append(newOrb)
            # When the player dies
            while self.quit is False and self.alive is False:
                game_over_menu = GameOverMenu(self.window, self.winDims)
                if game_over_menu.play_again:
                    self.refresh = True
                    self.quit = True
                elif game_over_menu.quit:
                    self.home = True
                    self.quit = True
                else:
                    self.quit = True

            # When the user pauses the game
            while self.pause is True and self.quit is False:
                pause_menu = PauseMenu(self.window, self.winDims)
                if pause_menu.resume:
                    self.pause = False
                elif pause_menu.restart:
                    self.refresh = True
                    self.quit = True
                else:
                    self.quit = True
                    self.home = True


    def update(self):
        self.clock.tick(FPS)

        # window events processed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            # When the user wants to pause the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.pause = True

        # orb update
        for orb in self.orbs:
            if orb.update(self.snakes):
                self.orbs.remove(orb)

        # snakes update
        for snake in self.snakes:
            if snake.update(self.orbs, self.snakes) == True:
                startX = snake.rect.x
                startY = snake.rect.y
                size = START_W

                randTexture = random.choice(self.textures)

                newOrb = Orb(startX, startY, size, randTexture)
                self.orbs.append(newOrb)

                for segment in snake.segments:
                    startX = segment.rect.x
                    startY = segment.rect.y
                    size = START_W

                    randTexture = random.choice(self.textures)

                    newOrb = Orb(startX, startY, size, randTexture)
                    self.orbs.append(newOrb)

                snake.segments.clear()
                self.snakes.remove(snake)

        # camera update
        self.camera.update(self.player.rect.x,self.player.rect.y)

        # Verify if the player is still alive
        if self.snakes[0] != self.player:
            self.alive = False


    def render(self):
        self.window.fill(self.winColor)
        self.font = pygame.font.Font("DIN_bold.ttf", 30)

        for orb in self.orbs:
            #On n'affiche que les orbes qui sont dans la camera, on ajoute une marge
            if abs(orb.rect.x-self.player.rect.x) <= 510 and abs(orb.rect.y-self.player.rect.y) <= 360:
                orb.draw(self.window, self.camera)


            # On veut render les orb sur une map de taille ((self.windim_x/self.windim_y)*200, 200)
            orb_map_position = (((orb.rect.x+3000)/6000)*286+715, ((orb.rect.y+2100)/4100)*200+500)
            pygame.draw.circle(self.window, (255, 255, 255), orb_map_position, 1)

        #On affiche le joueur sur la map
        player_map_position = (((self.snakes[0].rect.x+3000)/6000)*286+715, ((self.snakes[0].rect.y+2100)/4100)*200+500)
        pygame.draw.circle(self.window, (255, 0, 0), player_map_position, 4)

        for segment in self.snakes[0].segments:
            player_map_position = (((segment.rect.x + 3000) / 6000) * 286 + 715, ((segment.rect.y + 2100) / 4100) * 200 + 500)
            pygame.draw.circle(self.window, (255, 0, 0), player_map_position, 4)


        for snake in self.snakes:
            #On affiche les autres serpents sur la map
            if snake != self.player:
                for segment in snake.segments:
                    player_map_position = (
                    ((segment.rect.x + 3000) / 6000) * 286 + 715, ((segment.rect.y + 2100) / 4100) * 200 + 500)
                    pygame.draw.circle(self.window, (0, 0, 255), player_map_position, 2)

            #On n'affiche que les serpents qui sont dans la camera
            if abs(snake.rect.x-self.player.rect.x) <= 1000 and abs(snake.rect.y-self.player.rect.y) <= 600:
                snake.draw(self.window,self.camera)
                #Show the snakes username
                if snake == self.player:
                    text = self.font.render(self.user_name, True, (240, 240, 240))
                    self.window.blit(text, self.camera.translate(snake.rect.x, snake.rect.y))

                else:
                    text = self.font.render("Bot", True, (255, 255, 255))
                    self.window.blit(text, self.camera.translate(snake.rect.x, snake.rect.y))


        self.fontRenderer.renderFont(self.window, self.player.score, " "+str(self.snakes[0].rect.x)+" "+str(self.snakes[0].rect.y))

        pygame.display.update()
