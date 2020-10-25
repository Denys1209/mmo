import pygame
import time
import random 
class Drawing():
    
    def __init__(self, playr, map_1, sc, object_list, ip_map, map_predmet, map_enemy, enemy_list, map_environment, list_predmet, list_cvest, map_ocrug, efect):
        self.sc = sc 
        self.map = map_1
        self.playr = playr
        self.object_list = object_list
        self.ip_map = ip_map
        self.map_predmet = map_predmet
        self.map_enemy =map_enemy
        self.enemy_list =enemy_list
        self.map_environment =map_environment
        self.list_predmet = list_predmet
        self.list_cvest =list_cvest
        self.map_ocrug =map_ocrug

        self.efect = efect
        if (self.efect != None):
            rand = random.randint(0, 1)
            if (rand):
                self.efect = efect
            else:
                self.efect=None
        self.iteraz = 0
        
        
        
    def drawing(self):
        for i in range(0, len(self.map)):
            for a in range(0, len(self.map[i])):
                ob = self.object_list[self.map[i][a]]
                self.sc.blit(ob, (a*32, i*32))
        for i in range(0, len(self.map_ocrug)):
            for a in range(0, len(self.map_ocrug[i])):
                if self.map_ocrug[i][a] != ' ':
                    ob = self.object_list[self.map_ocrug[i][a]]
                    self.sc.blit(ob, (a*32, i*32))   
        for i in range(0, len(self.ip_map)):
            for a in range(0, len(self.ip_map[i])):
                if (self.ip_map[i][a] !=''):
                    self.sc.blit(self.object_list[self.ip_map[i][a]], (a*32, i*32))
        for i in range(0, len(self.map_predmet)):
            for a in range(0, len(self.map_predmet[i])):
                if (self.map_predmet[i][a] !=''):
                    self.sc.blit(self.object_list[self.map_predmet[i][a]], (a*32, i*32))
        for i in range(0, len(self.map_enemy)):
            for a in range(0, len(self.map_enemy[i])):
                if (self.map_enemy[i][a] !=''):
                    self.sc.blit(self.enemy_list[self.map_enemy[i][a]].image, (a*32, i*32))
        
        self.sc.blit(self.playr.image, self.playr.get_x_and_y())
        for i in range(0, len(self.map_environment)):
            for a in range(0, len(self.map_environment[i])):
                if (self.map_environment[i][a] !=''):
                    self.sc.blit(self.object_list[self.map_environment[i][a]], (a*32, i*32))
        if self.efect != None:
            for i in range(0, len(self.map)):
                for a in range(0, len(self.map[i])):
                    self.sc.blit(self.efect[self.iteraz], (a*32, i*32))
            self.iteraz += 1
            if (self.iteraz == len(self.efect)-1):
                self.iteraz =0
                    
    def invertal(self):
        cvadrat = pygame.image.load('D:\\Denis\\cvadrat.png')
        cvadrat_black = pygame.image.load('D:\\Denis\\cvadratblack.png')
        rect_cvadrat = cvadrat.get_rect(bottomright=(32, 32))
        rect_cvadrat_black = cvadrat_black.get_rect(bottomright=(32, 32))
        y,x = (0, 0)
        for i in range(0, len(self.playr.unventari)):
            for a in range(0, len(self.playr.unventari[i])):
                if self.playr.unventari[i][a] != None:
                    self.sc.blit( self.playr.unventari[i][a].image, ( i*32,a*32))
                else:
                    pygame.draw.rect(self.sc, (0, 255, 0), (0, 0, i*32, a*32))
                pygame.display.update()
                 
                    
        
        for a in range(0, 640//32):
            pygame.draw.line(self.sc, (0,0,0), [0, a*32], [640, a*32],5)
            pygame.display.update()
        for a in range(0, 640//32):
            pygame.draw.line(self.sc, (0,0,0), [a*32, 0], [a*32, 320], 5)
            pygame.display.update()
        invertals = True
        while invertals:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_LEFT:
                        if (x-1 != -1):
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            x-=1
                        else:
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            x = 19
                        
                    elif i.key == pygame.K_RIGHT:
                        if (x+1 != 20):
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            x += 1

                        else:
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            x = 0
                        
                    elif i.key == pygame.K_UP:
                        if (y-1 != -1):
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            y -= 1
                        else:
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            y = 9
                    elif i.key == pygame.K_DOWN:
                        if (y+1 != 10):
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            y += 1

                        else:
                            self.sc.blit(cvadrat_black, ( x*32,y*32))
                            y = 0
                    elif i.key == pygame.K_t:
                        invertals = False
                    elif i.key == pygame.K_g:
                        x1, y1  =self.playr.get_x_and_y()
                        self.map_predmet[y1//32][x1//32] = self.playr.unventari[x][y].name
                        self.playr.unventari[x][y].image = pygame.image.load('D:\\Denis\\greencvadrat.png')
                        self.playr.unventari[x][y].name = "нет предмета"
                        self.playr.unventari[x][y].tag = "not predmet"
                        self.playr.unventari[x][y].dameg = 0
                        for i in range(0, len(self.playr.unventari)):
                            for a in range(0, len(self.playr.unventari[i])):
                                if self.playr.unventari[i][a] != None:
                                    self.sc.blit( self.playr.unventari[i][a].image, ( i*32,a*32))
                                else:
                                    pygame.draw.rect(self.sc, (0, 255, 0), (0, 0, i*32, a*32))
                        for a in range(0, 640//32):
                            pygame.draw.line(self.sc, (0,0,0), [0, a*32], [640, a*32],5)
                            pygame.display.update()
                        for a in range(0, 640//32):
                            pygame.draw.line(self.sc, (0,0,0), [a*32, 0], [a*32, 320], 5)
                            pygame.display.update()
                    elif i.key == pygame.K_y:
                        if ( self.playr.unventari[x][y].tag == "weapon"):
                            if (self.playr.weapon.tag == "weapon"):
                                self.playr.weapon.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, self.playr.weapon.name
                                self.playr.weapon.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.weapon.image
                                self.playr.weapon.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.weapon.dameg
                                self.playr.weapon.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.weapon.tag
                            else:
                                self.playr.weapon.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, "нет предмета"
                                self.playr.weapon.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.weapon.image
                                self.playr.weapon.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.weapon.dameg
                                self.playr.weapon.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.weapon.tag

                        elif (self.playr.unventari[x][y].tag == "strap dameg"):
                            if (self.playr.strap.tag == "strap dameg"):
                                self.playr.strap.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, self.playr.strap.name
                                self.playr.strap.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.strap.image
                                self.playr.strap.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.strap.dameg
                                self.playr.strap.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.strap.tag
                            else:
                                self.playr.strap.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, "нет предмета"
                                self.playr.strap.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.strap.image
                                self.playr.strap.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.strap.dameg
                                self.playr.strap.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.strap.tag
                        
                        elif (self.playr.unventari[x][y].tag == "boots"):
                            if (self.playr.boots.tag == "boots"):
                                self.playr.speed -= self.playr.boots.dameg
                                self.playr.boots.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, self.playr.boots.name
                                self.playr.boots.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.boots.image
                                self.playr.boots.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.boots.dameg
                                self.playr.boots.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.boots.tag
                                self.playr.speed += self.playr.boots.dameg
                            else:
                                self.playr.boots.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, "нет предмета"
                                self.playr.boots.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.boots.image
                                self.playr.boots.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.boots.dameg
                                self.playr.boots.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.boots.tag
                                self.playr.speed += self.playr.boots.dameg
                        elif (self.playr.unventari[x][y].tag == "strap resist"):
                            if (self.playr.strap_resist.tag == "strap resist"):
                                self.playr.strap_resist.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, self.playr.strap_resist.name
                                self.playr.strap_resist.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.strap_resist.image
                                self.playr.strap_resist.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.strap_resist.dameg
                                self.playr.strap_resist.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.strap_resist.tag
                            else:
                                self.playr.strap_resist.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, "нет предмета"
                                self.playr.strap_resist.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.strap_resist.image
                                self.playr.strap_resist.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.strap_resist.dameg
                                self.playr.strap_resist.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.strap_resist.tag
                        elif (self.playr.unventari[x][y].tag == "nagrud"):
                            if (self.playr.nagrud.tag == "nagrud"):
                                self.playr.nagrud.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, self.playr.nagrud.name
                                self.playr.nagrud.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.nagrud.image
                                self.playr.nagrud.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.nagrud.dameg
                                self.playr.nagrud.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.nagrud.tag
                            else:
                                self.playr.nagrud.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, "нет предмета"
                                self.playr.nagrud.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.nagrud.image
                                self.playr.nagrud.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.nagrud.dameg
                                self.playr.nagrud.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.nagrud.tag
                        elif (self.playr.unventari[x][y].tag == "shield"):
                            if (self.playr.shield.tag == "shield"):
                                self.playr.shield.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, self.playr.strap_resist.name
                                self.playr.shield.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.strap_resist.image
                                self.playr.shield.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.strap_resist.dameg
                                self.playr.shield.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.strap_resist.tag
                            else:
                                self.playr.shield.name,self.playr.unventari[x][y].name  = self.playr.unventari[x][y].name, "нет предмета"
                                self.playr.shield.image, self.playr.unventari[x][y].image = self.playr.unventari[x][y].image, self.playr.shield.image
                                self.playr.shield.dameg, self.playr.unventari[x][y].dameg = self.playr.unventari[x][y].dameg, self.playr.shield.dameg
                                self.playr.shield.tag, self.playr.unventari[x][y].tag = self.playr.unventari[x][y].tag, self.playr.shield.tag
                            
                        elif (self.playr.unventari[x][y].tag == "potion help"):
                            hp = 0
                            if (self.playr.max_hp-(self.playr.hp+self.playr.unventari[x][y].dameg)) <=0:
                                hp = (self.playr.hp+self.playr.unventari[x][y].dameg)+(self.playr.max_hp-(self.playr.hp+self.playr.unventari[x][y].dameg))
                            else:
                                hp = (self.playr.hp+self.playr.unventari[x][y].dameg)-(self.playr.max_hp-(self.playr.hp+self.playr.unventari[x][y].dameg))
                            self.playr.hp = hp
                            self.playr.unventari[x][y].name = "нет предмета"
                            self.playr.unventari[x][y].image = pygame.image.load('D:\\Denis\\greencvadrat.png')
                            self.playr.unventari[x][y].dameg = 0
                            self.playr.unventari[x][y].tag = "not predmet"
                        elif (self.playr.unventari[x][y].tag == "switac dameg"):
                            self.playr.dameg+=self.playr.unventari[x][y].dameg()
                            
                        for i in range(0, len(self.playr.unventari)):
                            for a in range(0, len(self.playr.unventari[i])):
                                if self.playr.unventari[i][a] != None:
                                    self.sc.blit( self.playr.unventari[i][a].image, ( i*32,a*32))
                                else:
                                    pygame.draw.rect(self.sc, (0, 255, 0), (0, 0, i*32, a*32))
                        for a in range(0, 640//32):
                            pygame.draw.line(self.sc, (0,0,0), [0, a*32], [640, a*32],5)
                            pygame.display.update()
                        for a in range(0, 640//32):
                            pygame.draw.line(self.sc, (0,0,0), [a*32, 0], [a*32, 320], 5)
                            pygame.display.update()
                        
                        
                        
                       
            self.sc.blit(cvadrat, ( x*32,y*32))
            pygame.draw.rect(self.sc, (0, 0, 0), (0, 350, 600, 600))
            f2 = pygame.font.SysFont('serif', 48)
            if (self.playr.unventari[x][y].tag == "weapon"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("урон = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "strap dameg"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Дополнительный урон = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "boots"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Дополнительная скорость = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "strap resist"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Поглощение урона = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "shield"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Поглощение урона = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "nagrud"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Поглощение урона = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "nagrud"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Поглощение урона = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 400))
                self.sc.blit(text2, (0, 500))
            elif (self.playr.unventari[x][y].tag == "switac dameg"):
                text1 = f2.render(str(self.playr.unventari[x][y].name), 0, (0, 255, 0))
                text2 = f2.render("Добавляет к минимального урона = "+str(self.playr.unventari[x][y].dameg), 0, (0, 255, 0))
                self.sc.blit(text1, (0, 350))
                self.sc.blit(text2, (0, 450))
               
            elif (self.playr.unventari[x][y].tag == "just predmet"):
                text1 = f2.render(self.playr.unventari[x][y].name, 0, (0, 255, 0))
                self.sc.blit(text1, (0, 350))
            elif (self.playr.unventari[x][y].tag == "not predmet"):
                text1 = f2.render("нет предмета", 0, (0, 255, 0))
                self.sc.blit(text1, (0, 350))


            
            

           
            pygame.display.update()
    #do not remove comments
    def fight(self, enyme, y, x):
        
        
        self.sc.fill((0, 0, 0))
        
        
        f2 = pygame.font.SysFont('serif', 48)
        fight = True
        variant_fight = ["удар", "блок", "инвентарь"]
        while fight:
            
            self.sc.fill((0, 0, 0))
            prohod_otvet = 0
            bloc = self.playr.strap_resist.dameg+self.playr.nagrud.dameg+self.playr.shield.dameg
            kick = 0
            playrs = True
            while playrs:
                
                #pygame.display.update()
                
                text1 = f2.render("ваше "+"hp = "+str(self.playr.hp), 0, (0, 255, 0))
                text2 = f2.render("hp противника = "+str(enyme.hp), 0, (0, 255, 0))
                text3 = f2.render("варианты действий:", 0, (0, 255, 0))
                self.sc.blit(text1, (0, 0))
                self.sc.blit(text2, (0, 100))
                self.sc.blit(text3, (0, 200))
                for i in range(len(variant_fight)):
                    if (i == prohod_otvet):
                        text4 = f2.render(">"+variant_fight[i], 0, (0, 255, 0))
                    else:
                        text4 = f2.render(variant_fight[i], 0, (0, 255, 0))
                    
                
                    self.sc.blit(text4, (0, 350+i*100))
                pygame.display.update()
                self.sc.fill((0,0,0))
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        exit()
                    elif i.type == pygame.KEYDOWN:
                        if i.key == pygame.K_UP:
                            if (prohod_otvet-1 != -1):
                                prohod_otvet-=1
                            else:
                                prohod_otvet = len(variant_fight)-1
                        
                        elif i.key == pygame.K_DOWN:
                            if (prohod_otvet <= len(variant_fight)-1):
                                prohod_otvet+=1
                            else:
                                prohod_otvet = 0
                        elif i.key == pygame.K_e:
                            playrs = False
                            if (prohod_otvet == 0):
                                kick = self.playr.get_kick()
                                enyme.hp -= kick
                            elif(prohod_otvet == 1):
                                bloc += self.playr.get_block()
                            elif(prohod_otvet == 2):
                                self.invertal()
                
                
                
            self.sc.fill((0, 0, 0))
            text1 = f2.render("ваш удар нанес "+str(kick), 0, (0, 255, 0))
            text2 = f2.render("заблокировано столько урона "+str(bloc), 0, (0, 255, 0))
            self.sc.blit(text1, (0, 0))
            self.sc.blit(text2, (0, 100))
            pygame.display.update()
            
            if enyme.get_kick()-int(bloc) >0: 
                kick_npc=enyme.get_kick()-bloc 
            else: 
                kick_npc=0

            block_npc = 0
            self.playr.hp -= kick_npc
            text3 = f2.render("Вам нанесли столько урона"+str(kick_npc), 0, (0, 255, 0))
            text4 = f2.render("противник заблокировал "+str(block_npc), 0, (0, 255, 0))
            self.sc.blit(text3, (0, 200))
            self.sc.blit(text4, (0, 300))
            pygame.display.update()
            time.sleep(3)
            
            self.sc.fill((0,0,0))
            if (enyme.hp <= 0):
                fight = False
                self.map_enemy[y][x] = ''
                self.map_predmet[y][x] = enyme.pred_posli_smert
                return
            elif(self.playr.hp <= 0):
                fight = False
                print("you lose")
                self.playr.hp =self.playr.max_hp
                return
            #pygame.display.update()
    def menu_cvest(self):
        f2 = pygame.font.SysFont('serif', 48)
        y = 0
        T = True
        while T:
            self.sc.fill((0,0,0))
            for i in range(0,len(self.playr.list_cvest)):
                if (i == y):
                    text3 = f2.render(">"+self.playr.list_cvest[i].name, 0, (0, 255, 0))
                else:
                    text3 = f2.render(self.playr.list_cvest[i].name, 0, (0, 255, 0))
                self.sc.blit(text3, (0, i*100+100))
                
            
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_UP:
                        if (y-1 != -1):
                            y-=1
                        else:
                            y = len(self.playr.list_cvest)-1
                    elif i.key == pygame.K_DOWN:
                        if (y <= len(self.playr.list_cvest)-1):
                            y+=1
                        else:
                            y = 0
                    elif i.key == pygame.K_e:
                        if (self.playr.list_cvest[y].name != "нет квеста"):
                            self.opis_cvest(self.playr.list_cvest[y], y)
                    elif i.key == pygame.K_q:
                        T= False
            pygame.display.update()
                
    def opis_cvest(self, cv, namber):
        T = True
        f2 = pygame.font.SysFont('serif', 24)
        while T:
            self.sc.fill((0,0,0))
            op = ''
            st = 1
           
            op +=cv.opis
            text3 = f2.render(op, 0, (0, 255, 0))
            self.sc.blit(text3, (0, 100*st))
                
            pygame.display.update()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_e:
                        if (cv.zdat(self.playr)):
                            self.playr.list_cvest[namber].name = "нет квеста"
                            self.playr.list_cvest[namber].predmet = ""
                            self.playr.list_cvest[namber].opis = ""
                            self.playr.list_cvest[namber].get_predmet = ''
                            return
                            print("cv")
                    elif i.key == pygame.K_q:
                        return
                    





    
        

        