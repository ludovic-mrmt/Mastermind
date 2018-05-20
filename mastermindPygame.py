import pygame
from pygame.locals import *
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

fond = pygame.image.load("fond.png")
fenetre.blit(fond, (0, 0))

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Mastermind')
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)

noire = (0, 0, 0)
noireC = (64, 64, 64)
blanc = (255, 255, 180)
blancC = (255, 255, 100)
rouge = (255, 0, 0)
rougeC = (255, 102, 102)
bleu = (0, 0, 255)
bleuC = (102, 102, 255)
jaune = (255, 255, 0)
jauneC = (255, 255, 102)
vert = (0, 255, 0)
vertC = (102, 255, 102)

pygame.draw.circle(fenetre, noire, (536, 86), 16)
pygame.draw.circle(fenetre, blanc, (536, 159), 16)
pygame.draw.circle(fenetre, rouge, (536, 232), 16)
pygame.draw.circle(fenetre, bleu, (536, 305), 16)
pygame.draw.circle(fenetre, vert, (536, 378), 16)
pygame.draw.circle(fenetre, jaune, (536, 451), 16)


def master(propo, solutions):
    i = 0
    bpbc = 0
    bpmc = 0
    while i < 4:
        if solutions[i] == propo[i]:
            solutions[i] = 0
            propo[i] = 1
            bpbc += 1
            i += 1
        else:
            i += 1
    j = 0
    while j < 4:
        l = 0
        while l < 4:
            if solutions[l] == propo[j]:
                bpmc += 1
                solutions[l] = 0
                propo[j] = 1
                l = 4
            else:
                l += 1
        j += 1
    return bpbc, bpmc


def text_objects(text, font):
    textSurface = font.render(text, True, noire)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (300, 300)
    fenetre.fill(blanc)
    fenetre.blit(TextSurf, TextRect)
    pygame.display.update()


def nb_tour(tour):
    fenetre.blit(fond, (50, 70), pygame.Rect(63, 100, 50, 50))
    text = pygame.font.Font(None, 60)
    TextSurf, TextRect = text_objects(tour, text)
    TextRect.center = (63, 100)
    fenetre.blit(TextSurf, TextRect)
    pygame.display.update()


def game_loop():
    propo = ['', '', '', '']
    couleur = ["noir", "blanc", "rouge", "jaune", "vert", "bleu"]
    solutions = []
    for i in range(1, 5):
        solutions.append(couleur[randint(0, 5)])
    sol1 = solutions[0]
    sol2 = solutions[1]
    sol3 = solutions[2]
    sol4 = solutions[3]
    print(solutions)
    crashed = False
    win = False
    loose = False
    tour = 0
    while not crashed:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 125 > mouse[0] > 0 and 600 > mouse[1] > 543:
                    crashed = True
                if 552 > mouse[0] > 520 and 103 > mouse[1] > 70 and pos < 100:
                    pygame.draw.circle(fenetre, noire, (232 + 45 * pos, 571), 16)
                    propo[pos] = "noir"
                if 552 > mouse[0] > 520 and 172 > mouse[1] > 140 and pos < 100:
                    pygame.draw.circle(fenetre, blanc, (232 + 45 * pos, 571), 16)
                    propo[pos] = "blanc"
                if 552 > mouse[0] > 520 and 248 > mouse[1] > 216 and pos < 100:
                    pygame.draw.circle(fenetre, rouge, (232 + 45 * pos, 571), 16)
                    propo[pos] = "rouge"
                if 552 > mouse[0] > 520 and 321 > mouse[1] > 289 and pos < 100:
                    pygame.draw.circle(fenetre, bleu, (232 + 45 * pos, 571), 16)
                    propo[pos] = "bleu"
                if 552 > mouse[0] > 520 and 394 > mouse[1] > 362 and pos < 100:
                    pygame.draw.circle(fenetre, vert, (232 + 45 * pos, 571), 16)
                    propo[pos] = "vert"
                if 552 > mouse[0] > 520 and 467 > mouse[1] > 435 and pos < 100:
                    pygame.draw.circle(fenetre, jaune, (232 + 45 * pos, 571), 16)
                    propo[pos] = "jaune"
                if 248 > mouse[0] > 216 and 587 > mouse[1] > 555:
                    fenetre.blit(fond, (216, 555), pygame.Rect(216, 555, 35, 35))
                if 293 > mouse[0] > 261 and 587 > mouse[1] > 555:
                    fenetre.blit(fond, (261, 555), pygame.Rect(261, 555, 35, 35))
                if 338 > mouse[0] > 306 and 587 > mouse[1] > 555:
                    fenetre.blit(fond, (306, 555), pygame.Rect(306, 555, 35, 35))
                if 383 > mouse[0] > 351 and 587 > mouse[1] > 555:
                    fenetre.blit(fond, (351, 555), pygame.Rect(351, 555, 35, 35))
                if 600 > mouse[0] > 474 and 600 > mouse[1] > 543 and pos == 100:
                    print(sol1, sol2, sol3, sol4, solutions)
                    solutions = [sol1, sol2, sol3, sol4]
                    print(solutions)
                    pygame.draw.circle(fenetre, fenetre.get_at((232, 571)), (194, 482 - 57 * tour), 16)
                    pygame.draw.circle(fenetre, fenetre.get_at((277, 571)), (239, 482 - 57 * tour), 16)
                    pygame.draw.circle(fenetre, fenetre.get_at((322, 571)), (284, 482 - 57 * tour), 16)
                    pygame.draw.circle(fenetre, fenetre.get_at((367, 571)), (329, 482 - 57 * tour), 16)
                    fenetre.blit(fond, (351, 555), pygame.Rect(351, 555, 35, 35))
                    fenetre.blit(fond, (306, 555), pygame.Rect(306, 555, 35, 35))
                    fenetre.blit(fond, (261, 555), pygame.Rect(261, 555, 35, 35))
                    fenetre.blit(fond, (216, 555), pygame.Rect(216, 555, 35, 35))
                    checker = master(propo, solutions)
                    print(checker)
                    pos1 = (392, 471 - 57 * tour)
                    pos2 = (416, 471 - 57 * tour)
                    pos3 = (392, 488 - 57 * tour)
                    pos4 = (416, 488 - 57 * tour)
                    position = [pos1, pos2, pos3, pos4]
                    ind_pos = 0
                    if checker[0] == 4:
                        crashed = True
                        win = True
                    for i in range(1, checker[0] + 1):
                        pygame.draw.circle(fenetre, rouge, position[i - 1], 7)
                        ind_pos += 1
                    for i in range(1, checker[1] + 1):
                        pygame.draw.circle(fenetre, blanc, position[i - 1 + ind_pos], 7)
                    tour += 1
                    if 9 - tour == 0:
                        crashed = True
                        loose = True
            if event.type == pygame.MOUSEMOTION:
                if 552 > mouse[0] > 520 and 103 > mouse[1] > 70:
                    pygame.draw.circle(fenetre, noireC, (536, 86), 16)
                else:
                    pygame.draw.circle(fenetre, noire, (536, 86), 16)

                if 552 > mouse[0] > 520 and 172 > mouse[1] > 140:
                    pygame.draw.circle(fenetre, blancC, (536, 159), 16)
                else:
                    pygame.draw.circle(fenetre, blanc, (536, 159), 16)

                if 552 > mouse[0] > 520 and 248 > mouse[1] > 216:
                    pygame.draw.circle(fenetre, rougeC, (536, 232), 16)
                else:
                    pygame.draw.circle(fenetre, rouge, (536, 232), 16)

                if 552 > mouse[0] > 520 and 321 > mouse[1] > 289:
                    pygame.draw.circle(fenetre, bleuC, (536, 305), 16)
                else:
                    pygame.draw.circle(fenetre, bleu, (536, 305), 16)

                if 552 > mouse[0] > 520 and 394 > mouse[1] > 362:
                    pygame.draw.circle(fenetre, vertC, (536, 378), 16)
                else:
                    pygame.draw.circle(fenetre, vert, (536, 378), 16)

                if 552 > mouse[0] > 520 and 467 > mouse[1] > 435:
                    pygame.draw.circle(fenetre, jauneC, (536, 451), 16)
                else:
                    pygame.draw.circle(fenetre, jaune, (536, 451), 16)

        if fenetre.get_at((232, 571))[0] not in [0, 255, 102]:
            pos = 0
        elif fenetre.get_at((277, 571))[0] not in [0, 255, 102]:
            pos = 1
        elif fenetre.get_at((322, 571))[0] not in [0, 255, 102]:
            pos = 2
        elif fenetre.get_at((367, 571))[0] not in [0, 255, 102]:
            pos = 3
        else:
            pos = 100

        nb_tour(str(9 - tour))

        pygame.display.update()
        clock.tick(60)
    while win:
        for event in pygame.event.get():
            if event.type == QUIT:
                win = False
        fenetre.fill(blanc)
        message_display('GAGNE')
    while loose:
        for event in pygame.event.get():
            if event.type == QUIT:
                loose = False
        fenetre.fill(blanc)
        message_display('GAME OVER')


game_loop()
pygame.quit()
quit()
