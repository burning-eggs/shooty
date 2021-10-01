import pygame.sprite


class Soldier(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        img = pygame.image.load("assets/player/Idle/0.png")

        self.surface = surface
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        self.surface.blit(self.image, self.rect)
