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
pygame.display.set_caption("Click it!")

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
                    
    x = random.randint(radius, 640-radius)
    y = random.randint(radius, 480-radius)

    # Vykreslíme nový míček (na náhodné pozici z IF) a skóre
    ball = pygame.draw.circle(screen, (0, 0, 255), (x,y), radius)
    score_text = f"Score: {score}"
    score_font = pygame.font.Font(None, 36)
    score_surface = score_font.render(score_text, True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

    return ball

# Vlastnosti pohybujícího se míčku
def moving_ball_prop():
    global speed, ball_pos, ball_radius, difficulty, level
    # nastavení rychlosti míčku
    speed = [round(random.uniform(-0.5, 0.5), 2), round(random.uniform(-0.5, 0.5), 2)]
    # nastavení polohy míčku
    ball_pos = [random.randint(difficulty.get(level), 640-difficulty.get(level)), random.randint(difficulty.get(level), 480-difficulty.get(level))]
    # nastavení průměru míčku
    ball_radius = difficulty.get(level)

# Funkce ke zobrazování POUZE skóre
def show_score(score):
    score_text = f"Score: {score}"
    score_font = pygame.font.Font(None, 36)
    score_surface = score_font.render(score_text, True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

# Funkce k měření času míčku na obrazovce
def ball_time():
    # Čas míčku na obrazovce
    ball_screen_time = pygame.time.get_ticks()
    print(ball_screen_time)

    return ball_screen_time

# Funkce ke zobrazování levelu
def show_level(level):
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

# Čtení maximálního skóre
def time_read():
    min_time = open("min_time.txt", "a")
    min_time.close
    min_time = open("min_time.txt", "r")
    time_saved = min_time.read()
    min_time.close()
    if time_saved == "":
        min_time = open("min_time.txt", "w")
        min_time.write("1000000")
        time_saved = "1000000"
        min_time.close
    return int(time_saved)

# Zápis maximálního skóre
def time_write(new_time):
    min_time = open("min_time.txt", "w")
    min_time.write(str(new_time))
    min_time.close()

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Font pro text
font = pygame.font.Font(None, 60)

# Vytvoření tlačítek
button_play = font.render("Play", True, BLACK)
button_rules = font.render("Rules", True, BLACK)
button_quit = font.render("Exit", True, BLACK)

# Umístění tlačítek
button_play_pos = button_play.get_rect(center=(640 // 2, 480 // 2 - 100))
button_rules_pos = button_rules.get_rect(center=(640 // 2, 480 // 2))
button_quit_pos = button_quit.get_rect(center=(640 // 2, 480 // 2 + 100))

# Hlavní smyčka programu
waiting = True
clock = pygame.time.Clock()
fade_speed = 10
alpha = 0
text = font.render('Click it!', True, BLACK)

while waiting:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if current_time > 3200:
        waiting = False
    
    # zrušení pozadí
    screen.fill(WHITE)

    # nastavení alfa kanálu textu
    if current_time < 1500:
        alpha = int(min(max(0, alpha + fade_speed),255))
    elif current_time < 3000:
        alpha = int(max(0, alpha - fade_speed))

    # nastavení barvy textu
    color = (alpha, alpha, alpha)

    # nastavení barvy textu
    text = font.render('Click it!', True, color)

    # vykreslení textu
    screen.blit(text, (640 // 2 - text.get_width() // 2, 480 // 2 - text.get_height() // 2))

    # obnovování obrazovky
    pygame.display.flip()

    # omezení počtu snímků na 30 za sekundu
    clock.tick(30)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_play_pos.collidepoint(event.pos):
                # Zde hra
                
                # Počáteční skóre
                score = 0
                # Počáteční level
                level = 0
                # Startovní čas
                start_time = pygame.time.get_ticks()

                while level < 2:

                    # Ukaž číslo levelu
                    show_level(level)

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

                while level == 2:

                    # Ukaž číslo levelu
                    show_level(level)
                    
                    # Nastav vlastnosti nového míčku
                    moving_ball_prop()

                    # vyčištění obrazovky
                    screen.fill((255, 255, 255))
                    # vykreslení míčku
                    ball = pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
                    # Vykreslení skóre
                    show_score(score)
                    # aktualizace obrazovky
                    pygame.display.update()

                    # hlavní smyčka programu
                    running = True
                    while running:

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
                                    # Nastav vlastnosti nového míčku
                                    moving_ball_prop()
                                    # 10 bodů --> ukončíme hru
                                    if score >= 10*(level+1):
                                        running = False
                                        level = 3

                        # pohyb míčku
                        ball_pos[0] += speed[0]
                        ball_pos[1] += speed[1]

                        # odrážení míčku od okrajů obrazovky
                        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > 640:
                            speed[0] = -speed[0]
                        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > 480:
                            speed[1] = -speed[1]

                        # vykreslení pozadí
                        screen.fill((255, 255, 255))
                        # vykreslení míčku
                        ball = pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
                        # Vykreslení skóre
                        show_score(score)
                        # aktualizace obrazovky
                        pygame.display.update()

                if score == 30:
                    # Konečný čas
                    ball_screen_time = pygame.time.get_ticks()
                    show_time = ((ball_screen_time - start_time)//1000)
                    

                    # Ulož nové maximální skóre
                    if show_time < time_read():
                        time_write(show_time)
                        new_best = True
                    else:
                        new_best = False
                        
                        

                    waiting = True
                    # Program čeká 3 sekundy
                    while waiting:
                        current_time = pygame.time.get_ticks()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                waiting = False
                        if current_time - ball_screen_time > 3000:
                            waiting = False
                        
                        
                        # Vymažeme předchozí obsah okna
                        screen.fill((255, 255, 255))
                        # Nastavení fontu a velikosti textu
                        font = pygame.font.Font(None, 50)
                        # Nastavení textu na základě levelu
                        text = font.render("Your time: {}s".format(show_time), True, (0, 0, 0))
                        text_rect = text.get_rect()
                        text_rect.center = screen.get_rect().center
                        # Vykreslení textu na obrazovku
                        screen.blit(text, text_rect)

                        if new_best:
                            # nastavení alfa kanálu textu
                            if (current_time - ball_screen_time) < 1500:
                                alpha = int(min(max(0, alpha + fade_speed),255))
                            elif (current_time - ball_screen_time) < 3000:
                                alpha = int(max(0, alpha - fade_speed))

                            # nastavení barvy textu
                            color = (alpha, alpha, alpha)

                            # nastavení barvy textu
                            text = font.render('New best time!', True, color)

                            # vykreslení textu
                            screen.blit(text, (640 // 2 - text.get_width() // 2, 480 // 4 - text.get_height() // 2))

                        # obnovování obrazovky
                        pygame.display.flip()

                        # omezení počtu snímků na 30 za sekundu
                        clock.tick(30)

            elif button_rules_pos.collidepoint(event.pos):
                # Zde pravidla
                pass
            elif button_quit_pos.collidepoint(event.pos):
                pygame.quit()
                quit()

    # Vyplnění pozadí černou barvou
    screen.fill(WHITE)

    # Vykreslení tlačítek
    pygame.draw.rect(screen, GRAY, button_play_pos)
    screen.blit(button_play, button_play_pos)
    pygame.draw.rect(screen, GRAY, button_rules_pos)
    screen.blit(button_rules, button_rules_pos)
    pygame.draw.rect(screen, GRAY, button_quit_pos)
    screen.blit(button_quit, button_quit_pos)

    pygame.display.update()


# ukončení knihovny Pygame
pygame.quit()