class HealthBar():
    def __init__(self, health, name="SuccessCounter"):
        self.actions = []
        self.name = name
        self.counter = health
        self.template = None
        self.verbose = False
        self.active = True
        self.children = []

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a) 
        return a