import pygame
NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]#used to only render tiles around player to improve performance
PHYSICS_TILES = {"grass", "stone"}#more effiecent to search for values in a set and this determines the type of tiles that require  physics




class Tilemap:
    def __init__(self, solution, tile_size = 16):
        self.solution = solution
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []  #broken into tile map, partitons screen into grid  where tiles can go, and off grid tiles that may not align with grid


        for i in range(10):
            self.tilemap[str(3 + i) + ";10"] = {"type": "grass", "variant" : 1, "pos" : (3 + i, 10)} # tiles are represented in dictionary, contains type, variation  and positioning
            self.tilemap["10;" + str(5 + i)] = {"type": "stone", "variant" : 1, "pos" : (10, 5+ i)}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))#converts pixel position into grid position
        for offset in NEIGHBOUR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0])+ ";" + str(tile_loc[1] + offset[1])#generates tiles around pixel position
            if check_loc in self.tilemap: #prevents tile being generated for empty space
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos): #converts the tiles to have physics
        rects = []
        for tile in self.tiles_around(pos):
            if tile["type"] in PHYSICS_TILES:#esnures that the tile is one that requires physics
                rects.append(pygame.Rect(tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size, self.tile_size, self.tile_size)) #this will create a rectangle around the tile
        return rects


    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile["type"]][tile["variant"]], (tile["pos"]))

            
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.solution.assets[tile["type"]][tile["variant"]], (tile["pos"][0] * self.tile_size, tile["pos"][1] * self.tile_size)) #59:50


       
                    
