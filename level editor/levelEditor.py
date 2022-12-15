import pygame
import sys
import os.path
import math
from pathlib import Path
from enum import Enum

SCREENWIDTH = 40
SCREENHEGHT = 22

COLOR_MODIFY = .5

player = (0, 0, 255)
player_hover = (0, 0, 255 * COLOR_MODIFY)
enemy = (255, 128, 0)
enemy_hover = (255 * COLOR_MODIFY, 128 * COLOR_MODIFY, 0)
boss = (255, 0, 0)
boss_hover = (255 * COLOR_MODIFY, 0, 0)
health = (0, 255, 0)
health_hover = (0, 255 * COLOR_MODIFY, 0)
door = (102, 51, 0)
door_hover = (102 * COLOR_MODIFY, 51 * COLOR_MODIFY, 0)
wall = (64, 64, 64)
wall_hover = (64 * COLOR_MODIFY, 64 * COLOR_MODIFY, 64 * COLOR_MODIFY)
floor = (255, 255, 255)
floor_hover = (255 * COLOR_MODIFY, 255 * COLOR_MODIFY, 255 * COLOR_MODIFY)
void = (0, 0, 0)
void_hover = (30, 30, 30)

offset = 1
tile_dimensions = (32 - offset * 2, 32 - offset * 2)

gameMap = []
playerHealth = 0
filenum = 0

def saveMap(userText):
    f = open(filenum, "w")
    for row in range(len(gameMap) - 1):
        for col in range(len(gameMap[0])):
            f.write(gameMap[row][col] + " ")

        f.write("\n")

    if userText == "":
        f.write(playerHealth[0])
    else:
        f.write(userText)
        playerHealth[0] = userText
    f.close()

def blankFile(userText):
    global filenum
    global playerHealth
    filenum = userText

    if not os.path.isfile(filenum):
        f = open(filenum, "w")
        for row in range(SCREENHEGHT):
            for col in range(SCREENWIDTH):
                if row == SCREENHEGHT/2 - 1 and col == SCREENWIDTH / 2 - 1:
                    f.write("f ")
                else:
                    f.write("v ")

            f.write("\n")
        f.write("100")
        f.close()

    with open(filenum, "r") as f:
        for line in f:
            gameMap.append(line.strip().split(' '))
    playerHealth = gameMap[len(gameMap) - 1]
    print(gameMap[len(gameMap) - 1])


def hoverColor(row, col):
    match gameMap[row][col]:
        case "p":
            return player_hover
        case "e":
            return enemy_hover
        case "b":
            return boss_hover
        case "h":
            return health_hover
        case "d":
            return door_hover
        case "w":
            return wall_hover
        case "f":
            return floor_hover
        case "v":
            return void_hover


def getColor(row, col):
    match gameMap[row][col]:
        case "p":
            return player
        case "e":
            return enemy
        case "b":
            return boss
        case "h":
            return health
        case "d":
            return door
        case "w":
            return wall
        case "f":
            return floor
        case "v":
            return void


def getType(keys):
    if keys[pygame.K_p]:
        return "p"
    elif keys[pygame.K_e]:
        return "e"
    elif keys[pygame.K_b]:
        return "b"
    elif keys[pygame.K_h]:
        return "h"
    elif keys[pygame.K_d]:
        return "d"
    elif keys[pygame.K_LSHIFT]:
        return "f"
    else:
        return "w"


def main():
    pygame.init()

    res = (1280, 704)

    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Select a File")

    width = screen.get_width()
    height = screen.get_height()

    input_rect = pygame.Rect(0, 32, 250, 32)
    background_rect = pygame.Rect(0, 0, 250, 32)
    textActive = True
    mapLoaded = False

    base_font = pygame.font.Font(None, 32)
    user_text = ""
    text_type = 3
    TextType = Enum("TextType", ['NONE', 'SAVE', 'NEW'])

    while True:
        mouse = pygame.mouse.get_pos()
        mouseButtons = pygame.mouse.get_pressed()

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_ESCAPE]:
                    pygame.quit()

                if not textActive:
                    if keys[pygame.K_s] and keys[pygame.K_LCTRL]:
                        textActive = True
                        text_type = TextType.SAVE.value
                    if keys[pygame.K_LCTRL] and keys[pygame.K_n]:
                        textActive = True
                        text_type = TextType.NEW.value

                if textActive:
                    if keys[pygame.K_BACKSPACE]:
                        user_text = user_text[:-1]
                    if not keys[pygame.K_LCTRL] and not ev.type == pygame.MOUSEBUTTONDOWN and not keys[pygame.K_BACKSPACE] and not keys[pygame.K_RETURN]:
                        user_text += ev.unicode

                if keys[pygame.K_RETURN]:
                    if text_type == TextType.SAVE.value:
                        saveMap(user_text)
                        pygame.display.set_caption("Currently viewing file " + str(filenum) + ". Health: " + str(playerHealth[0]))
                    
                    if text_type == TextType.NEW.value:
                        global gameMap
                        gameMap = []
                        blankFile(user_text)
                        pygame.display.set_caption("Currently viewing file " + str(filenum) + ". Health: " + str(playerHealth[0]))
                    
                    textActive = False
                    user_text = ""
                    mapLoaded = True
                
            #checks if a mouse is clicked
            if pygame.mouse.get_pressed():
                if mouseButtons == (1, 0, 0):
                    keys = pygame.key.get_pressed()
                    gameMap[math.floor(mouse[1] / 32)][math.floor(mouse[0] / 32)] = getType(keys)

                elif mouseButtons == (0, 0, 1):
                    gameMap[math.floor(mouse[1] / 32)][math.floor(mouse[0] / 32)] = "v"
                    
        # fills the screen with a color
        screen.fill(void)

        if mapLoaded:
            for row in range(0, SCREENHEGHT):
                for col in range(0, SCREENWIDTH):
                    if col * 32 <= mouse[0] <= col * 32 + tile_dimensions[0] and row * 32 <= mouse[1] <= row * 32 + tile_dimensions[1]:
                        pygame.draw.rect(screen, hoverColor(row, col), [(col * 32 + offset), (row * 32 + offset), tile_dimensions[0], tile_dimensions[1]])
                    else:
                        pygame.draw.rect(screen, getColor(row, col), [(col * 32 + offset), (row * 32 + offset), tile_dimensions[0], tile_dimensions[1]])

        if textActive:
            pygame.draw.rect(screen, floor, background_rect)
            pygame.draw.rect(screen, floor, input_rect)
            if text_type == TextType.SAVE.value:
                infoText = "Enter Player Health"
            elif text_type == TextType.NEW.value:
                infoText = "Enter Filename"
            infoSurface = base_font.render(infoText, True, (0, 0, 0))
            text_surface = base_font.render(user_text, True, (0, 0, 0))
            screen.blit(infoSurface, (background_rect.x+5, background_rect.y+5))
            screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        

        # updates the frames of the game
        pygame.display.update()

main()