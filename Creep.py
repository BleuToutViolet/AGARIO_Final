Auteur: ROBERT Loïc et DURAISAMY_Arinidan
Contact: loicrobert80 @ gmail.com et arinidan @ hotmail.fr
Dossier Creep pour le dossier DURAISAMY_ROBERT
Version: 0.1

import random
import pygame
from pygame.math import Vector2


class Creep :
    def __init__(self):
        self.rayon = 2
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))


    def mourir (self):
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))


    def draw (self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)