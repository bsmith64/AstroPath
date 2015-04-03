

# _ _ _ _ _ A S T R O _ P A T H _ _ _ _ _  #
# - - - - - - - - - - - - - - - - - - - - -#


# Written by Blake Smith
# This is a Pygame experiment and a learn as I go type of thing.
# AstroPath is modeled after the arcade game Raiden.

import pygame
import random

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


# # # # # # # # # - - CLASSES - - # # # # # # # # #

class Block(pygame.sprite.Sprite):

        def __init__(self,color):
                # Init the parent class
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('astroid-1.png')
                self.rect = self.image.get_rect()



                #self.image = pygame.Surface((50,50)).convert()
                #self.image.fill(pygame.Color("white"))
                #self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('starshipOne.png')
                self.rect = self.image.get_rect()
                

                #self.image = pygame.Surface((50,50)).convert()
                #self.image.fill(pygame.Color("green"))
                #self.rect = self.image.get_rect()


class Bullet(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self)

                self.image = pygame.Surface([4,10])
                self.image.fill(green)

                self.rect = self.image.get_rect()

        def update(self):
                self.rect.y -= 30




# Initialize Pygame - - - - - - - -
pygame.init()

# Set up screen dimensions - - - - - - - -
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Game title display
pygame.display.set_caption('Astro Path')


# Create SPRITES LIST - - - - - - - - -
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
astroid_trash = pygame.sprite.Group()



# Create the PLAYER - - - - - - - - - -
player = Player()
all_sprites_list.add(player)



# Game paramaters - - - - - - - - - - -
clock = pygame.time.Clock()

x_change = 300
y_change = 400

player.rect.x = x_change
player.rect.y = y_change

points = 0

# Blit SCORE to the screen - - - - - - - - - -
smallFont = pygame.font.SysFont('Charcoal', 25)
mediumFont = pygame.font.SysFont('Charcoal', 30)
largeFont = pygame.font.SysFont('Charcoal', 50)

def score(points):
        text = largeFont.render(str(points), True, green)
        screen.blit(text, [750,510])



# # # # # # # # # # - - MAIN GAME LOOP - - # # # # # # # # #

def gameLoop():

        points = 0
        x_change = 0
        y_change = 0
        movement = 11

        astroid_speed = 10

        # GENERATED THE ASTROIDS - - - - - - - - - - -
        block = Block(black)

        def genRoid():
                
                print ('GENERATION!!!')
                block.rect.x = random.randrange(screen_width * 0.8)
                block.rect.y = -200
                
                all_sprites_list.add(block)
                block_list.add(block)


        genRoid()

        # THE LOOP - - - - - - - - - -
        
        done = False
        while not done:


                

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                                pygame.quit()
                                quit()
                        
                        # MOVEMENT - - - - - - - - - - -
                        if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_LEFT:
                                        x_change -= movement
                                if event.key == pygame.K_RIGHT:
                                        x_change += movement
                                if event.key == pygame.K_UP:
                                        y_change -= movement
                                if event.key == pygame.K_DOWN:
                                        y_change += movement
                        
                        # CONTINUAL MOVEMENT - - - - - - - - - - -
                        if event.type == pygame.KEYUP:

                                if event.key == pygame.K_LEFT:
                                        x_change = 0
                                if event.key == pygame.K_RIGHT:
                                        x_change = 0
                                if event.key == pygame.K_UP:
                                        y_change = 0
                                if event.key == pygame.K_DOWN:
                                        y_change = 0

                        
                        # BULLET FIRE - - - - - - - - - - -
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_s:

                                        bullet = Bullet()

                                        bullet.rect.x = player.rect.x + 38
                                        bullet.rect.y = player.rect.y

                                        all_sprites_list.add(bullet)
                                        bullet_list.add(bullet)


                                

                player.rect.x += x_change
                player.rect.y += y_change
                all_sprites_list.update()



                for bullet in bullet_list:

                        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

                        for block in block_hit_list:
                                bullet_list.remove(bullet)
                                all_sprites_list.remove(bullet)
                                points += 1
                                block_list.remove(block)
                                astroid_trash.add(block)
                                
                                print ('points: ', points)

                        

                        if bullet.rect.y < -10:
                                bullet_list.remove(bullet)
                                all_sprites_list.remove(bullet)

                        

                if block.rect.y > 600:
                        genRoid()
                        print (block.rect.y)
                        block_list.remove(block)
                        all_sprites_list.remove(block)
                        astroid_trash.add(block)

                                

                if len(astroid_trash) == 1 :
                        block.rect.x = random.randrange(screen_width * 0.8)
                        block.rect.y = -200

                        all_sprites_list.add(block)
                        block_list.add(block)
                        astroid_trash.remove(block)

                        

        # Astroid collision detection - - - - - - - - - -

                block_collision_list = pygame.sprite.spritecollide(player, block_list, True)
                
                for block in block_collision_list:
                        block_list.remove(block)
                        all_sprites_list.remove(block)
                        astroid_trash.add(block)
                        done = True


        # END astroid collision test


                block.rect.y += astroid_speed


                


                # GAME BOUNDARIES - - - - - - - - -

                if player.rect.x < 0 or player.rect.x > screen_width - 79:
                        done = True
                        
                if player.rect.y < 0 or player.rect.y > screen_height - 70:
                        done = True
                        





                screen.fill(black)
                score(points)
                
                gui = pygame.image.load('GUI_test.png')
                screen.blit(gui, [0,0])
                
                all_sprites_list.draw(screen)

                pygame.display.update()

                clock.tick(30)

             

gameLoop()
pygame.quit()
quit()
