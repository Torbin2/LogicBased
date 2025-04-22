import os
import pygame

from tiletypes import TileTypes

BASE_IMG_PATH = 'assets/'

def load_image(path, tile_size):
    # print(BASE_IMG_PATH + path)
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    img.set_colorkey((0, 0, 1))
    img = pygame.transform.scale(img, (tile_size , tile_size))
    return img

def load_images(tile_size):
    images = {}

    for img_name in sorted(os.listdir(BASE_IMG_PATH)):
        if "button" not in img_name and img_name != "bridge.png":
            images[eval("TileTypes." + img_name.removesuffix(".png").upper())] = load_image(img_name, tile_size)
        else: images[img_name.removesuffix(".png")] = load_image(img_name, tile_size)
    return images