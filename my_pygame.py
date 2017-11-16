import pygame

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        monster_x = 0
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x += 1
        # Draw Images
        hero_image = pygame.image.load('images/hero.png').convert_alpha()
        monster_image = pygame.image.load('images/monster.png').convert_alpha()


        # Draw background
        background_image = pygame.image.load('images/background.png').convert_alpha()
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (400, 400))
        screen.blit(monster_image, (50, monster_x))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
