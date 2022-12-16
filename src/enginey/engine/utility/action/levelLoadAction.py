class LevelLoadAction():
    def __init__(self):
        self.types = ["event"]
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
        print(self.condition_to_act())
        if self.condition_to_act():
            self.makeLevel()
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def makeLevel(self):
        # reseting the map
        self.entity_state.entity_state.map = []
        self.entity_state.entity_state.bossAlive = False
        self.entity_state.entity_state.numEnemiesAlive = 0


        self.parseFile(self.entity_state.entity_state, self.entity_state.level)

        self.entity_state.active = False

    def parseFile(self, map, level):
        try:
            file = open("./levels/" + str(level),"r")
        except:
            file = open("./levels/end","r")
        rowNum = 0
        for line in file:
            if len(line) < 4:
                map.children[1].health = line
                map.children[1].maxHealth = line
                break
            map.map.append([])
            colNum = 0
            for char in line:
                if char != ' ':
                    map.map[rowNum].append(char)
                    if char == 'p':
                        map.children[1].location = (rowNum, colNum)
                        print(map.children[1].location)
                    if char == 'e':
                        map.numEnemiesAlive += 1
                    if char == 'b':
                        map.bossAlive = True
                    if char == 'L':
                        map.children[1].children[0].active = False
                        map.active = False
                        map.activitas[1].active = True
                    colNum += 1
            rowNum += 1
        file.close()
        return