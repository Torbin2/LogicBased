import pygame
from sys import exit

from input import get_input
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

        #bad
        self.mouse_action : list[bool, tuple, tuple] = (None, (0, 0), (0, 0, 0))


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
            self.screen.fill("#678db1")

            self.camera, self.mouse_action = get_input(self.camera, self.mouse_action, self.TILE_SIZE)
            self.wire_network.update(self.mouse_action[0], self.mouse_action[1])

            self.wire_network.render(self.screen, self.TILE_SIZE, self.camera)

            pygame.display.update()
            self.clock.tick(60)


Game().run()
#TODO:wires, logic gates, input, output