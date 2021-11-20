from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32, LPoint3f
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

keyMap = {
        "up" : False,
        "down" : False,
        "left": False,
        "right": False,
         "u": False,
          "d": False,
        "enter":False,
        "space":False}

def updateKeyMap(self):
    self.phase += 1
    
    
class MilleniumChess(ShowBase):
    def __init__(self):
        super().__init__(self)
        
        self.taskMgr.add(self.update, "update")
        self.taskMgr.add(self.change, "change")
        
        self.phase = 1
        self.accept("arrow_right", self.updateKeyMap())
        
    def update(self, task):
        self.change()
        if self.phase == 1:
            self.set_background_color(1,1,1)
        elif self.phase == 2:
            self.set_background_color(0,1,0)
        elif self.phase == 3:
            self.set_background_color(0,0,1)
        task.cont
            
    def change(self):
        if keyMap["Right"]:
            self.phase += 1
            if self.phase <= 3:
                keyMap["Right"] = False
                return 
            elif self.phase > 3:
                self.phase = 1
                keyMap["Right"] = False
                return 
        return 
            
game = MilleniumChess()
game.run()
            
        
        