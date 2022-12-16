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
        # catch for if a level cant be loaded
        try:
            file = open("./levels/" + str(level),"r")
        except:
            file = open("./levels/end","r")

        #start file parse
        rowNum = 0
        #go row by row and col by col
        for line in file:
            if len(line) < 4:
                map.children[1].health = line
                map.children[1].maxHealth = line
                break
            #appends new array to 2d array in map
            map.map.append([])
            colNum = 0
            for char in line:
                #ignores any white space
                if char != ' ':
                    map.map[rowNum].append(char)
                    #changes map data for specific entities
                    if char == 'p':
                        map.children[1].location = (rowNum, colNum)
                    if char == 'e':
                        map.numEnemiesAlive += 1
                    if char == 'b':
                        map.bossAlive += 1
                    if char == 'L':
                        map.children[1].children[0].active = False
                        map.active = False
                        map.activitas[1].active = True
                    colNum += 1
            rowNum += 1

        #close file for safety
        file.close()
        return