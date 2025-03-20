from tiletypes import TileTypes
import pygame


class WireNetwork:
    def __init__(self, color) -> None:
        self.color = color

        self.tilemap = {} #(type , state)
        self.temp()


    def render(self, screen, tile_size, camera):
        for i in self.tilemap:
            match self.tilemap[i][0]:
                case TileTypes.WIRE:
                    pygame.draw.rect(screen, self.color, pygame.Rect(i[0] * tile_size + camera[0], i[1] * tile_size + camera[1], tile_size, tile_size))

    def temp(self):
        for i in range(10):
            self.tilemap[(0, i)] = (TileTypes.WIRE, 0)
            self.tilemap[(i, 0)] = (TileTypes.WIRE, 0)