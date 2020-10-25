import pygame
from random import randint
from predmet import *
from setting import *
from cvest import cvest
class player():
    def __init__(self, x,y, image):
        self.x = x
        self.y = y
        self.x_map, self.y_map = 2, 2
        self.max_hp = 100
        self.speed = 2
        self.image = image
        self.unventari = [
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],
            [predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet(),predmet()],

            ]
        self.hp = 90
        self.dameg = 5
        self.list_cvest = [cvest(), cvest(), cvest(), cvest(), cvest()]
        self.weapon = predmet()
        self.strap = predmet()
        self.boots = predmet()
        self.nagrud = predmet()
        self.shield = predmet()
        self.strap_resist = predmet()
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            self.y -= self.speed
            if (self.y <= 0):
                self.y_map -=1
                self.y = 580
                return True
            #if (self.not_prohod(interactiv.map_local[self.y//32][self.x//32],interactiv)):
            #    self.y+=self.speed  
        if keys[pygame.K_s]:
            self.y += self.speed
            if (self.y >= 640):
                self.y_map += 1
                if (self.y_map >= SIZE_WORLD):
                    self.y_map = 0
                
                self.y = 64
                return True
            #if (self.not_prohod(interactiv.map_local[self.y//32][self.x//32],interactiv)):
            #    self.y-=self.speed 
        if keys[pygame.K_a]:
            self.x -= self.speed
            if (self.x <= 0):
                self.x_map -= 1
                self.x = 580
                return True
            #if (self.not_prohod(interactiv.map_local[self.y//32][self.x//32],interactiv)):
            #   self.x+=self.speed 

        if keys[pygame.K_d]:
            self.x += self.speed
            if (self.x >= 640):
                self.x_map +=1
                if (self.x_map >= SIZE_WORLD):
                    self.x_map = 0
                self.x = 64
                return True
            #if (self.not_prohod(interactiv.map_local[self.y//32][self.x//32+1],interactiv)):
            #    self.x-=self.speed 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        return False
    
            

        
    def get_image(self):
        return self.image
    def get_x_and_y(self):
        return (self.x, self.y)
    def pol_in_inverta(self, pred):
        for i in range(len(self.unventari)):
            for a in range(len(self.unventari[i])):
                if (self.unventari[i][a].tag == "not predmet"):
                    self.unventari[i][a].name = pred.name
                    self.unventari[i][a].image = pred.image
                    self.unventari[i][a].dameg = pred.dameg
                    self.unventari[i][a].tag = pred.tag
                    return
    def get_kick(self):
        return randint(self.dameg, self.dameg + self.weapon.dameg + self.strap.dameg)
    def get_block(sekf):
        return randint(0, 10)
    def not_prohod(self, block, interactiv):
        for i in interactiv.list_not_prohod:
            if block == i:
                return True
        return False
    def cvest_append(self, cve):
        for i in range(0, len(self.list_cvest)):
            if (self.list_cvest[i].name == "нет квеста"):
                self.list_cvest[i].name = cve.name
                self.list_cvest[i].predmet = cve.predmet
                self.list_cvest[i].opis = cve.opis
                self.list_cvest[i].get_predmet = cve.get_predmet
                break
                

    def find_predmet(self, pred):
        for i in range(0, len(self.unventari)):
            for k in range(0, len(self.unventari[i])):
                if(self.unventari[i][k].name == pred.name):
                    print(1)
                    return (True,i, k)
        return (False,0, 0)






