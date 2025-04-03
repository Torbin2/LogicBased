import pygame

from tiletypes import TileTypes
# import timeit


def get_keyboard_input(camera, selected):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        camera[1] -=20
    if keys[pygame.K_a]:
        camera[0] -=20
    if keys[pygame.K_s]:
        camera[1] +=20
    if keys[pygame.K_d]:
        camera[0] +=20

    if keys[pygame.K_q]:
        camera[0] -=50
    if keys[pygame.K_e]:
        camera[0] +=50
    
    if keys[pygame.K_SPACE]:
        camera = [0,0]

    combo_keys = []
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        combo_keys.append("shift")
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        combo_keys.append("control")


    for i in range(9):
        key = getattr(pygame, f'K_{i}')  
        if keys[key]:
            selected = TileTypes(i)

    return camera, combo_keys, selected


def get_mouse_input(previous_mouse, TILE_SIZE, camera):

    x = pygame.mouse.get_pos()
    mouse_pos = ((x[0] + camera[0]) // TILE_SIZE, (x[1] + camera[1])// TILE_SIZE)

    mouse = pygame.mouse.get_pressed()
    add = None
    if previous_mouse[2] != mouse or previous_mouse[1] != mouse_pos:
        if mouse[0]:add = True      
        if mouse[2]:add = False

    mouse_action : list[bool, tuple, tuple] = (add, mouse_pos, mouse) #add or remove, mouse_pos, buttons_pressed
    return mouse_action
    


    # print(timeit.timeit("import pygame;x = (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] + 10)"), "a")
    # print(timeit.timeit("import pygame;x = pygame.mouse.get_pos(); y= (x[0] -10, x[1] + 10)"), "b") #~0.07s faster