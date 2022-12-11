### 
###  Entities 
### 
 
def make_map():
    import enginey.engine.enviro.entity.map as mp
    return mp.Map()

### 
### Actions 
### 

def make_render_map(screen):
    import enginey.engine.enviro.action.RenderMap as mpr
    return mpr.RenderMap(screen)