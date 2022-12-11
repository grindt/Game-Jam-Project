import pygame

import enginey.engine.play as pl
import enginey.engine.actor as ac
import enginey.engine.utility as utl
import enginey.engine.physics as phys

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
# -> player entity
# ----> location
# ----> health
# ----> hud entity
# ------> health bar


# load files






################## Looper #############################################

game_looper = pl.make_game_loop(game_content)
game_looper.loop()