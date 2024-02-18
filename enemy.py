import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surf1, surf2):
        super().__init__()
        self.frames = [surf1, surf2]
        y_pos = (randint(430, 590))
        self.animacja_index = 0
        self.image = self.frames[self.animacja_index]
        self.rect = self.image.get_rect(midbottom = (randint(1250, 1600), y_pos))

    def animacja(self):
        self.animacja_index += 0.1
        if self.animacja_index >= len(self.frames): self.animacja_index = 0
        self.image = self.frames[int(self.animacja_index)]

    def zniszczenie(self):
        if self.rect.x <= -200:
            self.kill()

    def update(self):
        self.animacja()
        self.rect.x -= 5
        self.zniszczenie()