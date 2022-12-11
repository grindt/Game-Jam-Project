class RenderMap():
    def __init__(self, screen):
        self.types = ["draw"]
        self.entity_state = None
        self.screen = screen
        self.verbose = False
        self.name = "render_map"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, screen):
        if self.condition_to_act():
            self.draw(screen)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        #draw map
        pass
        return