import pygame

class Move():
    def __init__(self):
        self.types = ["physics"]
        self.entity_state = None
        self.verbose = False
        self.name = "move"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, screen):
        if self.condition_to_act():
            #do something
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return