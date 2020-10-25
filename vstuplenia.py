import pygame
from setting import sc
def loga():
    loga = pygame.image.load("D:\\Denis\\loga.png")
    compani = pygame.image.load("D:\\Denis\\compani.png")
    sc.blit(loga, (0, 0))
    sc.blit(compani, (0, 300))
    pygame.display.update()
    