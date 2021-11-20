from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d.core import TransparencyAttrib,RenderAttrib
import sys


class KeyBoardTask(ShowBase):
    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
        
        
        self.squares1 = loader.loadModel("models/square.egg")
        self.squares1.reparentTo(render)
        self.squares1.setPos(0,10,0)
        self.squares1.setColor(0,0,0)
        
        self.squares2 = loader.loadModel("models/square.egg")
        self.squares2.reparentTo(render)
        self.squares2.setPos(0,10,1)
        self.squares2.setColor(1,0,0)
        self.squares2.setTransparency(TransparencyAttrib.MAlpha)
        self.squares2.setAlphaScale(0.4)



        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,5,10)
        self.camera.setHpr(0,-60,0)
        
        
game = KeyBoardTask()
game.run()

