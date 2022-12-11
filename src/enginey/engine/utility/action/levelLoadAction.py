class LevelLoadAction():
    def __init__(self):
        self.types = None
        self.entity_state = None
        self.verbose = False
        self.name = "increment"
        return

    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, screen):
        if self.condition_to_act():
            #do loading
            return self.makeLevel(screen)
        import enginey.engine.enviro as ev
        if self.verbose:
            print(self.name + " for " + self.entity_state.name)
        return

    def makeLevel(self, screen):
        import enginey.engine.enviro as ev
        # Map entity
        # -> 2d array map
        # -> boss isAlive boolean
        # -> enemies alive number
        # -> player entity
        # ----> location
        # ----> health
        # ----> hud entity
        # ------> health bar
        map = ev.make_map()
        mapRenderer = ev.make_render_map(screen)
        map.insert_action(mapRenderer)

        

        self.parseFile(map, self.entity_state.level)


        
        return map

    def parseFile(self, map, level):
        pass