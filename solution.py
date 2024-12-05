import sys
import pygame  #this imports special functions and procedures that will help contribute to the formation of the solution
from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
class Game: 
    def __init__(self):
        pygame.init() #This will "start up" pygame, giving us access to special functions an procedures
        pygame.display.set_caption("Noor's Game")
        #changes name of window
        self.display = pygame.Surface((320, 420)) #This generates an empty image, everything will be rendered here and then scaled up to the full window  
         #creates window and resolution
        self.clock = pygame.time.Clock() #limits the frames to prevent  the CPU providing too much processing power to the solution

        self.movement = [False, False]

        self.assets = { #storing as a  dictionary means that multiple different assets can be stored together while having their own picture
            "decor": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "large_decor": load_images("tiles/large_decor"),
            "stone": load_images("tiles/stone"),
            "player" : load_image("entities/player.png") 
            } 
        
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))#defining player and size
        self.tilemap = Tilemap(self, tile_size = 16)

        
    def run(self):
        while True: # always running
            self.display.fill((14, 219, 248))#Determines the backgroun of the screen with RGB values
            self.tilemap.render(self.display)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))#This will determine movement in x direction
            self.player.render(self.display)#This will actually show the player on the screen
            
                             
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #have to code what happens if user presses X in the top right
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN: #checks if any keys are being pressed 
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                        self.movement[0] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # allows for both arrow keys or WASD 
                        self.movement[1] = True
                if event.type == pygame.KEYUP: #checks if any keys are being pressed 
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d : 
                        self.movement[0] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                        self.movement[1] = False
                        
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))# this will scale the display to the size of the window to further emphaise the pixel art style
            pygame.display.update() #constantly updating window
            self.clock.tick(60) #limits the frames to 60 in order to prevent  the CPU providing too much processing power to the solution
Game().run()
