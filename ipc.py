import pygame
from setting import *
from random import randint
from map import *

pygame.init()
class npc():
    def __init__(self, list_vopros, list_otvet, name  ):
        self.list_vopros = list_vopros
        self.list_otvet = list_otvet
        self.name = name
        
        
    def dialog(self, dr):
        
        x = 0
        prohod = 0
        
        f2 = pygame.font.SysFont('serif', 48)
        print_otvet = False
        prohod_otvet = 0
        dialog = True
        while dialog:
            sc.fill((0, 0, 0))
            text_name = f2.render(self.name+" ответ:", 0, (0, 255, 0))
            sc.blit(text_name, (0, 92))
            if (print_otvet == True):
                text1 = f2.render(str(self.list_otvet[prohod_otvet][0]), 0, (0, 255, 0))
                if (self.list_otvet[prohod_otvet][1] != None):
                    if (self.list_otvet[prohod_otvet][1][0] == 'predmet' and self.list_otvet[prohod_otvet][1][1] != None):
                        dr.playr.pol_in_inverta(dr.list_predmet[self.list_otvet[prohod_otvet][1][1]])
                        self.list_otvet[prohod_otvet][1][1] = None
                    elif (self.list_otvet[prohod_otvet][1][0] == 'cvest' and self.list_otvet[prohod_otvet][1][1] != None):
                        dr.playr.cvest_append(dr.list_cvest[self.list_otvet[prohod_otvet][1][1]])
                        self.list_otvet[prohod_otvet][1][1] = None
                sc.blit(text1, (0, 192))
            for i in range(0, len(self.list_vopros)):
                if (i == prohod):
                    text2 = f2.render(">"+str(self.list_vopros[i][0]), 0, (0, 255, 0))
                    sc.blit(text2, (0, 292+100*i))
                else:
                    text2 = f2.render(str(self.list_vopros[i][0]), 0, (0, 255, 0))
                    sc.blit(text2, (0, 292+100*i))
    
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_UP:
                        if (prohod-1 != -1):
                            prohod-=1
                        else:
                            prohod = len(self.list_vopros)-1
                        
                    elif i.key == pygame.K_DOWN:
                        if (prohod <= len(self.list_vopros)-1):
                            prohod+=1
                        else:
                            prohod = 0
                    elif i.key == pygame.K_e:
                        if (self.list_vopros[prohod_otvet][1] == None):
                            print_otvet= True
                            prohod_otvet= prohod
                            
                        else:
                            TorF, y, x = dr.playr.find_predmet(dr.list_predmet[self.list_vopros[prohod_otvet][1]])
                            if (TorF):
                                if ((self.list_otvet[prohod_otvet][1][0] == 'predmet' or self.list_otvet[prohod_otvet][1][0] == 'predmet most')and self.list_otvet[prohod_otvet][1][1] != None):
                                    dr.playr.unventari[y][x] = dr.list_predmet[self.list_otvet[prohod_otvet][1][1]]
                                elif (self.list_otvet[prohod_otvet][1][0] == 'cvest' and self.list_otvet[prohod_otvet][1][1] != None):
                                    dr.playr.cvest_append(dr.list_cvest[self.list_otvet[prohod_otvet][1][1]])
                                if (self.list_otvet[prohod_otvet][1][0] != 'predmet most'):
                                    self.list_otvet[prohod_otvet][1][1] = None
                                    self.list_vopros[prohod_otvet][1] = None
                                print_otvet= True
                                prohod_otvet= prohod
                            else:
                                print_otvet= False
                                prohod_otvet= prohod
                            
                

                    elif i.key == pygame.K_q:
                        dialog = False

            pygame.display.update()
class enemy():
    def __init__(self, image,name, hp, dameg,pred_posli_smert):
        self.image = image
        self.name = name
        self.hp = hp
        self.dameg = dameg
        self.pred_posli_smert = pred_posli_smert
    def get_kick(self):
        return randint(0, self.dameg)
        
        
        

            
    
            
       
            
        

            


