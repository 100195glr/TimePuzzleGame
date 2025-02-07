import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Rewind Puzzle Prototype")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()


player = pygame.Rect(50, 500, 40, 40)
player_speed = 5
gravity = 0.5
jump_strength = -10
velocity_y = 0
on_ground = False


crate = pygame.Rect(300, 500, 40, 40)
crate_velocity_y = 0
crate_start_x, crate_start_y = crate.x, crate.y


goal = pygame.Rect(700, 500, 50, 50)


running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
        if player.colliderect(crate):
            player.left = crate.right

    if keys[pygame.K_RIGHT]:
        player.x += player_speed
        if player.colliderect(crate):
            player.right = crate.left

    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_strength
        on_ground = False

    velocity_y += gravity
    player.y += velocity_y

    if player.y >= 500:
        player.y = 500
        velocity_y = 0
        on_ground = True

    if player.colliderect(crate) and velocity_y > 0:
        player.bottom = crate.top
        velocity_y = 0
        on_ground = True

    crate_velocity_y += gravity
    crate.y += crate_velocity_y

    if crate.y >= 500:
        crate.y = 500
        crate_velocity_y = 0

    if keys[pygame.K_r]:
        crate.x, crate.y = crate_start_x, crate_start_y
        crate_velocity_y = 0


    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, crate)
    pygame.draw.rect(screen, BLACK, goal)

    if player.colliderect(goal):
        print("You Win!")
        running = False


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()