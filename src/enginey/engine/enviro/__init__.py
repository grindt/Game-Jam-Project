### 
###  Entities 
### 
 
def make_map():
    import enginey.engine.enviro.entity.map as mp
    return mp.Map()

### 
### Actions 
### 

def make_render_map(screenWidth, screenHeight, offset, tileSize):
    import enginey.engine.enviro.action.RenderMap as mpr
    return mpr.RenderMap(screenWidth, screenHeight, offset, tileSize)