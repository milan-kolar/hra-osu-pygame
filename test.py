import pygame

# initialize pygame
pygame.init()

# set up window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Example")

# set up font
font = pygame.font.SysFont(None, 50)

# set up text surfaces
text1 = font.render("Move your mouse to the circle!", True, (0, 0, 0))
text2 = font.render("Press spacebar!", True, (0, 0, 0))

# load instructions image
instructions_img = pygame.image.load("instructions.png")

# get the rectangle for the first text surface
text1_rect = text1.get_rect(center=(320, 300))

# get the rectangle for the second text surface
text2_rect = text2.get_rect(center=(320, 340))

# set up button surface and rect
button = font.render("Back", True, (255, 255, 255), (0, 0, 255))
button_rect = button.get_rect(bottomright=(630, 470))

# set up clock
clock = pygame.time.Clock()

# set up game loop
waiting = True
while waiting:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            waiting = False

    # fill screen with white
    screen.fill((255, 255, 255))

    # draw instructions image onto screen
    screen.blit(instructions_img, (80, 70))

    # draw text surfaces onto screen
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)

    # draw button onto screen
    screen.blit(button, button_rect)

    # update the display
    pygame.display.update()

    # set the framerate
    clock.tick(60)

# quit pygame
pygame.quit()