# Map entity
# -> 2d array map
# -> boss isAlive boolean
# -> enemies alive number
# -> player entity
# ----> location
# ----> health
# ----> hud entity
# ------> health bar

class Map():
    def __init__(self, name="Map"):
        self.actions = []
        self.name = name
        self.map = []
        self.bossAlive = 0
        self.numEnemiesAlive = 0
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []
        self.activitas = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def insert_child(self, c):
        c.entity_state = self
        self.children.append(c) 
        return c

    def insert_activitas(self, a):
        self.activitas.append(a) 
        return a