class LevelLoadAction():
    def __init__(self):
        self.types = None
        self.entity_state = None
        self.verbose = False
        self.name = "load"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self):
        if self.condition_to_act():
            self.makeLevel()
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def makeLevel(self):
        # Map entity
        # -> 2d array map
        # -> boss isAlive boolean
        # -> enemies alive number
        # -> level loader
        # -> player entity
        # ----> location
        # ----> health
        # ----> hud entity
        # ------> health bar

        #accessing the map
        self.entity_state.entity_state.map = []

        self.parseFile(self.entity_state.entity_state, self.entity_state.level)

        self.entity_state.active = False

    def parseFile(self, map, level):
        file = open("./levels/" + str(level),"r")
        lineNum = 0
        for line in file:
            if len(line) < 2:
                map.children[1].health = line
                map.children[1].maxHealth = line
                break
            map.map.append([])
            for char in line:
                if char != ' ':
                    map.map[lineNum].append(char)
            lineNum += 1
        file.close()
        return