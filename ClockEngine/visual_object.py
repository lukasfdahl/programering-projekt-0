import pygame
from game_object import game_object
import vec2
import math

class visual_object(game_object):
    def __init__(self):
        game_object.__init__(self)
        
    def render(screen: pygame.Surface, camera_pos: tuple[float, float], camera_rot: float):
        pass

class square(visual_object):
    size = (0, 0)
    color = (0, 0, 0)

    def __init__(self, color: tuple[int, int, int] = (0, 0, 0), size: tuple[float, float] = (10, 10), pos: tuple[float, float] = (0, 0), rot: float = 0):
        visual_object.__init__(self)
        self.color = color
        self.size = size
        self.pos = pos
        self.rot = rot
    
    def render(self, screen: pygame.Surface, camera_pos: tuple[float, float], camera_rot: float):
        corner_point = (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2)
        adjusted_camera_pos = vec2.negate_y(camera_pos)

        #find corner points
        point_bottom_left = corner_point
        point_top_left = (corner_point[0], corner_point[1] + self.size[1])
        point_top_right = vec2.add(corner_point, self.size)
        point_bottom_right = (corner_point[0] + self.size[0], corner_point[1])   
        
        #camera_center = (camera_pos[0] + screen.get_width() / 2, camera_pos[0] + screen.get_height() / 2)
        center = (screen.get_width() / 2, screen.get_height() / 2)
        
        #rotate based on local rotation
        point_bottom_left  = vec2.rotate_point(self.pos, self.rot, point_bottom_left)
        point_top_left  = vec2.rotate_point(self.pos, self.rot, point_top_left)
        point_top_right  = vec2.rotate_point(self.pos, self.rot, point_top_right)
        point_bottom_right  = vec2.rotate_point(self.pos, self.rot, point_bottom_right)
        
        #to flip y-axis
        point_bottom_left = vec2.negate_y(point_bottom_left)
        point_top_left = vec2.negate_y(point_top_left)
        point_top_right = vec2.negate_y(point_top_right)
        point_bottom_right = vec2.negate_y(point_bottom_right)
        
        #rotate based on camera rot
        point_bottom_left  = vec2.rotate_point(adjusted_camera_pos, camera_rot, point_bottom_left)
        point_top_left  = vec2.rotate_point(adjusted_camera_pos, camera_rot, point_top_left)
        point_top_right  = vec2.rotate_point(adjusted_camera_pos, camera_rot, point_top_right)
        point_bottom_right  = vec2.rotate_point(adjusted_camera_pos, camera_rot, point_bottom_right)

        #offest based on center
        point_bottom_left = vec2.add(point_bottom_left, center)
        point_top_left = vec2.add(point_top_left, center)
        point_top_right = vec2.add(point_top_right, center)
        point_bottom_right = vec2.add(point_bottom_right, center)

        #offest based on camera pos
        point_bottom_left = vec2.subtract(point_bottom_left, adjusted_camera_pos)
        point_top_left = vec2.subtract(point_top_left, adjusted_camera_pos)
        point_top_right = vec2.subtract(point_top_right, adjusted_camera_pos)
        point_bottom_right = vec2.subtract(point_bottom_right, adjusted_camera_pos)

        pygame.draw.polygon(screen, self.color, [point_bottom_left, point_top_left, point_top_right, point_bottom_right])
    
class circle(visual_object):
    radius = 0
    color = (0, 0, 0)
    width = 0

    def __init__(self, color: tuple[int, int, int] = (0, 0, 0), radius: float = 25, pos: tuple[float, float] = (0, 0), width : int = 0):
        visual_object.__init__(self)
        self.color = color
        self.radius = radius
        self.pos = pos
        self.width = width
    
    def render(self, screen: pygame.Surface, camera_pos: tuple[float, float], camera_rot: float):
        circle_center = vec2.negate_y(self.pos)
        adjusted_camera_pos = vec2.negate_y(camera_pos)

        center = (screen.get_width() / 2, screen.get_height() / 2)
        
        #rotate based on camera rot
        circle_center  = vec2.rotate_point(adjusted_camera_pos, camera_rot, circle_center)

        #offest based on center
        circle_center = vec2.add(circle_center, center)

        #offest based on camera pos
        circle_center = vec2.subtract(circle_center, adjusted_camera_pos)


        pygame.draw.circle(screen, self.color, circle_center, self.radius, self.width)

class line(visual_object):
    point_a = (0, 0)
    point_b = (0, 0)
    color = (0, 0, 0)
    width = 1

    def __init__(self, color: tuple[int, int, int] = (0, 0, 0), point_a: tuple[float, float] = (0, 0), point_b: tuple[float, float] = (0, 0), width : float = 1):
        visual_object.__init__(self)
        self.color = color
        self.point_a = point_a
        self.point_b = point_b
        self.width = width
        self.pos = vec2.add(vec2.divide(vec2.subtract(point_a, point_b), 2), point_a)
    
    def render(self, screen: pygame.Surface, camera_pos: tuple[float, float], camera_rot: float):
        adjusted_point_a = vec2.negate_y(self.point_a)
        adjusted_point_b = vec2.negate_y(self.point_b)
        adjusted_camera_pos = vec2.negate_y(camera_pos)
        
        #camera_center = (camera_pos[0] + screen.get_width() / 2, camera_pos[0] + screen.get_height() / 2)
        center = (screen.get_width() / 2, screen.get_height() / 2)
        
        #rotate based on camera rot
        adjusted_point_a  = vec2.rotate_point(adjusted_camera_pos, camera_rot, adjusted_point_a)
        adjusted_point_b  = vec2.rotate_point(adjusted_camera_pos, camera_rot, adjusted_point_b)

        #offest based on center
        adjusted_point_a = vec2.add(adjusted_point_a, center)
        adjusted_point_b = vec2.add(adjusted_point_b, center)

        #offest based on camera pos
        adjusted_point_a = vec2.subtract(adjusted_point_a, adjusted_camera_pos)
        adjusted_point_b = vec2.subtract(adjusted_point_b, adjusted_camera_pos)


        pygame.draw.line(screen, self.color, adjusted_point_a, adjusted_point_b, self.width)

class text(visual_object):
    content = ""
    font : pygame.font.Font = None
    color = (0, 0, 0)

    def __init__(self, font : pygame.font.Font, content : str = "", color: tuple[int, int, int] = (0, 0, 0), pos: tuple[float, float] = (0, 0), rot: float = 0):
        visual_object.__init__(self)
        self.color = color
        self.content = content
        self.pos = pos
        self.rot = rot
        
        if (font == None):
            self.font = pygame.font.SysFont(None, 30)
        else:
            self.font = font
    
    def render(self, screen: pygame.Surface, camera_pos: tuple[float, float], camera_rot: float):
        adjusted_camera_pos = vec2.negate_y(camera_pos)
        center = (screen.get_width() / 2, screen.get_height() / 2)
        
        
        center_point = vec2.negate_y(self.pos)
        
        #rotate based on camera rot
        center_point  = vec2.rotate_point(adjusted_camera_pos, camera_rot, center_point)
        
        #offest based on center
        center_point = vec2.add(center_point, center)
        
        #offest based on camera pos
        center_point = vec2.subtract(center_point, adjusted_camera_pos)
        
        
        draw_text = self.font.render(self.content, True, self.color)
        draw_text = pygame.transform.rotate(draw_text, math.degrees(self.rot + vec2.angle_clockwise(vec2.rotate_vec(vec2.UP, self.rot), vec2.rotate_vec(vec2.UP, camera_rot))))
        draw_rect = draw_text.get_rect(center = center_point)
        
        screen.blit(draw_text, draw_rect)