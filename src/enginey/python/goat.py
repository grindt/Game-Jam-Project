###################################################################################
#  ____          _    _    _          _____                                       #
# |  _ \        | |  | |  | |        / ____|                                      #
# | |_) |  __ _ | |_ | |_ | |  ___  | (___    __ _  _   _   __ _  _ __  ___  ___  #
# |  _ <  / _` || __|| __|| | / _ \  \___ \  / _` || | | | / _` || '__|/ _ \/ __| #
# | |_) || (_| || |_ | |_ | ||  __/  ____) || (_| || |_| || (_| || |  |  __/\__ \ #
# |____/  \__,_| \__| \__||_| \___| |_____/  \__, | \__,_| \__,_||_|   \___||___/ #
#                                               | |                               #
#                                               |_|                               #
###################################################################################

import pygame

import enginey.engine.play as pl
import enginey.engine.actor as ac
import enginey.engine.utility as utl
import enginey.engine.ui as ui
import enginey.engine.enviro as ev

STARTING_LEVEL = 23

pygame.init()

################## Viewer ############################################# 

screen = pygame.display.set_mode([1280, 720])
viewer = pl.make_frame_viewer(screen)
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [ viewer ]

################## game setup ###########################################

# map setup
map = ev.make_map()
mapRenderer = ev.make_render_map(40, 22, 1, 32) # screenWidth, screenHeight, offset, tileSize
map.insert_action(mapRenderer)

# needed for frameviewer to render the map
display.insert_entity(map)

# level loader setup
levelLoader = utl.make_level_loader(STARTING_LEVEL)
levelLoaderAction = utl.make_level_loader_Action()
levelLoader.insert_action(levelLoaderAction)
levelLoaderActivateAction = utl.make_activate()
levelLoader.insert_activate_object(levelLoaderActivateAction)
map.insert_child(levelLoader)

# activitas is a array for activate methods
map.insert_activitas(levelLoaderActivateAction)

# player setup
player = ac.make_player()
move_action = ac.make_move_action()
player.insert_action(move_action)

# adding move_action to game_content for the key handler
game_content.append(move_action)

# make hud
new_hud = ui.make_hud((10,10))
new_hud.insert_action(ui.make_draw_hud())
player.insert_child(new_hud)

# needed for frameviewer to render the hud
display.insert_entity(new_hud)

# adds player to map once it is fully setup
map.insert_child(player)

# credits
credits = ui.make_hud((0,0))
credits.active = False
credits_game_title = ui.make_draw_credits((60,50), "Battle Squares")
credits_title = ui.make_draw_credits((60,250), "Credits")
credits_name_1 = ui.make_draw_credits((60,310), "Engine Designer: Gage Rindt")
credits_name_2 = ui.make_draw_credits((60,370), "Level Designer: Nicholas Rengier")

credits.insert_action(credits_title)
credits.insert_action(credits_name_1)
credits.insert_action(credits_name_2)
credits.insert_action(credits_game_title)

map.insert_activitas(credits)

display.insert_entity(credits)

# loads first level into memory
levelLoaderAction.act()

# adds map to game_content after it is fully setup
game_content.append(map)

################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()