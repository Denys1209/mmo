import pygame

class predmet():
    def __init__(self, name = "нет предмета", image =pygame.image.load('D:\\Denis\\greencvadrat.png'), dameg = 0,tag = "not predmet" ):
        self.name = name
        self.image = image
        self.tag = tag
        self.dameg = dameg
    def misappropriate(self,pr):
        self.tag = pr.tag
        self.dameg = pr.dameg
        self.image = pr.image
        self.name = pr.name

