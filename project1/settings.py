# this class has an instance as p1
class Settings():
    def __init__(self):
        """initialize game settings"""
        self.screen_width = 1200    #setting up default values for screen width
        self.screen_height = 800    #setting up default values for screen height
        self.bg_color = (230,230,223) #setting up default values for bg_color
        self.p2_speed_factor = 8.5

        #all about bullet to make it appear in the surface..
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
