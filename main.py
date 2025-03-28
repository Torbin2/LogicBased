import pygame
from sys import exit

from input import get_keyboard_input, get_mouse_input
from wires import WireNetwork

pygame.init()

class Game:
    def __init__(self) -> None:
        self.TILE_SIZE = 20
        
        self.screen = pygame.display.set_mode((1600,1200))
        pygame.display.set_caption('LogicBased')
        
        self.wire_network = WireNetwork(color='#b18b67')

        self.camera = [0, 0]

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

            self.camera, combo_keys = get_keyboard_input(self.camera)
            self.mouse_action = get_mouse_input(self.mouse_action, self.TILE_SIZE, self.camera)

            self.wire_network.update(self.mouse_action[0], self.mouse_action[1], combo_keys)

            self.wire_network.render(self.screen, self.TILE_SIZE, self.camera)

            pygame.display.update()
            self.clock.tick(60)


Game().run()
#TODO:wires, logic gates, input, output