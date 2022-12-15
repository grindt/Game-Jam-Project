import pygame

import enginey.engine.play as pl
import enginey.engine.actor as ac
import enginey.engine.utility as utl
import enginey.engine.ui as ui
import enginey.engine.enviro as ev

STARTING_LEVEL = 1

pygame.init()

################## Viewer ############################################# 

screen = pygame.display.set_mode([1280, 720])
viewer = pl.make_frame_viewer(screen)
display = pl.make_screen_display_action()
viewer.insert_action(display)

game_content = [ viewer ]

################## game setup ###########################################

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

# map setup
map = ev.make_map()
mapRenderer = ev.make_render_map(40, 22, 1, 32) # screenWidth, screenHeight, offset, tileSize
map.insert_action(mapRenderer)

# needed for frameviewer to render the map
display.insert_entity(map)

# level loader
levelLoader = utl.make_level_loader(STARTING_LEVEL)
levelLoaderAction = utl.make_level_loader_Action()
levelLoader.insert_action(levelLoaderAction)
map.insert_child(levelLoader)


# player setup
player = ac.make_player()
player.insert_action(ac.make_move_action())

# make hud
new_hud = ui.make_hud((10,10))
new_hud.insert_action(ui.make_draw_hud())
player.insert_child(new_hud)

# needed for frameviewer to render the hud
display.insert_entity(new_hud)

#add it to player
#make incrementer for hud
#add it to hud/player

#add player to frame viewer to render hud
display.insert_entity(player)
new_hud.insert_action(ui.make_draw_hud())

# adds player to map once it is fully setup
map.insert_child(player)

# loads first level into memory
levelLoaderAction.act()



# adds map to game_content after it is fully setup
game_content.append(map)

################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()