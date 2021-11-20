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

# Can move selecting square in all direction

keyMap = {
        "up" : False,
        "down" : False,
        "left": False,
        "right": False,
         "u": False,
          "d": False}

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
    
        self.square  = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(1,11,0.001)
        self.square.setColor(0,1,1,1)
        
        self.pawn1 = loader.loadModel("models/pawn.egg")
        self.pawn1.reparentTo(render)
        self.pawn1.setPos(1,9,0)
        self.pawn1.setColor(0.5,0.1,0.5)
        
        self.pawn2 = loader.loadModel("models/pawn.egg")
        self.pawn2.reparentTo(render)
        self.pawn2.setPos(0,9,0)
        self.pawn2.setColor(0.5,0.1,0.5)
        
        self.accept("arrow_left", updateKeyMap, ["left", True])
        self.accept("arrow_right", updateKeyMap, ["right", True])
        self.accept("arrow_up", updateKeyMap, ["up", True])
        self.accept("arrow_down", updateKeyMap, ["down", True])
        self.accept("u", updateKeyMap, ["u", True])
        self.accept("d", updateKeyMap, ["d", True])

        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,-7,10)
        self.camera.setHpr(0,-30,0)
        
        self.dx = 1
        
        self.taskMgr.add(self.update, "update")
        
    def update(self, task):
        pos = self.square.getPos()
        if keyMap["left"]:
            pos.x -= self.dx
            keyMap["left"] = False
        elif keyMap["right"]:
            pos.x += self.dx
            keyMap["right"] = False
        elif keyMap["up"]:
            pos.y += self.dx
            keyMap["up"] = False
        elif keyMap["down"]:
            pos.y -= self.dx
            keyMap["down"] = False
        elif keyMap["u"]:
            pos.z += self.dx
            keyMap["u"] = False
        elif keyMap["d"]:
            pos.z -= self.dx
            keyMap["d"] = False
            
        self.square.setPos(pos)
        return task.cont
        

 

        
        
game = KeyBoardTask()
game.run()




