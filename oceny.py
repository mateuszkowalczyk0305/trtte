from enemy import Enemy
from random import randint
import pygame

class Dwojka(Enemy):
    def __init__(self, dwojka_surface1, dwojka_surface2):
        super().__init__(dwojka_surface1, dwojka_surface2)
        pass

class Trojka(Enemy):
    def __init__(self, trojka_surface1, trojka_surface2):
        super().__init__(trojka_surface1, trojka_surface2)
        pass

class Czworka(Enemy):
    def __init__(self, czworka_surface1, czworka_surface2):
        super().__init__(czworka_surface1, czworka_surface2)
        pass

class Piatka(Enemy):
    def __init__(self, piatka_surface1, piatka_surface2):
        super().__init__(piatka_surface1, piatka_surface2)
        pass

class Wejsciowka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        wejsciowka_surface1 = pygame.image.load("tekstury/postacie/wejsciowka.png").convert_alpha()
        wejsciowka_surface2 = pygame.image.load("tekstury/postacie/wejsciowka2.png").convert_alpha()
        self.frames = [wejsciowka_surface1, wejsciowka_surface2]
        y_pos = (randint(430, 600))
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