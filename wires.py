from tiletypes import TileTypes
import pygame

OFFSETS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

class WireNetwork:
    def __init__(self, screen, tile_size) -> None:
        self.screen = screen
        self.tile_size = tile_size
        self.camera = [0, 0]

        self.next_update = []

        self.tilemap = {} #(type , state)
        #self.temp()

        self.shift_connect = False


    def render(self, camera):
        self.camera = camera

        for i in self.tilemap:
            match self.tilemap[i][0]:
                case TileTypes.WIRE_G | TileTypes.WIRE_B:
                    color = "blue" if self.tilemap[i][0] == TileTypes.WIRE_G else "green"
                    self.drawrect(color, i)
                

                case TileTypes.BUTTON:
                    color = "red" if self.tilemap[i][1] == 1 else "grey"
                    self.drawrect(color, i)
                
                case TileTypes.SHIFT_TILE:
                    self.drawrect(self.tilemap[i][1], i)
                
                case _ :
                    self.drawrect("purple", i)

    def drawrect(self, color, pos) -> pygame.Rect:
        pygame.draw.rect(self.screen, color, pygame.Rect(pos[0] * self.tile_size - self.camera[0],
                                                         pos[1] * self.tile_size - self.camera[1],
                                                        self.tile_size, self.tile_size))
    
    def temp(self):
        for i in range(10):
            self.tilemap[(0, i)] = (TileTypes.WIRE_G, 0)
            self.tilemap[(i, 0)] = (TileTypes.WIRE_G, 0)

    def handle_input(self, add_tile: bool, mouse_pos: tuple[int, int], combo_keys, selected : TileTypes):
        if add_tile:
            if "control" in combo_keys:
                if mouse_pos in self.tilemap:
                    if self.tilemap[mouse_pos][0] == TileTypes.BUTTON:
                        self.tilemap[mouse_pos][1] = (self.tilemap[mouse_pos][1] - 1) * -1
                        if mouse_pos not in self.next_update: self.next_update.append(mouse_pos)
            
            elif "shift" in combo_keys:
                if self.shift_connect:
                    polarity = abs(self.shift_connect[0] - mouse_pos[0]) // (self.shift_connect[0] - mouse_pos[0] if self.shift_connect[0] - mouse_pos[0] != 0 else 1)
                    for x in range(abs(self.shift_connect[0] - mouse_pos[0])):
                        self.tilemap[mouse_pos[0] + x * polarity, self.shift_connect[1]] = [TileTypes.WIRE_G, 0]
                    
                    polarity = abs(self.shift_connect[1] - mouse_pos[1] + 1) // (self.shift_connect[1] - mouse_pos[1] if self.shift_connect[1] - mouse_pos[1] != 0 else 1)
                    for y in range(abs(self.shift_connect[1] - mouse_pos[1])):
                        self.tilemap[mouse_pos[0], mouse_pos[1] + y * polarity] = [TileTypes.WIRE_G, 0]    
                else: 
                    
                    self.tilemap[mouse_pos] = [TileTypes.SHIFT_TILE, "orange"]
                    self.shift_connect = (mouse_pos)
                
            else: 
                if self.shift_connect: self.tilemap[self.shift_connect] = [TileTypes.WIRE_G, 0]
                self.shift_connect = False
                self.tilemap[mouse_pos] = [selected, 0]
        
        elif add_tile == False: #add_tile can be None
            if mouse_pos in self.tilemap:
                self.tilemap.pop(mouse_pos)
       
    def update(self):
        next_tilemap = self.tilemap
        for i in self.next_update:
            pass