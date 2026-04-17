import pygame
import random
import sys

pygame.init()

# window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# images
bg = pygame.image.load("back.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

target_img = pygame.image.load("greenapple.jpg")
target_img = pygame.transform.scale(target_img, (80, 80))

bad_img = pygame.image.load("redapple.jpg")
bad_img = pygame.transform.scale(bad_img, (80, 80))

# fonts
font = pygame.font.SysFont(None, 48)

# game conditions
score = 0
lives = 1

game_time = 30  # 秒
start_ticks = pygame.time.get_ticks()

# effects
effects = []

# target class
class Target:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 80)
        self.y = random.randint(0, HEIGHT - 80)
        self.is_bad = random.random() < 0.2
        self.timer = 60  # 約1秒

    def update(self):
        self.timer -= 1

    def draw(self):
        if self.is_bad:
            screen.blit(bad_img, (self.x, self.y))
        else:
            screen.blit(target_img, (self.x, self.y))

    def is_clicked(self, pos):
        rect = pygame.Rect(self.x, self.y, 80, 80)
        return rect.collidepoint(pos)

# no deplicate creation
def create_target(existing_targets):
    while True:
        new = Target()
        rect1 = pygame.Rect(new.x, new.y, 80, 80)

        overlap = False
        for t in existing_targets:
            rect2 = pygame.Rect(t.x, t.y, 80, 80)
            if rect1.colliderect(rect2):
                overlap = True
                break

        if not overlap:
            return new

targets = []

# main loop
while True:
    screen.blit(bg, (0, 0))
    # calculate time
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    remaining_time = max(0, int(game_time - seconds))

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for t in targets[:]:
                if t.is_clicked(event.pos):

                    # add effects
                    effects.append([t.x + 40, t.y + 40, 10])

                    if t.is_bad:
                        lives -= 1
                    else:
                        score += 1

                    targets.remove(t)

    # create target painting
    if len(targets) < 3:
        if random.random() < 0.05:
            targets.append(create_target(targets))

    # update & delete
    for t in targets[:]:
        t.update()
        if t.timer <= 0:
            targets.remove(t)

    # draw target painting
    for t in targets:
        t.draw()

    # draw effects
    for e in effects[:]:
        x, y, radius = e

        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius, 2)

        beat_text = font.render("BEAT!!", True, (255, 0, 0))
        screen.blit(beat_text, (x - 50, y - 60))

        e[2] += 3

        if e[2] > 40:
            effects.remove(e)

    # create UI 
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    time_text = font.render(f"Time: {remaining_time}", True, (0, 0, 0))
    screen.blit(time_text, (20, 80))

    lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
    screen.blit(lives_text, (20, 140))

    # judge game finish
    if remaining_time <= 0 or lives <= 0:
        end_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(end_text, (WIDTH // 2 - 150, HEIGHT // 2))

        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
