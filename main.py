import pygame
from sys import exit

from wires import WireNetwork

pygame.init()

class Game:
    def __init__(self) -> None:
        self.TILE_SIZE = 20
        
        self.screen = pygame.display.set_mode((800,400))
        pygame.display.set_caption('LogicBased')
        
        self.green_line = WireNetwork(color=(0, 255, 0))

        self.clock = pygame.time.Clock()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()

            self.green_line.render(self.screen, self.TILE_SIZE)

            pygame.display.update()
            self.clock.tick(60)


Game.run()
#TODO:wires, logic gates, input, output