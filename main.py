import pygame
import time

from sys import exit

from input import get_keyboard_input, get_mouse_input
from wires import WireNetwork
from tiletypes import TileTypes

pygame.init()
pygame.display.set_caption('LogicBased')
print("temp: 1/2 = wire, 8=button, 3-7 = logic_gate")

class Game:
    def __init__(self) -> None:
        self.TILE_SIZE: int = 30
        
        self.screen = pygame.display.set_mode((80 * self.TILE_SIZE, 60 * self.TILE_SIZE))
        
        
        self.wire_network = WireNetwork(self.screen, self.TILE_SIZE)

        self.camera = [0, 0]
        self.selected = TileTypes.WIRE_G

        self.clock = pygame.time.Clock()
        
        #input
        self.mouse_action : list[bool, tuple, tuple] = (None, (0, 0), (0, 0, 0))


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
            self.screen.fill("#678db1")
            self.camera, combo_keys, self.selected = get_keyboard_input(self.camera, self.selected, self.clock.get_time())
            self.mouse_action = get_mouse_input(self.mouse_action, self.TILE_SIZE, self.camera)

            self.wire_network.handle_input(self.mouse_action[0], self.mouse_action[1], combo_keys, self.selected)

            self.wire_network.update()

            self.wire_network.render(self.camera)
            
            print(self.clock.get_fps())
            pygame.display.update()
            self.clock.tick(60)

            


Game().run()
#TODO:wires, logic gates, input, output