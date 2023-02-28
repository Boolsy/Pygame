import pygame
import math
from game import Game

pygame.init()

# Genere la fenetre de jeu
pygame.display.set_caption("EpicGameEnSueur")
# taille en pixel de la fenetre (x,y)screen pour recup la surface
screen = pygame.display.set_mode((1080, 720))

# Importe le fond de la fenetre Charge l'image dans le background mais ne l'affiche pas encore
background = pygame.image.load('Assets/bg.jpg')

#importer charger la bannière
banner = pygame.image.load('Assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charger le bouton pour lancer la partie
play_button = pygame.image.load('Assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)



# charge le jeu
game = Game()

running = True

# Boucle tant que la condition est vrai (True)
while running:

    # Appliquer l arrière plan du jeu
    screen.blit(background, (0, -200))

    # Verifier si le jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commencé
    else:
        # ajouter ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenetre
    for event in pygame.event.get():
        # Que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
    # detecte si le joueur relache une touche 
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            # detecte si la touche espace est press pour lancer le projectile 
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
            
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()