import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cartoon Flower Animation")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

def draw_flower(screen, num_petals, petal_length, x, y):
    for _ in range(num_petals):
        pygame.draw.polygon(screen, green, [(x, y), (x + 20, y - petal_length), (x - 20, y - petal_length)])
        pygame.display.flip()
        pygame.time.delay(100)
        screen.fill(white)

def animate_flower(screen, num_petals, petal_length, x, y, rotations):
    for _ in range(rotations):
        pygame.event.pump()
        draw_flower(screen, num_petals, petal_length, x, y)
        pygame.time.delay(10)
        x += 1

# Flower parameters
num_petals = 5
petal_length = 50
x, y = 400, 300
rotations = 500

# Animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    animate_flower(screen, num_petals, petal_length, x, y, rotations)
