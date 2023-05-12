import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH//COLUMNS


# colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown2.png'), (45, 25))
# CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))

HUMANVSCOMPUTER = "HUMANVSCOMPUTER"
HUMANVSHUMAN = "HUMANVSHUMAN"
COMPUTERVSCOMPUTER = "COMPUTERVSCOMPUTER"
