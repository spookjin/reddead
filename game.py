import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_SPEED = 3
HORSE_SPEED = 5

class Character(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

    def update(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Red Dead 2 Lite")
        self.clock = pygame.time.Clock()
        self.player = Character((SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (255, 0, 0))
        self.horse = Character((SCREEN_WIDTH//2+50, SCREEN_HEIGHT//2+50), (139, 69, 19))

    def run(self):
        on_horse = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    if self.player.rect.colliderect(self.horse.rect):
                        on_horse = not on_horse

            keys = pygame.key.get_pressed()
            speed = HORSE_SPEED if on_horse else PLAYER_SPEED
            dx = dy = 0
            if keys[pygame.K_LEFT]:
                dx -= speed
            if keys[pygame.K_RIGHT]:
                dx += speed
            if keys[pygame.K_UP]:
                dy -= speed
            if keys[pygame.K_DOWN]:
                dy += speed

            self.player.update(dx, dy)
            if on_horse:
                self.horse.rect.center = self.player.rect.center

            self.screen.fill((33, 120, 33))
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.horse.image, self.horse.rect)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()
