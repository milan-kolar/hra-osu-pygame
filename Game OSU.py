import pygame
import random

# Inicializace
pygame.init()

# Okno hry o velikosti 640x480 pixelů
screen = pygame.display.set_mode((640, 480))

# Titulek
pygame.display.set_caption("Sestřelit míček")

# Pozadí okna RGB formát
screen.fill((255, 255, 255))

# Počáteční skóre
score = 0

# Nový míček (ihned se připraví na vykreslení - PROČ??)
x = random.randint(0, 640)
y = random.randint(0, 480)
# povrch na vykreslení, barva RGB, souřadnice středu, poloměr
ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 50)

# Vykreslení skóre
score_text = f"Score: {score}"
score_font = pygame.font.Font(None, 36)
score_surface = score_font.render(score_text, True, (0, 0, 0))
screen.blit(score_surface, (20, 20))

# Aktualizace okna
pygame.display.flip()

# Hra běží, dokud nezavřeme okno nebo nedosáhneme skóre 10 bodů
running = True
while running:
    # Získáme seznam událostí
    for event in pygame.event.get():
        # Událost == okno zavřeno --> ukončíme hru
        if event.type == pygame.QUIT:
            running = False
        # Stisknut mezerník --> zkontrolujeme, zda míček byl sestřelen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Získáme souřadnice myši
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Zjistíme, zda se míček a myš překrývají
            if ball.collidepoint((mouse_x, mouse_y)):
                # +1 bod
                score += 1
                # 10 bodů --> ukončíme hru
                if score >= 10:
                    running = False
                # Jinak nový míček na náhodné pozici
                else:
                    x = random.randint(0, 640)
                    y = random.randint(0, 480)
    # Pozadí okna RGB formát = vymažeme předchozí obsah okna
    screen.fill((255, 255, 255))

    # Vykreslíme nový míček a skóre
    ball = pygame.draw.circle(screen, (0, 0, 255), (x,y), 50)
    score_text = f"Score: {score}"
    score_font = pygame.font.Font(None, 36)
    score_surface = score_font.render(score_text, True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

     # Aktualizace okna
    pygame.display.flip()