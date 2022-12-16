class Move():
    def __init__(self):
        self.types = ["move"]
        self.entity_state = None
        self.verbose = False
        self.name = "move"
        self.active = False
        return

    def condition_to_act(self):
        if self.active == False:
            return False
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, key):
        if self.condition_to_act():
            self.move(key)
        return

    def move(self, key):
        playerCoords = self.entity_state.location
        map = self.entity_state.entity_state

        import pygame
        adj_tile = ''
        # coords are y,x
        adj_coord = (0,0)
        # get correct offset for adj tile based on button pressed
        if key == pygame.K_w:
            # w key (y-1, x)
            adj_coord = (playerCoords[0] - 1, playerCoords[1])
            adj_tile = map.map[playerCoords[0] - 1][playerCoords[1]]
        elif key == pygame.K_a:
            # a key (y, x-1)
            adj_coord = (playerCoords[0], playerCoords[1] - 1)
            adj_tile = map.map[playerCoords[0]][playerCoords[1] - 1]
        elif key == pygame.K_s:
            # a key (y+1, x)
            adj_coord = (playerCoords[0] + 1, playerCoords[1])
            adj_tile = map.map[playerCoords[0] + 1][playerCoords[1]]
        elif key == pygame.K_d:
            # d key (y, x+1)
            adj_coord = (playerCoords[0], playerCoords[1] + 1)
            adj_tile = map.map[playerCoords[0]][playerCoords[1] + 1]
        else:
            print("Error!!!")
            return

        damage = 0
        if adj_tile == "e":
            #enemy
            damage = -5
            self.entity_state.health = int(self.entity_state.health) + damage
            self.entity_state.entity_state.numEnemiesAlive -= 1
            self.makeMove(adj_coord)
        elif adj_tile == "b":
            #boss
            damage = -10
            if int(self.entity_state.entity_state.numEnemiesAlive) <= 0:
                self.entity_state.health = int(self.entity_state.health) + damage
                self.entity_state.entity_state.bossAlive -= 1
                self.makeMove(adj_coord)
            pass
        elif adj_tile == "h":
            #health
            damage = 15
            # health can go over max health
            self.entity_state.health = int(self.entity_state.health) + damage
            self.makeMove(adj_coord)
        elif adj_tile == "d":
            #door
            #validate all enemies and bosses have been eleminated
            if self.entity_state.entity_state.bossAlive == False and int(self.entity_state.entity_state.numEnemiesAlive) <= 0:
                self.entity_state.entity_state.children[0].level += 1
                self.entity_state.entity_state.activitas[0].act()
        elif adj_tile == "f":
            #floor
            damage = -1
            self.entity_state.health = int(self.entity_state.health) + damage
            self.makeMove(adj_coord)

        # check for death
        if int(self.entity_state.health) <= 0:
            self.entity_state.entity_state.activitas[0].act()

        return

    def makeMove(self, adj_coord):
        #updates all stored positions and p char in the 2d map array
        self.entity_state.playSound()
        self.entity_state.entity_state.map[adj_coord[0]][adj_coord[1]] = "p"
        self.entity_state.entity_state.map[self.entity_state.location[0]][self.entity_state.location[1]] = "f"
        self.entity_state.location = adj_coord
        return