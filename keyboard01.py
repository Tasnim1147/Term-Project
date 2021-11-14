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


class KeyBoardTask(ShowBase):
    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
        self.squares1 = loader.loadModel("models/square.egg")
        self.squares1.reparentTo(render)
        self.squares1.setPos(0,10,0)
        self.squares1.setColor(0,0,0)
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,-7,10)
        self.camera.setHpr(0,-30,0)
        
        
game = KeyBoardTask()
game.run()
