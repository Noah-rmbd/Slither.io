import pygame
import math
from Snake import Snake
from Segment import Segment

class Player(Snake):
    def __init__(self,x,y,w,h,filePath, winDims):
        super().__init__(x,y,w,h,filePath)
        self.winDims = winDims
        self.direction_angle = 0
        self.turn_speed = 10

    def update(self, orbs, snakes):
        self.calculateDirection()
        return super().update(snakes)

    def calculateDirection(self):
        #mousePos = pygame.mouse.get_pos()

        #worldPos = (mousePos[0] - self.winDims[0] / 2 + self.rect.x, mousePos[1] - self.winDims[1] / 2 + self.rect.y)
        (x, y) = pygame.mouse.get_pos()
        print((x,y))

        self.stick_direction = math.atan2(y - self.winDims[1]/2, x - self.winDims[0]/2)

        # Calculer la différence entre l'angle actuel et l'angle cible
        angle_diff = (self.stick_direction - self.direction_angle) % (2 * math.pi)

        # Ajuster l'angle progressivement (braquage limité)
        if angle_diff > math.pi:  # Si l'angle_diff dépasse π, tourner dans l'autre sens
            angle_diff -= 2 * math.pi
        if abs(angle_diff) > self.turn_speed * math.pi / 180:  # Limiter l'ajustement de l'angle à chaque frame
            self.direction_angle += self.turn_speed * math.pi / 180 * math.copysign(1, angle_diff)  # Ajuster l'angle par incréments
        else:
            self.direction_angle = self.stick_direction  # Si la différence est petite, on aligne directement l'angle

        self.direction = (math.cos(self.direction_angle), math.sin(self.direction_angle))
