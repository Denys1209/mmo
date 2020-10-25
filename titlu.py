import pygame
from setting import *
def titlu():
    sc.fill((0,0,0))
    y_title = [640, 740, 840]
    speed = 10
    natpis = ["Программист Денис", "Продакт менеджер Денис", "И вообще все сделал Денис"]
    f2 = pygame.font.SysFont('serif', 48)
    
    while True:
        text1 = f2.render(natpis[0], 0, (0, 255, 0))
        text2 = f2.render(natpis[1], 0, (0, 255, 0))
        text3 = f2.render(natpis[2], 0, (0, 255, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        sc.blit(text1, (0, y_title[0]))
        sc.blit(text2, (0, y_title[1]))
        sc.blit(text3, (0, y_title[2]))
        y_title[0]-=0.05
        y_title[1]-=0.05
        y_title[2]-=0.05
        pygame.display.update()
        sc.fill((0,0,0))


        
        
        