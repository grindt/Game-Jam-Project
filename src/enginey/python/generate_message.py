import pygame

class GenerateMessage():
    def __init__(self, location=(0,0)):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.location = location
        self.name = "display_message"
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
        msgToDisplay = str(self.entity_state.health)

        font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = font.render(msgToDisplay, False, (255, 255, 255))
        screen.blit(text_surface, self.location)
        return