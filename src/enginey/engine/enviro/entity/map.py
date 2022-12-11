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
        self.bossAlive = True
        self.numEnemiesAlive = 99
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def insert_child(self, c):
        c.entity_state = self
        self.children.append(c) 
        return c