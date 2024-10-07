class game_object():
    children = []
    
    pos = (0, 0)
    rot = 0
    
    def __init__(self):
        self.children = []
        self.pos = (0, 0)
        self.rot = 0
        pass
    def start(self):
        pass
    def update(self, delta_time : float):
        pass
    
    def add_child(self, object):
        self.children.append(object)
        object.start()
    
class camera():
    camera_pos = (0, 0)
    camera_rot = 0