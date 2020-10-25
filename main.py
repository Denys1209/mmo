from drawing import *
from player import *
from map import *
from setting import *
from interaction import *
import pygame

pygame.init()
 

dog_surf = pygame.image.load('D:\\Denis\\priesta.png')
dog_rect = dog_surf.get_rect(bottomright=(640, 640))

pl = player(0, 0, dog_surf)
x_world, y_world = pl.x_map, pl.y_map
dr = Drawing(pl,map_world[y_world][x_world].map_local, sc, object_list, map_world[y_world][x_world].map_ip, map_world[y_world][x_world].map_predmet, map_world[y_world][x_world].map_enemy, enyme_list, map_world[y_world][x_world].map_environment, list_predmet, list_cvest, map_world[y_world][x_world].map_ocrug, map_world[y_world][x_world].efect)

inter = interaction(pl, map_world[y_world][x_world].map_ip, ii_list, map_world[y_world][x_world].map_predmet, list_predmet,enyme_list,map_world[y_world][x_world].map_enemy,dr, map_world[y_world][x_world].map_local)

while 1:
    pygame.display.update()
    sc.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_e:
                inter.do()
            elif i.key == pygame.K_t:
                dr.invertal()
            elif i.key == pygame.K_p:
                dr.menu_cvest()
    dr.drawing()
    if (pl.move()):
        x_world, y_world = pl.x_map, pl.y_map
        dr = Drawing(pl,map_world[y_world][x_world].map_local, sc, object_list, map_world[y_world][x_world].map_ip, map_world[y_world][x_world].map_predmet, map_world[y_world][x_world].map_enemy, enyme_list, map_world[y_world][x_world].map_environment, list_predmet, list_cvest, map_world[y_world][x_world].map_ocrug, map_world[y_world][x_world].efect)
        inter = interaction(pl, map_world[y_world][x_world].map_ip, ii_list, map_world[y_world][x_world].map_predmet, list_predmet,enyme_list,map_world[y_world][x_world].map_enemy,dr, map_world[y_world][x_world].map_local, )

    pygame.time.delay(20)
