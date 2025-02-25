#pip install pygame
#xiaoyuan suo
import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GUN_WIDTH, GUN_HEIGHT = 40, 30
BULLET_WIDTH, BULLET_HEIGHT = 5, 15
ALIEN_RADIUS = 10
ALIEN_SPEED = 2
BULLET_SPEED = 5
GUN_SPEED = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooter")

# Gun position
gun_x = WIDTH // 2
gun_y = HEIGHT - 40

# Lists for bullets and aliens
bullets = []
aliens = []

# Clock
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    pygame.time.delay(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and gun_x > GUN_SPEED:
        gun_x -= GUN_SPEED
    if keys[pygame.K_RIGHT] and gun_x < WIDTH - GUN_SPEED:
        gun_x += GUN_SPEED
    if keys[pygame.K_SPACE]:  # Shoot bullet
        bullets.append([gun_x, gun_y])

    # Spawn aliens randomly
    if random.randint(1, 50) == 1:
        aliens.append([random.randint(0, WIDTH - ALIEN_RADIUS), 0])

    # Move bullets
    bullets = [[x, y - BULLET_SPEED] for x, y in bullets if y > 0]

    # Move aliens
    aliens = [[x, y + ALIEN_SPEED] for x, y in aliens if y < HEIGHT]

    # Check for collisions
    new_aliens = []
    for ax, ay in aliens:
        hit = False
        for bx, by in bullets:
            if abs(ax - bx) < ALIEN_RADIUS and abs(ay - by) < BULLET_HEIGHT:
                bullets.remove([bx, by])
                hit = True
                break
        if not hit:
            new_aliens.append([ax, ay])
    aliens = new_aliens

    # Draw gun (triangle)
    pygame.draw.polygon(screen, RED, [(gun_x, gun_y), (gun_x - 20, gun_y + 30), (gun_x + 20, gun_y + 30)])

    # Draw bullets
    for bx, by in bullets:
        pygame.draw.rect(screen, WHITE, (bx, by, BULLET_WIDTH, BULLET_HEIGHT))

    # Draw aliens
    for ax, ay in aliens:
        pygame.draw.circle(screen, RED, (ax, ay), ALIEN_RADIUS)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
