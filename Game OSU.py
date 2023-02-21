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

# Definování levelů a jejich obtížností
difficulty = {
  0: 50,
  1: 30,
  2: 20
}

# Funkce vykreslování míčku a skóre
def ball_and_score(score, radius):
    # Pozadí okna RGB formát = vymažeme předchozí obsah okna
    screen.fill((255, 255, 255))
                    
    x = random.randint(0, 640)
    y = random.randint(0, 480)

    # Vykreslíme nový míček (na náhodné pozici z IF) a skóre
    ball = pygame.draw.circle(screen, (0, 0, 255), (x,y), radius)
    score_text = f"Score: {score}"
    score_font = pygame.font.Font(None, 36)
    score_surface = score_font.render(score_text, True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

    return ball

# Funkce k měření času míčku na obrazovce
def ball_time():
    # Čas míčku na obrazovce
    ball_screen_time = pygame.time.get_ticks()
    print(ball_screen_time)

    return ball_screen_time

# Počáteční skóre
score = 0
# Počáteční level
level = 0


while level < 3:
    # Vymažeme předchozí obsah okna
    screen.fill((255, 255, 255))

    # Nastavení fontu a velikosti textu
    font = pygame.font.Font(None, 100)

    # Nastavení textu na základě levelu
    text = font.render("Level {}".format(level+1), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = screen.get_rect().center

    # Vykreslení textu na obrazovku
    screen.blit(text, text_rect)

    # Obnovení obrazovky
    pygame.display.flip()

    # Program čeká 1 sekundu
    pygame.time.delay(1000)

    # Nový míček (ihned se připraví na vykreslení - PROČ??)
    ball = ball_and_score(score, difficulty.get(level))
    ball_screen_time = ball_time()
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
                level = 3
            # Stisknut mezerník --> zkontrolujeme, zda míček byl sestřelen
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Získáme souřadnice myši
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Zjistíme, zda se míček a myš překrývají
                if ball.collidepoint((mouse_x, mouse_y)):
                    # +1 bod
                    score += 1
                    # 10 bodů --> ukončíme hru
                    if score >= 10*(level+1):
                        running = False
                    # Jinak nový míček na náhodné pozici
                    else:
                        # Vykreslení míčku a skóre
                        ball = ball_and_score(score, difficulty.get(level))
                        # Měření času míčku na obzarovce
                        ball_screen_time = ball_time()
        
        
        if current_time - ball_screen_time > 1000:
            # Vykreslení míčku a skóre
            ball = ball_and_score(score, difficulty.get(level))
            # Měření času míčku na obzarovce
            ball_screen_time = ball_time()

        # Měření aktuálního času
        current_time = pygame.time.get_ticks()

        # Aktualizace okna
        pygame.display.flip()

        # Neznámý řádek, PŘIČÍTÁ MILISEKUNDY??, 1frame = 17ms
        clock.tick(60)
    
    # Zvýšit level
    level += 1