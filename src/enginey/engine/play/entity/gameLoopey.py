import pygame
from pygame.locals import *
import enginey.engine.play as term

class GameLoopey():
    def __init__(self, game_content):
        self.game_content = game_content
        self.events = None

    def loop(self):
        isPlaying = True
        while isPlaying:
            #get events
            self.events = pygame.event.get()

            #handle all active entities
            self.entityHandler(self.game_content)

            #do event handling
            for event in self.events:
                if event.type == pygame.QUIT:
                    isPlaying = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPlaying = False
                    if event.key == pygame.K_w or \
                       event.key == pygame.K_a or \
                       event.key == pygame.K_s or \
                       event.key == pygame.K_d:
                       self.game_content[1].move(event.key)
                    
        term.make_terminate().wait_for_exit()

    def actionHandler(self, action):
        if action.types[0] == "display":
            action.act(self.game_content[0].screen)

        if action.types[0] == "event":
            action.act()

        if action.types[0] == "loop":
            action.act()
        
        if len(action.types) > 1:
            if action.types[1] == "loop":
                action.act()
    
    def entityHandler(self, entities):
        for entity in entities:
            if entity.active:
                for action in entity.actions:
                    self.actionHandler(action)
                if len(entity.children) > 0:
                    self.entityHandler(entity.children)