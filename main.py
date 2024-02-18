# import funkcji exit z modułu sys
from sys import exit
import pygame
from random import randint
from oceny import *
from gracz import *

gracz_mial_kolizje_wejsciowka = False

def kolizja_wejsciowka():
    global game_active
    global top_checked
    global srednia
    global gracz_mial_kolizje_wejsciowka
    if pygame.sprite.spritecollide(gracz.sprite, wejsciowka_group, True): # Argumenty (sprite, group, bool), gdzie bool = True oznacza, że obstacle zniknie po kolizji
        if not gracz_mial_kolizje_wejsciowka:
            gracz_mial_kolizje_wejsciowka = True
            srednia = 3.0
            animacja_smutas()
        else:
            gracz_mial_kolizje_wejsciowka = False
            game_active = False
            top_checked = False




def kolizja_dwojka():
    if pygame.sprite.spritecollide(gracz.sprite, dwojka_group, True):
        return True
    else: return False

def kolizja_trojka():
    global score_sum
    global score_count
    if pygame.sprite.spritecollide(gracz.sprite, trojka_group, True):
        score_sum += 3
        score_count += 1

def kolizja_czworka():
    global score_sum
    global score_count
    if pygame.sprite.spritecollide(gracz.sprite, czworka_group, True):
        score_sum += 4
        score_count += 1

def kolizja_piatka():
    global score_sum
    global score_count
    if pygame.sprite.spritecollide(gracz.sprite, piatka_group, True):
        score_sum += 5
        score_count += 1

def animacja_smutas():
    global tekst
    global tekst_szansa_rectangle
    smutas_frames = [pygame.image.load("tekstury/smutas1.png").convert_alpha(),pygame.image.load("tekstury/smutas.png").convert_alpha()]
    smutas_pozycja = (500,100)
    for frame in smutas_frames:
        okno.blit(frame, smutas_pozycja)
        tekst = pygame.font.Font("tekstury/fonty/Pixeltype.ttf", 50)
        tekst_szansa_surface = tekst_koniec.render('OSTATNIA SZANSA', False, (42, 158, 247))
        tekst_szansa_rectangle = tekst_szansa_surface.get_rect(center=(600, 100))

        # Rysowanie tła napisu
        pygame.draw.rect(okno, (201, 234, 240),tekst_szansa_rectangle)
        okno.blit(tekst_szansa_surface, tekst_szansa_rectangle)
        pygame.display.flip()
        pygame.time.delay(800)


# inicjalizacja zaimportowanych modułów z pygame:

pygame.init()

# okno naszej gry (szerokość, wysokość):

okno = pygame.display.set_mode((1200, 700))

# nazwa okna naszej gry:

pygame.display.set_caption("The Road To The Engineer")

# zmienna do statusu gry:

game_active = True
game_start = True
top_checked = False

najlepsze = []

# Grupy Klas:

gracz = pygame.sprite.GroupSingle()
gracz.add(Gracz())

dwojka_group = pygame.sprite.Group()
wejsciowka_group = pygame.sprite.Group()

trojka_group = pygame.sprite.Group()
czworka_group = pygame.sprite.Group()
piatka_group = pygame.sprite.Group()

# grafiki (.convert() - bardziej optymalny format grafiki):

tlo_surface = pygame.image.load("tekstury/school.png").convert()
ziemia_surface = pygame.image.load("tekstury/ziemia.png").convert()
# tekst:

tekst = pygame.font.Font("tekstury/fonty/Pixeltype.ttf", 50)                     # argumenty: (font type, size)
tekst_stopera = pygame.font.Font("tekstury/fonty/Pixeltype.ttf", 30)             # argumenty: (font type, size)
tekst_score = pygame.font.Font("tekstury/fonty/Pixeltype.ttf", 30)               # argumenty: (font type, size)
tekst_surface = tekst.render('The Road To The Engineer', False, (42, 158, 247))  # argumenty: (string, (wygładzanie krawędzi), kolor)
tekst_rectangle = tekst_surface.get_rect(center = (600, 50))


dwojka_surface1 = pygame.image.load("tekstury/postacie/2.png").convert_alpha()
dwojka_surface2 = pygame.image.load("tekstury/postacie/2.1.png").convert_alpha()
trojka_surface1 = pygame.image.load("tekstury/postacie/3.png").convert_alpha()
trojka_surface2 = pygame.image.load("tekstury/postacie/3.1.png").convert_alpha()
czworka_surface1 = pygame.image.load("tekstury/postacie/4.1.1.png").convert_alpha()
czworka_surface2 = pygame.image.load("tekstury/postacie/4.1.png").convert_alpha()
piatka_surface1 = pygame.image.load("tekstury/postacie/5.png").convert_alpha()
piatka_surface2 = pygame.image.load("tekstury/postacie/5.1.png").convert_alpha()


# Stoper:

stoper = 0
score_sum = 0
score_count = 0
srednia = 0
predkosc_timer = 0

# Muzyczka:

muza_w_tle = pygame.mixer.Sound("music/muza_w_tle.mp3")
muza_w_tle.set_volume(0.1)
muza_w_tle.play(loops = -1)

# User events:

dwojka_stoper = pygame.USEREVENT + 1                 # tworzymy swój własny event w grze
trojka_stoper = pygame.USEREVENT + 2                 # tworzymy swój własny event w grze
czworka_stoper = pygame.USEREVENT + 3                 # tworzymy swój własny event w grze
piatka_stoper = pygame.USEREVENT + 4                 # tworzymy swój własny event w grze
wejsciowka_stoper = pygame.USEREVENT + 5

dwojka_stoper_event = pygame.event.Event(dwojka_stoper)
trojka_stoper_event = pygame.event.Event(trojka_stoper)
czworka_stoper_event = pygame.event.Event(czworka_stoper)
piatka_stoper_event = pygame.event.Event(piatka_stoper)
wejsciowka_stoper_event = pygame.event.Event(wejsciowka_stoper)

pygame.time.set_timer(pygame.event.Event(dwojka_stoper), 4000)
pygame.time.set_timer(pygame.event.Event(trojka_stoper), 1500)  # co 2500 ms event: friends_stoper
pygame.time.set_timer(pygame.event.Event(czworka_stoper), 5000)
pygame.time.set_timer(pygame.event.Event(piatka_stoper), 10000)
pygame.time.set_timer(pygame.event.Event(wejsciowka_stoper), 5000)


# Outro gry:

smutas = pygame.image.load("tekstury/smutas.png").convert_alpha()
smutas1 = pygame.image.load("tekstury/smutas1.png").convert_alpha()

tekst_koniec = pygame.font.Font("tekstury/fonty/Pixeltype.ttf", 120)
tekst_koniec_surface = tekst_koniec.render('Koniec Gry', False, (42, 158, 247))
tekst_koniec_rectangle = tekst_koniec_surface.get_rect(center = (600, 550))

koniec_gry = pygame.image.load("tekstury/postacie/gracz1dead.png").convert_alpha()
koniec_gry_skala = pygame.transform.scale(koniec_gry,(200, 400))                    # argumenty (obraz, szer, wys)
koniec_gry_rectangle = koniec_gry_skala.get_rect(center = (650,300))

gracz_walk_1 = pygame.image.load("tekstury/postacie/gracz1walk.png").convert_alpha()
gracz_rectangle = gracz_walk_1.get_rect(midbottom = (120,600))

gra_nazwa = tekst.render("The Road To The Engineer", False, (42, 158, 247))
gra_nazwa_rectangle = gra_nazwa.get_rect(center = (600,100))

spacja_nazwa = tekst.render("Nacisnij spacje, zeby popykac", False, (42, 158, 247))
spacja_nazwa_rectangle = spacja_nazwa.get_rect(center = (600,500))

gra_mess = tekst.render("SPACJA & GORNA STRZALKA - NOWA GRA", False, ((242, 5, 5)))
gra_mess_rectangle = gra_mess.get_rect(center = (600, 620))

# Główna pętla gry:
game_active = True
while True:

# 60 fps
    dt = pygame.time.Clock().tick(60)
    stoper += dt/1000
    if score_count > 0:
        srednia = score_sum / score_count
    else:
        średnia = 2

    for e in pygame.event.get():
        if e.type == dwojka_stoper: # dwojka_stoper -> user event stworzenia enemy
            dwojka_group.add(Dwojka(dwojka_surface1, dwojka_surface2))
            print("Dwojka")
        elif e.type == trojka_stoper:
            trojka_group.add(Trojka(trojka_surface1, trojka_surface2))
            print("Trojka")
        elif e.type == czworka_stoper:
            czworka_group.add(Czworka(czworka_surface1, czworka_surface2))
        elif e.type == piatka_stoper:
            piatka_group.add(Piatka(piatka_surface1, piatka_surface2))
        elif e.type == wejsciowka_stoper:
            wejsciowka_group.add(Wejsciowka())
        elif e.type == pygame.QUIT:
            pygame.quit()                     # zamknięcie pygame
            exit()     
        else:
            print("anohers:")
            print(e)
        

# game_active = True:

    if game_active:
        if game_start:
            okno.fill((69,147,158))
            pygame.draw.rect(okno, (201, 234, 240), gra_nazwa_rectangle)
            okno.blit(gra_nazwa, gra_nazwa_rectangle)
            pygame.draw.rect(okno, (201, 234, 240), spacja_nazwa_rectangle)
            okno.blit(spacja_nazwa, spacja_nazwa_rectangle)



            klaw = pygame.key.get_pressed()
            if klaw[pygame.K_SPACE]:
                game_start = False
                

        else:
            # Warunki wpisania enemy do tablicy:


            if predkosc_timer > pygame.time.get_ticks():  # Sprawdź czy minął określony czas
                gracz.predkosc = 5


            okno.blit(tlo_surface, (0, 0))
            okno.blit(ziemia_surface, (0, 600))
            pygame.draw.rect(okno, (201, 234, 240), tekst_rectangle)
            okno.blit(tekst_surface, tekst_rectangle)
            #print(score)

            # Gracz:

            gracz.draw(okno)
            gracz.update()

            # Enemy:

            dwojka_group.draw(okno)
            dwojka_group.update()

            trojka_group.draw(okno)
            trojka_group.update()

            czworka_group.draw(okno)
            czworka_group.update()

            piatka_group.draw(okno)
            piatka_group.update()

            wejsciowka_group.draw(okno)
            wejsciowka_group.update()

            # Kolizje:
            if kolizja_dwojka():
                game_active = False
                top_checked = False

            for trojka in trojka_group:
                kolizja_trojka()

            for czworka in czworka_group:
                kolizja_czworka()

            for piatka in piatka_group:
                kolizja_piatka()

            for wejsciowka in wejsciowka_group:
                kolizja_wejsciowka()

            # Stoper:

            stoper_surface = tekst_stopera.render(('Czas: %d sek.' % int(stoper)), False, (42, 158, 247))
            stoper_rectangle = stoper_surface.get_rect(topleft=(50, 5))
            pygame.draw.rect(okno, (201, 234, 240), stoper_rectangle)
            okno.blit(stoper_surface, stoper_rectangle)

            # Średnia:

            srednia_surface = tekst_score.render(("Srednia: %.2f" % float(srednia)), False, (42, 158, 247))
            srednia_rectangle = srednia_surface.get_rect(topright=(1150, 5))
            pygame.draw.rect(okno, (201, 234, 240), srednia_rectangle)
            okno.blit(srednia_surface, srednia_rectangle)

# game_active = False:

    else:
        
        if not top_checked: #sprawdzamy jednorazowo
            top_checked = True
            file = open('highscores.txt','a') # otwieramy plik w trybie append
            file.write("{:.2f}\n".format(round(srednia, 2))) # wpis
            file.close() #zamykamy

            file = open('highscores.txt','r') #otwieramy w trybie read


            lines = file.readlines()
            lines.sort(key=lambda x: x, reverse=True) # sortujemy tablice (lambda niepotrzebna, ale nwm jak inaczej[przy jednej kolumnie dziala]), reverse najwyzszy da na góre
            
            najlepsze = lines[:5]
            file.close()



        okno.fill((56, 54, 55))
        okno.blit(koniec_gry_skala, koniec_gry_rectangle)

        gracz_rectangle.midbottom = (120, 600)

        pygame.draw.rect(okno, (201, 234, 240), tekst_koniec_rectangle)
        okno.blit(tekst_koniec_surface, tekst_koniec_rectangle)

        pygame.draw.rect(okno, (201, 234, 240), gra_nazwa_rectangle )
        okno.blit(gra_nazwa, gra_nazwa_rectangle)

        pygame.draw.rect(okno, (201, 234, 240), gra_mess_rectangle)
        okno.blit(gra_mess, gra_mess_rectangle)

        srednia_surface = tekst_score.render(("Twoja Srednia: %.2f" % float(srednia)), False, (42, 158, 247))
        srednia_rectangle = srednia_surface.get_rect(center=(600, 30))


        top_srednia_surf = tekst_score.render(("Najlepsze wyniki:"), False, (42, 158, 247))
        top_srednia_rect = top_srednia_surf.get_rect(center=(100, 70))
        pygame.draw.rect(okno, (201, 234, 240), top_srednia_rect)
        okno.blit(top_srednia_surf, top_srednia_rect)


        for i in range(5):
            top_srednia_surf = tekst_score.render((najlepsze[i].strip("\n")), False, (42, 158, 247))
            top_srednia_rect = top_srednia_surf.get_rect(center=(100, 100+i*30)) # w odstępach co 30px
            pygame.draw.rect(okno, (201, 234, 240), top_srednia_rect)
            okno.blit(top_srednia_surf, top_srednia_rect)


        pygame.draw.rect(okno, (201, 234, 240), srednia_rectangle)
        okno.blit(srednia_surface, srednia_rectangle)
        

        klaw = pygame.key.get_pressed()
        if klaw[pygame.K_SPACE] and klaw[pygame.K_UP]:
            game_active = True
            game_start = False
            stoper = 0
            score = 0
            srednia = 0
            pygame.event.clear()
    pygame.display.update()

################################################################################################################################################################################################
# korzystałem z następujących pomocy:
# YouTube tutorial PL version: https://www.youtube.com/playlist?list=PLUOJeouuYOXEcIGa-g6m3islVTD5WWcOL
# YouTube tutorial ENG version: https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=2532s
# Dokumentacja pygame: pygame.org
# Forum dyskusyjne: stackoverflow.com
################################################################################################################################################################################################

