from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
import sys

# Can move 1 thing in one direction

keyMap = {
        "up" : False,
        "down" : False,
        "left": False,
        "right": False
          }

def updateKeyMap(key, state):
    keyMap[key] = state
    


class KeyBoardTask(ShowBase):
    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
    
        
        self.squares1 = loader.loadModel("models/square.egg")
        self.squares1.reparentTo(render)
        self.squares1.setPos(1,10,0)
        self.squares1.setColor(1,1,1)
        
        self.squares2 = loader.loadModel("models/square.egg")
        self.squares2.reparentTo(render)
        self.squares2.setPos(0,10,0)
        self.squares2.setColor(0,0,0)
        
        self.squares3 = loader.loadModel("models/square.egg")
        self.squares3.reparentTo(render)
        self.squares3.setPos(0,9,0)
        self.squares3.setColor(1,1,1)
        
        self.squares4 = loader.loadModel("models/square.egg")
        self.squares4.reparentTo(render)
        self.squares4.setPos(1,9,0)
        self.squares4.setColor(0,0,0)
        
        self.pawn = loader.loadModel("models/pawn.egg")
        self.pawn.reparentTo(render)
        self.pawn.setPos(1,9,0)
        self.pawn.setColor(0.5,0.1,0.5)
        
        self.accept("arrow_left", updateKeyMap, ["left", True])
#         self.accept("arrow_left-up", updateKeyMap, ["left", False])
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,-7,10)
        self.camera.setHpr(0,-30,0)
        
        self.dx = 1
        
        self.taskMgr.add(self.update, "update")
        
    def update(self, task):
        pos = self.pawn.getPos()
#         print("entereds")
        if keyMap["left"] == True:
            print("entered")
            pos.x -= self.dx
            keyMap["left"] = False
            
        self.pawn.setPos(pos)
        return task.cont
        

 

        
        
game = KeyBoardTask()
game.run()


