class RenderMap():
    def __init__(self, screenWidth = 40, screenHeight = 22, offset = 1, tileSize = 32):
        self.types = ["draw"]
        self.entity_state = None
        self.verbose = False
        self.SCREENWIDTH = 40
        self.SCREENHEIGHT = 22
        self.offset = 1
        self.tile_dimensions = (tileSize - self.offset * 2, tileSize - self.offset * 2)
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
        import pygame
        # assumes the whole stage is void color already
        for row in range(0, self.SCREENHEIGHT):
            for col in range(0, self.SCREENWIDTH):
                pygame.draw.rect(screen, self.getColor(row, col), [(col * 32 + self.offset), (row * 32 + self.offset), self.tile_dimensions[0], self.tile_dimensions[1]])
        return

    def getColor(self, row, col):
        char = self.entity_state.map[row][col]

        if char == "p":
            #player
            return (0, 0, 255)
        if char == "e":
            #enemy
            return (255, 128, 0)
        if char == "b":
            #boss
            return (255, 0, 0)
        if char == "h":
            #health
            return (0, 255, 0)
        if char == "d":
            #door
            return (102, 51, 0)
        if char == "w":
            #wall
            return (64, 64, 64)
        if char == "f":
            #floor
            return (255, 255, 255)
        if char == "v":
            #void
            return (0, 0, 0)
        if char == "L":
            #void
            return (0, 0, 0)