import titlu
class cvest():
    def __init__(self, predmet = '', opis = '', name = "нет квеста", get_predmet = "", tag = ''):
        self.opis = opis
        self.predmet = predmet
        self.name = name
        self.get_predmet = get_predmet
        self.tag = tag
    def zdat(self, pl):
        TorF, y, x = pl.find_predmet(self.predmet)
        
        if (TorF):
            if (self.tag != "JUST CVEST"):
                titlu.titlu()
                exit()
            else:
                pl.unventari[y][x].name = self.get_predmet.name
                pl.unventari[y][x].tag = self.get_predmet.tag
                pl.unventari[y][x].image = self.get_predmet.image
                pl.unventari[y][x].dameg = self.get_predmet.dameg
                return True

        return False
    




