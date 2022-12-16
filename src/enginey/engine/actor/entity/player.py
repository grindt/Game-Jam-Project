class Player():
    def __init__(self, location=(0,0), health=100, name="player"):
        self.actions = []
        self.location = location
        self.health = health
        self.maxHealth = health
        self.name = name
        self.volume = 0.5
        self.file = "../assets/sounds/move_sound.mp3"
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def insert_child(self, c):
        c.entity_state = self
        self.children.append(c) 
        return c

