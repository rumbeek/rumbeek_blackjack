import pygame
pygame.init()

# Parameters

SUITS = ['club', 'spade', 'heart', 'diamond']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

resolution = (1000, 750)
background = pygame.image.load('img/background.png')
table = pygame.image.load('img/table.jpg')
icon = pygame.image.load('img/icon.png')

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode(resolution)

pygame.display.set_caption("Blackjack")
pygame.display.set_icon(icon)
gameDisplay.blit(table, (0, 0))

pygame.display.flip()

grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (193,205,205)
dark_slat = (238,121,66)
dark_red = (255, 0, 0)
font = pygame.font.SysFont("Comic Sans MS", 30, True, True)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 100)
blackjack = pygame.font.SysFont('roboto', 70)


# Text objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# Game text display
def game_texts(text, x, y):
    TextSurf, TextEll = text_objects(text, textfont)
    TextEll.center = (x, y)
    gameDisplay.blit(TextSurf, TextEll)

    pygame.display.update()


def game_finish(text, x, y, color):
    TextSurf, TextEll = end_text_objects(text, game_end, color)
    TextEll.center = (x, y)
    gameDisplay.blit(TextSurf, TextEll)
    pygame.display.update()


def black_jack(text, x, y, color):
    TextSurf, TextEll = end_text_objects(text, blackjack, color)
    TextEll.center = (x, y)
    gameDisplay.blit(TextSurf, TextEll)
    pygame.display.update()


# Button display
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.ellipse(gameDisplay, ac, (x, y, w, h), 5)
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.ellipse(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextEll = text_objects(msg, font)
    TextEll.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextEll)


def points(msg, x, y, w, h, rect):
    pygame.draw.ellipse(gameDisplay, rect, (x, y, w, h))
    TextSurf, TextEll = text_objects(msg, font)
    TextEll.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextEll)
