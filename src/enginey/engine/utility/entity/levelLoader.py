class LevelLoader():
    def __init__(self, level=0, name="Level Loader"):
        self.actions = []
        self.name = name
        self.level = level
        self.entity_state = None
        self.verbose = False
        self.active = True
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a