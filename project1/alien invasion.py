import pygame
from pygame.sprite import Group      #for making groups of bullets to manage previous
from settings import Settings                                       #bullets
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    #creating an instance of the defined class using object called p1..
    p1 = Settings()
    screen=pygame.display.set_mode((p1.screen_width,p1.screen_height ))
    pygame.display.set_caption("Alien Invasion")
    p2 = Ship(p1,screen)

    #create a group to store bullets in.
    bullets = Group()

    #management event loop for game...
    while True:
        gf.check_events(p1, screen ,p2,bullets)
        bullets.update()
        p2.update()
        gf.update_screen(p1,screen,p2,bullets)
run_game()
