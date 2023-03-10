import pygame
import random

# Crée une classe qui va gérer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health =100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 2)
        self.image = pygame.image.load('Assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.all_projectiles = pygame.sprite.Group()
        self.all_monsters = pygame.sprite.Group()
        self.all_monsters.add(self)

    def damage(self, amount):
        self.health -= amount

        # verifier si son nombre de point de vie est inférieur ou égal à 0
        if self.health <= 0:
            # réaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

        #si la barre d'evenement est chargée au max
        if self.game.comet_event.is_full_loaded():
            #retirer le monstre
            self.game.all_monsters.remove(self)

            #appel de la méthode pour essayer de déclencher la pluie de cometes
            self.game.comet_event.attempt_fall()


    def update_health_bar(self, surface):

        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])



    def forward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            # infliger des dégats
            self.game.player.damage(self.attack)


