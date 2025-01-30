import pygame

class FontRenderer:
    def __init__(self):
        self.color = (255,255,0)
        self.size = 30
        self.font = pygame.font.Font("DIN_bold.ttf",self.size)


    def renderFont(self,window,score,texte):
        text = self.font.render("Score: " + str(score) + texte,True,self.color)
        window.blit(text,(0,0))
