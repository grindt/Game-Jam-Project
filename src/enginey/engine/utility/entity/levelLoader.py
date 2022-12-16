class LevelLoader():
    def __init__(self, level=0, name="Level Loader"):
        self.actions = []
        self.name = name
        self.level = level
        self.entity_state = None
        self.verbose = False
        self.active = True
        self.children = []
        self.activate_object = None

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a

    def insert_activate_object(self, a):
        a.entity_state = self
        self.activate_object = a 
        return a