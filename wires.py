from tiletypes import TileTypes
import pygame

OFFSETS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

class WireNetwork:
    def __init__(self, screen, tile_size) -> None:
        self.screen = screen
        self.tile_size = tile_size
        self.camera = [0, 0]

        self.next_update = []
        self.delete_list = []

        self.tilemap = {} #(type , state)
        #self.temp()

        self.shift_connect = False
        self.WIRE_TYPES = (TileTypes.WIRE_B, TileTypes.WIRE_G)


    def render(self, camera):
        self.camera = camera

        for i in self.tilemap:
            match self.tilemap[i][0]:
                case TileTypes.WIRE_G | TileTypes.WIRE_B:
                    color = [0, 25, 200] if self.tilemap[i][0] == TileTypes.WIRE_B else [0, 200, 25]
                    color[0] += 200 * self.tilemap[i][1]
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
                        self.tilemap[mouse_pos][1] = not self.tilemap[mouse_pos][1]
                        if mouse_pos not in self.next_update: self.next_update.append(mouse_pos)
                    elif self.tilemap[mouse_pos][0] in self.WIRE_TYPES:
                        print(self.tilemap[mouse_pos][1])
            
            elif "shift" in combo_keys:
                if self.shift_connect:
                    polarity = abs(self.shift_connect[0] - mouse_pos[0]) // (self.shift_connect[0] - mouse_pos[0] if self.shift_connect[0] - mouse_pos[0] != 0 else 1)
                    for x in range(abs(self.shift_connect[0] - mouse_pos[0])):
                        self.tilemap[mouse_pos[0] + x * polarity, self.shift_connect[1]] = [TileTypes.WIRE_G, 0]
                    
                    polarity = abs(self.shift_connect[1] - mouse_pos[1] + 1) // (self.shift_connect[1] - mouse_pos[1] if self.shift_connect[1] - mouse_pos[1] != 0 else 1)
                    for y in range(abs(self.shift_connect[1] - mouse_pos[1])):
                        self.tilemap[mouse_pos[0], mouse_pos[1] + y * polarity] = [TileTypes.WIRE_G, False]    
                else:             
                    self.tilemap[mouse_pos] = [TileTypes.SHIFT_TILE, "orange"]
                    self.shift_connect = (mouse_pos)
                
            else: 
                if self.shift_connect: self.tilemap[self.shift_connect] = [TileTypes.WIRE_G, False]
                
                self.shift_connect = False
                self.tilemap[mouse_pos] = [selected, False]
        
        elif add_tile == False: #add_tile can be None
            if mouse_pos in self.tilemap:
                
                self.tilemap[mouse_pos][1] = False
                self.next_update.append(mouse_pos)
                self.delete_list.append(mouse_pos)
       
    def update(self):
        next_tilemap = self.tilemap.copy()

        update = self.next_update.copy()
        self.next_update = []
        if update: print(update)

        for i in update:
            match self.tilemap[i][0]:
                case TileTypes.WIRE_B | TileTypes.WIRE_G:
                    state = False
                    for offset in OFFSETS:
                        try: 
                            if (self.tilemap[i[0] + offset[0], i[1] + offset[1]][1] and 
                                self.tilemap[i[0] + offset[0], i[1] + offset[1]][0] not in self.WIRE_TYPES): 
                                
                                state = True
                        except KeyError: pass
                    
                    for wire in self.check_wire_conections(i, self.tilemap[i][0], state):
                        next_tilemap[wire][1] = state
                    
                case TileTypes.BUTTON:
                    for offset in OFFSETS:
                        try:
                            if self.tilemap[i[0] + offset[0], i[1] + offset[1]][0] != TileTypes.BUTTON:
                                self.next_update.append((i[0] + offset[0], i[1] + offset[1]))  
                        except KeyError: pass

                case _:
                    print(self.tilemap[i], "logic gate")
        
        for tile in self.delete_list: next_tilemap.pop(tile)
        self.delete_list = []
        
        self.tilemap = next_tilemap
        
            

    def check_wire_conections(self, wire_pos, type, state) -> list:
        next_wires = [wire_pos]
        checked_wires = [wire_pos]
        
        while True:
            wires = next_wires
            next_wires = []
            for wire in wires:
                for offset in OFFSETS:
                    if (wire[0] + offset[0], wire[1] + offset[1]) in self.tilemap:
                        tile_pos = (wire[0] + offset[0], wire[1] + offset[1])
                        if self.tilemap[tile_pos][0] == type:
                            if tile_pos not in checked_wires: next_wires.append(tile_pos)
                            checked_wires.append(tile_pos)
                        
                        elif self.tilemap[tile_pos][1] == 1 and self.tilemap[tile_pos][0] not in self.WIRE_TYPES and state == 0:
                            return []
            if next_wires == []:
                return checked_wires
                        

                       