import pygame

# this class has an instance as p2
class Ship():
    def __init__(self,p1,screen):

        #load the ship image and get its rectangle using (rect)
        self.p1 = p1

        #creating the ship surface

        self.screen = screen
        self.image = pygame.image.load("images/ship.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen.
        self.rect.centerx =  self.screen_rect.centerx
        self.rect.bottom =  self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #moving the ship left and right ie. by setting flag
        self.moving_right= False
        self.moving_left = False


    def update(self):
        """bounds the ship within the rectangle..."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.p1.p2_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.p1.p2_speed_factor
        self.rect.centerx = self.center



    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
