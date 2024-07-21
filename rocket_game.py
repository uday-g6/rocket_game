import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rocket Game")

# Rocket class
class Rocket:
    def __init__(self):
        self.width = 50
        self.height = 60
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

        # Boundary check
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height

        self.rect.topleft = (self.x, self.y)

    def draw(self):
        rocket_design = [
            (self.x + 25, self.y),  # Top point
            (self.x, self.y + 30),  # Bottom left point
            (self.x + 12.5, self.y + 30),  # Bottom left wing point
            (self.x + 12.5, self.y + 50),  # Bottom left wing bottom point
            (self.x + 25, self.y + 60),  # Bottom center point
            (self.x + 37.5, self.y + 50),  # Bottom right wing bottom point
            (self.x + 37.5, self.y + 30),  # Bottom right wing point
            (self.x + 50, self.y + 30)   # Bottom right point
        ]
        pygame.draw.polygon(screen, BLUE, rocket_design)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.width = 5
        self.height = 10
        self.x = x + 22.5
        self.y = y
        self.speed = 7
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.y -= self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Enemy class
class Enemy:
    def __init__(self, health):
        self.width = 50
        self.height = 50
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(2, 5)
        self.health = health  # Set enemy health based on score
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Game loop
def game_loop():
    rocket = Rocket()
    bullets = []
    enemies = []
    score = 0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        screen.fill(BLACK)  # Fill the screen with black

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_KP8]:
            dy = -1
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_KP4]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_KP6]:
            dx = 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN] or keys[pygame.K_KP2]:
            dy = 1

        rocket.move(dx, dy)
        rocket.draw()

        # Fire bullets continuously when space bar is held down
        if keys[pygame.K_SPACE]:
            bullets.append(Bullet(rocket.x, rocket.y))

        # Determine enemy health based on score
        enemy_health = 3
        if score > 50:
            enemy_health = 5
        elif score > 100:
            enemy_health = 7
        elif score > 150:
            enemy_health = 10
        elif score > 200:
            enemy_health = 12

        if random.randint(1, 20) == 1:
            enemies.append(Enemy(enemy_health))

        for bullet in bullets:
            bullet.move()
            bullet.draw()

        for enemy in enemies:
            enemy.move()
            enemy.draw()
            if enemy.rect.colliderect(rocket.rect):
                running = False

        for bullet in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemy.health -= 1
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                        score += 1
                    break

        bullets = [bullet for bullet in bullets if bullet.y > 0]
        enemies = [enemy for enemy in enemies if enemy.y < SCREEN_HEIGHT]

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Display controls
        controls_text = font.render("Controls:", True, WHITE)
        screen.blit(controls_text, (SCREEN_WIDTH - 120, 10))

        pygame.draw.polygon(screen, WHITE, [(SCREEN_WIDTH - 100, 40), (SCREEN_WIDTH - 80, 40), (SCREEN_WIDTH - 90, 20)])
        pygame.draw.polygon(screen, WHITE, [(SCREEN_WIDTH - 100, 80), (SCREEN_WIDTH - 80, 80), (SCREEN_WIDTH - 90, 100)])
        pygame.draw.polygon(screen, WHITE, [(SCREEN_WIDTH - 120, 60), (SCREEN_WIDTH - 120, 80), (SCREEN_WIDTH - 140, 70)])
        pygame.draw.polygon(screen, WHITE, [(SCREEN_WIDTH - 80, 60), (SCREEN_WIDTH - 80, 80), (SCREEN_WIDTH - 70, 70)])

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
