import pygame

class interaction():
    def __init__(self, player, map_ip, ii_list, map_predmat, list_predmat, list_enemy,map_enyme, dr, map_local):
        self.player = player
        self.map_ip = map_ip
        self.ii_list = ii_list
        self.map_predmat = map_predmat
        self.list_predmat = list_predmat
        self.list_enemy =  list_enemy
        self.map_enyme = map_enyme
        self.dr= dr
        self.map_local =map_local
        
    def do(self):
        x, y =self.player.get_x_and_y()
       
        if (self.map_predmat[y//32][x//32] != ''):
            self.player.pol_in_inverta(self.list_predmat[self.map_predmat[y//32][x//32]])
            self.map_predmat[y//32][x//32] = ''
            print(1)
        elif (self.map_enyme[y//32][x//32] != ''):
            
            self.dr.fight(self.list_enemy[self.map_enyme[y//32][x//32]],y//32,x//32)
            print(1)
        elif (self.map_ip[y//32][x//32] != ''):
            self.ii_list[self.map_ip[y//32][x//32]].dialog(self.dr)

        
            
            
            
