import pygame

class DrawCredits():
    def __init__(self, location=(0,0), message=""):
        self.types = ["draw"]
        self.message = message
        self.location = location
        self.entity_state = None
        self.verbose = False
        self.name = "draw_hud_action"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, screen, *args):
        if self.condition_to_act():
            self.draw(screen)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        msgToDisplay = self.message

        font = pygame.font.SysFont('Comic Sans MS', 50)
        text_surface = font.render(msgToDisplay, False, (255, 255, 255))
        screen.blit(text_surface, self.location)
        return