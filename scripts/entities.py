import pygame


class PhysicsEntity:
    def __init__(self, solution, e_type, pos, size): #this allows access to anything in the other file
        self.solution = solution
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.speed = 0.5

    def rect(self): #generates rectangle 
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement =(0, 0)):
        frame_movement = (movement[0] + self.velocity [0], movement[1] + self.velocity[1])  # This creates a vector that represents how much the entity should be moving in the frame, based on how much it is required to move in addition to existing velocity

        print(frame_movement)                                                                                                   
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect() #gives entity a rectangle
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left 
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                self.pos[0] = entity_rect.x
                
        self.pos[1] += frame_movement[1]
        for rect in tilemap.physics_rects_around(self.pos): #checks the rectangle for the tiles with physics and sees if it is colliding with the entity
            if entity_rect.colliderect(rect): #sets the side of the entity that interacts with the tile to the opposite side of the tile to push it back
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top 
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y
        #This updates x and y position

        self.velocity[1] = min(5, self.velocity[1] + 0.1) #adds gravity 


    def render (self, surf):
        surf.blit(self.solution.assets["player"], self.pos)
        
