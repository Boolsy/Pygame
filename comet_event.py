import pygame


#crée une classe pour gérer cet evenement
class CometFallEvent:

    # lors du chargement -> créer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed = 3

        #definir un groupe de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def update_bar(self, surface):
        #ajouter du pourcentage à la barre
        self.add_percent()
        #barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,#axe des x
            surface.get_height() - 20,#axe des y
            surface.get_width(),#longueur de la surface
            10 #epaisseur de la barre
        ])
        #barre rouge (en avant plan)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la surface
            10  # epaisseur de la barre
        ])