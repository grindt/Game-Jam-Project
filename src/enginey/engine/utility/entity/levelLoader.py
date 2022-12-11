class LevelLoader():
    def __init__(self, name="Level Loader"):
        self.actions = []
        self.name = name
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a