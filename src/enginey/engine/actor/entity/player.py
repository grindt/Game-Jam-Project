class Player():
    def __init__(self, location=(0,0), health=100, name="player"):
        self.actions = []
        self.location = location
        self.health = health
        self.name = name
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

