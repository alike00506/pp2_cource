import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((620, 620))
done = False
bg_image = pygame.image.load('C:/Users/Alinur/Documents/pp2/lab7/MicrosoftTeams-image (2).png')
sec_img = pygame.image.load('C:/Users/Alinur/Documents/pp2/lab7/MicrosoftTeams-image (1).png')
min_img = pygame.image.load('C:/Users/Alinur/Documents/pp2/lab7/MicrosoftTeams-image.png')
bg_image = pygame.transform.scale(bg_image, (620, 620))
center_x, center_y = 310, 310
while not done:
    
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    min_angle = -(time.minute * 6)
 
  
    nsec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = nsec_img.get_rect(center=(center_x, center_y))
    screen.blit(nsec_img, sec_rect.topleft)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=(center_x, center_y))
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()