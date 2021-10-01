import pygame.sprite


class Soldier(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface
        self.speed = speed

        img = pygame.image.load("assets/player/Idle/0.png")

        self.image = pygame.transform.scale(
            img, (int(img.get_width() * scale), int(img.get_height() * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left: bool, moving_right: bool):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed

        if moving_right:
            dx = self.speed

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.surface.blit(self.image, self.rect)
