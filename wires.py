from tiletypes import TileTypes
import pygame


class WireNetwork:
    def __init__(self, color) -> None:
        self.color = color

        self.tilemap = {} #(type , state)
        self.temp()

        self.shift_connect = False


    def render(self, screen, tile_size, camera):
        for i in self.tilemap:
            match self.tilemap[i][0]:
                case TileTypes.WIRE:
                    pygame.draw.rect(screen, self.color, pygame.Rect(i[0] * tile_size - camera[0], i[1] * tile_size - camera[1], tile_size, tile_size))
                
                case TileTypes.SHIFT_TILE:
                    pygame.draw.rect(screen, self.tilemap[i][1], pygame.Rect(i[0] * tile_size - camera[0], i[1] * tile_size - camera[1], tile_size, tile_size))

    def temp(self):
        for i in range(10):
            self.tilemap[(0, i)] = (TileTypes.WIRE, 0)
            self.tilemap[(i, 0)] = (TileTypes.WIRE, 0)

    def handle_input(self, add_tile: bool, mouse_pos: tuple[int, int], combo_keys):
        if add_tile:
            if "shift" in combo_keys:
                if self.shift_connect:
                    polarity = abs(self.shift_connect[0] - mouse_pos[0]) // (self.shift_connect[0] - mouse_pos[0] if self.shift_connect[0] - mouse_pos[0] != 0 else 1)
                    for x in range(abs(self.shift_connect[0] - mouse_pos[0])):
                        self.tilemap[mouse_pos[0] + x * polarity, self.shift_connect[1]] = (TileTypes.WIRE, 0)
                    
                    polarity = abs(self.shift_connect[1] - mouse_pos[1] + 1) // (self.shift_connect[1] - mouse_pos[1] if self.shift_connect[1] - mouse_pos[1] != 0 else 1)
                    for y in range(abs(self.shift_connect[1] - mouse_pos[1])):
                        self.tilemap[mouse_pos[0], mouse_pos[1] + y * polarity] = (TileTypes.WIRE, 0)

                    
                else: 
                    
                    self.tilemap[mouse_pos] = (TileTypes.SHIFT_TILE, "orange")
                    self.shift_connect = (mouse_pos)
                
            else: 
                self.shift_connect = False
                self.tilemap[mouse_pos] = (TileTypes.WIRE, 0)
        
        elif add_tile == False: #add_tile can be None
            if mouse_pos in self.tilemap:
                self.tilemap.pop(mouse_pos)
        
    def update(self, add_tile: bool, mouse_pos: tuple[int, int], combo_keys):
        self.handle_input(add_tile, mouse_pos, combo_keys)