import pygame

class DrawHUDAction():
    def __init__(self):
        self.types = ["draw"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_hud_action"
        return

    def condition_to_act(self):
        if self.entity_state != None:
            return True
        if self.entity_state.active != False:
            return True
        return False

    def act(self, screen, *args):
        if self.condition_to_act():
            self.draw(screen)
            if self.verbose:
                print(self.name + " for " + self.entity_state.name)
        return

    def draw(self, screen):
        msgToDisplay = str(self.entity_state.entity_state.health) + " / " + str(self.entity_state.entity_state.maxHealth)

        pygame.draw.rect(screen, (0,0,0), (self.entity_state.location[0], self.entity_state.location[1], 190, 30) )

        font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = font.render(msgToDisplay, False, (255, 255, 255))
        screen.blit(text_surface, self.entity_state.location)
        return