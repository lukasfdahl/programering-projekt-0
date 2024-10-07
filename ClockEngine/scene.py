import pygame
import numpy
import random
import math
import game_object
import visual_object as vo
import vec2
from GameObjects.player import movable_player

class scene:

    _game_objects : list[game_object.game_object] = []
    camera = game_object.camera()
    render_radius = None

    def __init__(self):
        pygame.init() # Initialize Pygame
    
    def run(self):
        screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
        clock = pygame.time.Clock()
        
        if (self.render_radius == None):
            self.render_radius = vec2.distance((screen.get_width() / 2, screen.get_height() / 2), (0, 0))

        # Make sure the window stays open until the user closes it
        run_flag = True
        while run_flag is True:
            screen.fill((255, 255, 255)) # Fill the screen with white
            delta_time : numpy.float64 = clock.tick() / 1000
            
            for object in self._game_objects:
                self.run_game_object(screen, object, delta_time)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_flag = False
                    
            pygame.display.flip() # Refresh the screen so drawing appears
            
    def add_game_object(self, object : game_object.game_object):
        self._game_objects.append(object)
        object.start()
        
    def run_game_object(self, screen : pygame.Surface, object: game_object.game_object, delta_time : float):
        object.update(delta_time)
            
        for child in object.children:
            self.run_game_object(screen, child, delta_time)
            
        if (issubclass(type(object), vo.visual_object)):
            if (vec2.distance(object.pos, self.camera.camera_pos) < self.render_radius):
                object.render(screen, self.camera.camera_pos, self.camera.camera_rot)

