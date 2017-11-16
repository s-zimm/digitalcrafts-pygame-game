import pygame
import time
import random

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    monster_x = 0
    monster_y = 0
    

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Monster moving right
        def monst_east(e):    
            e += 1
            if e > width:
                e = 0
            return e

        # Monster moving left
        def monst_west(w):    
            w -= 1
            if w < 0:
                w = width
            return w

        # Monster moving south
        def monst_south(s):    
            s += 1
            if s > height:
                s = 0
            return s

        # Monster moving north
        def monst_north(n):
            n -= 1
            if n < 0:
                n = height
            return n

        # Monster randomization
        def rand_move_x(dir1, dir2):
            directs = [dir1, dir2]
            return random.choice(directs)

            
        # Draw Images
        hero_image = pygame.image.load('images/hero.png').convert_alpha()
        monster_image = pygame.image.load('images/monster.png').convert_alpha()


        # Draw background
        background_image = pygame.image.load('images/background.png').convert_alpha()
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (400, 400))
        screen.blit(monster_image, (rand_move_x(monst_east(monster_x), monst_west(monster_x)), monst_north(monster_y)))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
