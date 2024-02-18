import pygame

class Gracz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        gracz_walk_1 = pygame.image.load("tekstury/postacie/gracz1walk.png").convert_alpha()
        gracz_walk_2 = pygame.image.load("tekstury/postacie/gracz2walk.png").convert_alpha()

        self.gracz_walk = [gracz_walk_1, gracz_walk_2]
        self.gracz_index = 0
        self.image = self.gracz_walk[self.gracz_index]
        self.rect = self.image.get_rect(midbottom = (120,600))
        self.grawitacja = 0
        self.gracz_jump = pygame.image.load("tekstury/postacie/graczjump.png").convert_alpha()
        self.muza_jump = pygame.mixer.Sound("music/skok.mp3")
        self.predkosc = 5


    def gracz_input(self):
        klaw = pygame.key.get_pressed()
        if klaw[pygame.K_SPACE] and self.rect.bottom >= 450:
            self.grawitacja = -30
            self.muza_jump.play()
        if klaw[pygame.K_LEFT]:
            self.rect.x -= self.predkosc
        if klaw[pygame.K_RIGHT]:
            self.rect.x += self.predkosc

    def add_grawitacja(self):
        self.grawitacja += 1
        self.rect.y += self.grawitacja
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def animacja(self):
        if self.rect.bottom < 600:
            self.image = self.gracz_jump
        else:
            self.gracz_index += 0.1
            if self.gracz_index >= len(self.gracz_walk): self.gracz_index = 0
            self.image = self.gracz_walk[int(self.gracz_index)]
        # chodzenie, gdy gracz na ziemii
        # skakanie, gdy nie na ziemii
    def update(self):
        self.gracz_input()
        self.add_grawitacja()
        self.animacja()