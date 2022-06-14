Auteur : ROBERT Loïc et DURAISAMY_Arinidan
Contact : loicrobert80@gmail.com    arinidan@hotmail.fr
Dossier Joueur pour DURAISAMY_ROBERT
Version : 0.1


import random
import pygame
from pygame.math import Vector2

import core


class Joueur :
    def __init__(self):
        self.rayon = 30
        self.couleur = (255, 255, 255)
        self.position = Vector2(random.randint(0,1200), random.randint(0, 800))
        self.mass = 20
        self.nom = "Bleu"
        self.vitesse = 5
        self.direction = Vector2()
        self.vitesseMax = 3
        self.vivant = True


        self.L = Vector2(0, 0)
        self.l = 0
        self.lo = 10
        self.Ux = 0
        self.Fx = 0



    def mourir (self):
        self.direction = Vector2()
        self.vivant = False

    def deplacer (self,clique):
        core.WINDOW_SIZE = [1200, 800]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.position = Vector2(1200,0)
        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.position = Vector2(0,800)

        if clique is not None:
            self.Ux = Vector2(clique) - self.position
            self.l= self.Ux.length()
            self.Ux= self.Ux.normalize()
            self.L= abs(self.l - self.lo)
            self.Fx= 0.0003 * self.L * self.Ux
            self.direction= self.direction + self.Fx
        if self.vivant :
            self.position = self.position + self.direction

    def grossir (self):
        self.rayon = self.rayon + 0.2

    def limit (self):
        core.WINDOW_SIZE = [1200, 800]

        if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            self.direction, Vector2(self.direction.x, self.direction.y * -1)
            self.rayon = self.rayon/2
            self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))

        if self.position.x < 0 or self.position.x > core.WINDOW_SIZE[0]:
            self.direction, Vector2(self.direction.x * -1, self.direction.y)
            self.rayon = self.rayon/2
            self.position = Vector2(random.randint(0, 1200), random.randint(0, 800))



    def draw (self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)