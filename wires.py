from tiletypes import TileTypes
import pygame


class WireNetwork:
    def __init__(self, color) -> None:
        self.color = color

        self.tilemap = {}
        self.temp()


    def render(self, screen, TILE_SIZE):
        for i in self.tilemap:
            match self.tilemap[i]:
                case TileTypes.WIRE:
                    pygame.draw(screen, self.color, pygame.Rect(i * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def temp(self):
        for i in range(10):
            self.tilemap[(0, i)] = TileTypes.WIRE
            self.tilemap[(i, 0)] = TileTypes.WIRE