# import pygame
# import sys
# pygame.init()

# # Set up the screen
# SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Moving Ball")
# clock = pygame.time.Clock()
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BALL_RADIUS = 25
# BALL_DIAMETER = BALL_RADIUS * 2
# BALL_SPEED = 20
# ball_x = (SCREEN_WIDTH - BALL_DIAMETER) // 2
# ball_y = (SCREEN_HEIGHT - BALL_DIAMETER) // 2
# running = True
# while running:
#     screen.fill(WHITE)  

#     pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

#     pygame.display.flip()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 ball_y = max(ball_y - BALL_SPEED, BALL_RADIUS)
#             elif event.key == pygame.K_DOWN:
#                 ball_y = min(ball_y + BALL_SPEED, SCREEN_HEIGHT - BALL_RADIUS)
#             elif event.key == pygame.K_LEFT:
#                 ball_x = max(ball_x - BALL_SPEED, BALL_RADIUS)
#             elif event.key == pygame.K_RIGHT:
#                 ball_x = min(ball_x + BALL_SPEED, SCREEN_WIDTH - BALL_RADIUS)
#     clock.tick(60)

# pygame.quit()
# sys.exit()
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 200
y = 150
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-25>0: y -= 20
    if pressed[pygame.K_DOWN] and y+25<300: y += 20
    if pressed[pygame.K_LEFT] and x-25>0: x -= 20
    if pressed[pygame.K_RIGHT] and x+25<400: x += 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()