from scene import scene
from game_object import game_object
from GameObjects.player import movable_player
import visual_object as vo
import math
import datetime

class clock_object(game_object): 
    time_scale = 1
    second_counter = 0
    milisecond_timer = 0

    #setting initial time
    current_time = datetime.datetime.now()
    second_counter = current_time.hour * 3600 + current_time.minute * 60 + current_time.second 
    
    #objects
    text : vo.text = None
    second_pointer : vo.line = None
    minute_pointer : vo.line = None
    hour_pointer : vo.line = None
    
    def __init__(self, pos : tuple[float, float]):
        game_object.__init__(self)
        self.pos = pos
    
    def draw_angled_line(self, point: tuple[float, float], angle : float, length : float, width : float = 1):
        angle_rad = math.radians(angle)
        opposite = length * math.sin(angle_rad)
        adjacent = length * math.cos(angle_rad)
        self.add_child(vo.line((0, 0, 0), point, (point[0] + opposite, point[1] + adjacent), width))

    def draw_angled_line_with_color(self, color: tuple[int, int, int], point: tuple[float, float], angle : float, length : float, width : float = 1):
        angle_rad = math.radians(angle)
        opposite = length * math.sin(angle_rad)
        adjacent = length * math.cos(angle_rad)
        line = vo.line(color, point, (point[0] + opposite, point[1] + adjacent), width)
        self.add_child(line)
        return line

    def get_clock_end_point(self, point : tuple[float, float], angle: float, length: int):
        angle_rad = math.radians(angle)
        opposite = length * math.sin(angle_rad)
        adjacent = length * math.cos(angle_rad)
        return (point[0] + opposite, point[1] + adjacent)

    def set_clock_text(self):
        hours = math.floor(self.second_counter / 3600)
        minutes = math.floor((self.second_counter - hours * 3600) / 60)
        seconds = self.second_counter - hours * 3600 - minutes * 60
        
        hours_text = str(hours)
        minutes_text = str(minutes)
        seconds_text = str(seconds)
        
        if hours < 10: hours_text = f"0{hours_text}"
        if minutes < 10: minutes_text = f"0{minutes_text}"
        if seconds < 10: seconds_text = f"0{seconds_text}"
        
        self.text.content = f"{hours_text}:{minutes_text}:{seconds_text}"
    
    def start(self):
        #minute lines
        for i in range(0, 60):
            self.draw_angled_line_with_color((48, 48, 48), self.pos[:], 6 * i, 200)
        self.add_child(vo.circle((255, 255, 255), 180, self.pos))
        
        #hour lines
        for i in range(0, 12):
            self.draw_angled_line(self.pos, 30 * i, 200, 2)
        self.add_child(vo.circle((255, 255, 255), 140, self.pos))
        
        self.add_child(vo.circle((0, 0, 0), 200, self.pos, 4))
        
        #text
        self.text = vo.text(None, "", (0, 0, 0), (self.pos[0], self.pos[1] - 220))
        self.add_child(self.text)
        self.set_clock_text()
        
        self.second_pointer = self.draw_angled_line_with_color((211, 100, 88), self.pos, (self.second_counter + 30) * -6, 185, 4)
        self.minute_pointer = self.draw_angled_line_with_color((82, 148, 229), self.pos, ((self.second_counter / 60)) * 6, 170, 4)
        self.hour_pointer = self.draw_angled_line_with_color((91, 181, 81), self.pos, ((self.second_counter / 3600)) * 30, 150, 4)
    
    def update(self, delta_time : float):
        self.milisecond_timer += delta_time * 1000
    
        if (self.milisecond_timer >= (1000 / self.time_scale)):
            self.second_counter += 1
            self.milisecond_timer -= 1000
            
        self.set_clock_text()
        self.second_pointer.point_b = self.get_clock_end_point(self.pos, (self.second_counter) * 6, 185)
        self.minute_pointer.point_b = self.get_clock_end_point(self.pos, ((self.second_counter / 60)) * 6, 170)
        self.hour_pointer.point_b = self.get_clock_end_point(self.pos, ((self.second_counter / 3600)) * 30, 150)

class player_bounds(game_object):
    camera = None
    
    bounds_x = (-640, 640)
    bounds_y = (-480, 480)
    
    def __init__(self):
        game_object.__init__(self)
        
    def update(self, delta_time : float):
        if (self.camera.camera_pos[0] < self.bounds_x[0]): self.camera.camera_pos = (self.bounds_x[1] - 1, self.camera.camera_pos[1])
        if (self.camera.camera_pos[0] > self.bounds_x[1]): self.camera.camera_pos = (self.bounds_x[0] + 1, self.camera.camera_pos[1])
        if (self.camera.camera_pos[1] < self.bounds_y[0]): self.camera.camera_pos = (self.camera.camera_pos[0], self.bounds_y[1] - 1)
        if (self.camera.camera_pos[1] > self.bounds_y[1]): self.camera.camera_pos = (self.camera.camera_pos[0], self.bounds_y[0] + 1)
        
#setup and run scene
clock_scene = scene()
clock_scene.add_game_object(clock_object((0, 0)))

player = movable_player((0, 0, 0), (0, 0), (0, 0), 0)
player.camera = clock_scene.camera
clock_scene.add_game_object(player)
bounds = player_bounds()
bounds.camera = clock_scene.camera
clock_scene.add_game_object(bounds)

clock_scene.render_radius = 1000

clock_scene.run()

