import pygame
import sys
from bullet import Bullet

#---------------------------------

def check_events(p1, screen, p2 ,bullets):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event ,p1, screen, p2, bullets)#calling the check_keydown_event func
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,p2)#same calling..


#---------------------------------breaking down into smaller functions to make it

def check_keydown_events(event, p1 ,screen ,p2, bullets):
    """key when kept pressed down"""
    if event.key == pygame.K_RIGHT:
        p2.moving_right = True
    elif event.key == pygame.K_LEFT:
        p2.moving_left = True
    elif event.key == 32:
        #create new bullet and add it to the group
        new_bullet = Bullet(p1 ,screen , p2 )
        bullets.add(new_bullet)
#---------------------------------

def check_keyup_events(event , p2):
    """works when keys are released up"""
    if event.key == pygame.K_RIGHT:
        p2.moving_right = False
    elif event.key == pygame.K_LEFT:
        p2.moving_left = False
                    
#---------------------------------

def update_screen(p1, screen, p2, bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    screen.fill(p1.bg_color)
    p2.blitme()
    pygame.display.flip() #makes most recent drawn screen..

#---------------------------------
























