import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("куб")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    screen.fill(WHITE)  
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))  
    pygame.display.flip()  

    pygame.time.Clock().tick(30)