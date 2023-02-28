import pygame

# definir la classe qui gère le projectile du joueur 
class Projectile(pygame.sprite.Sprite):
    
    # definir le constructeur de cette classe
    def __init__(self,player):
        super().__init__()
        self.player = player
        self.velocity = 2
        self.image = pygame.image.load('Assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        # tourne le projectile
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self) 
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        # verifie si le projectile n'est plus présent sur l'écran 
        if self.rect.x > 1080:
    #supprime le projectile en dehors de l'écran
            self.remove()
            print("Projectile delete")