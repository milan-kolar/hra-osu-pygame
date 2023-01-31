import pygame
import random

# Inicializace
pygame.init()

# Okno hry o velikosti 640x480 pixelů
screen = pygame.display.set_mode((640, 480))

# Časovač
clock = pygame.time.Clock()
current_time = 0
ball_screen_time = 0

# Titulek
pygame.display.set_caption("Sestřelit míček")

# Funkce vykreslování míčku a skóre
def ball_and_score(score):
    # Pozadí okna RGB formát = vymažeme předchozí obsah okna
    screen.fill((255, 255, 255))
                    
    x = random.randint(0, 640)
    y = random.randint(0, 480)

    # Vykreslíme nový míček (na náhodné pozici z IF) a skóre
    ball = pygame.draw.circle(screen, (0, 0, 255), (x,y), 50)
    score_text = f"Score: {score}"
    score_font = pygame.font.Font(None, 36)
    score_surface = score_font.render(score_text, True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

    return ball

def ball_time():
    # Čas míčku na obrazovce
    ball_screen_time = pygame.time.get_ticks()
    print(ball_screen_time)

    return ball_screen_time

# Pozadí okna RGB formát
screen.fill((255, 255, 255))

# Počáteční skóre
score = 0

# Nový míček (ihned se připraví na vykreslení - PROČ??)
x = random.randint(0, 640)
y = random.randint(0, 480)
# povrch na vykreslení, barva RGB, souřadnice středu, poloměr
ball = pygame.draw.circle(screen, (0, 0, 255), (x, y), 50)

# Čas míčku na obrazovce
ball_screen_time = pygame.time.get_ticks()

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
                    # Pozadí okna RGB formát = vymažeme předchozí obsah okna
                    screen.fill((255, 255, 255))
                    
                    x = random.randint(0, 640)
                    y = random.randint(0, 480)

                    # Vykreslíme nový míček (na náhodné pozici z IF) a skóre
                    ball = pygame.draw.circle(screen, (0, 0, 255), (x,y), 50)
                    score_text = f"Score: {score}"
                    score_font = pygame.font.Font(None, 36)
                    score_surface = score_font.render(score_text, True, (0, 0, 0))
                    screen.blit(score_surface, (20, 20))

                    # Čas míčku na obrazovce
                    ball_screen_time = pygame.time.get_ticks()
                    print(ball_screen_time)
    
    
    if current_time - ball_screen_time > 1000:
        ball = ball_and_score(score)
        ball_screen_time = ball_time()

    # Měření aktuálního času
    current_time = pygame.time.get_ticks()

     # Aktualizace okna
    pygame.display.flip()

    # Neznámý řádek, PŘIČÍTÁ MILISEKUNDY??, 1frame = 17ms
    clock.tick(60)