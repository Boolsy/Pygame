import pygame
import random

# definir une classe pour gérer la comet
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('Assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 2)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event


    def remove(self):
        self.comet_event.all_comets.remove(self)

        #vérifier si le nombre de boule de feu est égal à 0
        if len(self.comet_event.all_comets) == 0:
            print("l'evenement est fini")
            #remettre la barre d'evenement à 0
            self.comet_event.reset_percent()
            #apparaitre les monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 500:
            print ("Comet delete")
            self.remove()

          #si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("l'evenement est fini")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #vérifie si la boule de feu entre en collision avec le joueur
        if self.comet_event.game.check_collision(
          self, self.comet_event.game.all_players
        ):
            print("joueur hit")
            #retirer la boule de feu
            self.remove()
            #infliger des dégats
            self.comet_event.game.player.damage(20)
