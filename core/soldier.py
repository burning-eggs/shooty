import pygame.sprite


class Soldier(pygame.sprite.Sprite):
    def __init__(self, surface, char_type: str, x: int, y: int, scale: int, speed: int):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface
        self.char_type = char_type
        self.speed = speed
        self.direction = 1  # Faces right at startup.
        self.flip = False
        self.animation_list = []
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        temp_list = []

        for i in range(5):
            img = pygame.image.load(f"assets/{self.char_type}/Idle/{i}.png")
            img = pygame.transform.scale(
                img, (int(img.get_width() * scale), int(img.get_height() * scale))
            )

            temp_list.append(img)

        self.animation_list.append(temp_list)

        temp_list = []

        for i in range(6):
            img = pygame.image.load(f"assets/{self.char_type}/Run/{i}.png")
            img = pygame.transform.scale(
                img, (int(img.get_width() * scale), int(img.get_height() * scale))
            )

            temp_list.append(img)

        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left: bool, moving_right: bool):
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed

            self.flip = True
            self.direction = 0

        if moving_right:
            dx = self.speed

            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        ANIMATION_COOLDOWN = 100

        self.image = self.animation_list[self.action][self.frame_index]

        if (pygame.time.get_ticks() - self.update_time) > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action: int):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        self.surface.blit(
            pygame.transform.flip(self.image, self.flip, False), self.rect
        )
