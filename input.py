import pygame



def get_input(camera, previous_mouse):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        camera[1] +=10
    if keys[pygame.K_a]:
        camera[0] +=10
    if keys[pygame.K_s]:
        camera[1] -=10
    if keys[pygame.K_d]:
        camera[0] -=10

    if keys[pygame.K_q]:
        camera[0] +=50
    if keys[pygame.K_e]:
        camera[0] -=50
    
    if keys[pygame.K_SPACE]:
        camera = [0,0]
    
    mouse = pygame.mouse.get_pressed()
    add = None
    if previous_mouse != mouse:
        if mouse[0]:add = True      
        if mouse[2]:add = False

    mouse_action = (add, pygame.mouse.get_pos(), mouse)
    return camera, mouse_action
    
    # def select_crop(keys, selected, plants):
    #     plant_keys = list(plants.keys())
    #     for i in range(9):
    #         key = getattr(pygame, f'K_{i}')  
    #         if keys[key] and len(plant_keys) >= i:
    #             selected = plant_keys[i - 1]  
    #     return selected