import visual_object as vo
import game_object
import vec2
import pygame

class movable_player(vo.square):
    
    camera : game_object.camera = None
    move_speed = 200
    rotation_speed = 1
    
    def update(self, delta_time : float):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.camera.camera_pos = vec2.add(self.camera.camera_pos, vec2.multiply(vec2.rotate_vec(vec2.UP, self.camera.camera_rot), self.move_speed * delta_time))
        if keys[pygame.K_s]:
            self.camera.camera_pos = vec2.add(self.camera.camera_pos, vec2.multiply(vec2.rotate_vec(vec2.DOWN, self.camera.camera_rot), self.move_speed * delta_time))
        if keys[pygame.K_a]:
            self.camera.camera_pos = vec2.add(self.camera.camera_pos, vec2.multiply(vec2.rotate_vec(vec2.LEFT, self.camera.camera_rot), self.move_speed * delta_time))
        if keys[pygame.K_d]:
            self.camera.camera_pos = vec2.add(self.camera.camera_pos, vec2.multiply(vec2.rotate_vec(vec2.RIGHT, self.camera.camera_rot), self.move_speed * delta_time))
        
        if keys[pygame.K_q]:
            self.camera.camera_rot += self.rotation_speed * delta_time
        if keys[pygame.K_e]:
            self.camera.camera_rot -= self.rotation_speed * delta_time
            
        self.pos = self.camera.camera_pos
        self.rot = self.camera.camera_rot