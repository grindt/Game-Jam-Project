class HUD():
    def __init__(self, location=(0,0), name="HUD"):
        self.actions = []
        self.location = location
        self.name = name
        self.verbose = False
        self.active = True
        self.entity_state = None
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a
    
    def insert_child(self, e):
        e.parent = self
        self.children.append(e)
        return e