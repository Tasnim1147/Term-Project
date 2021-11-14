from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode, GeomNode
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d.core import Lens, OrthographicLens
import sys


class KeyBoardTask(ShowBase):
    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
        self.squares1 = loader.loadModel("models/square.egg")
        self.squares1.reparentTo(render)
        self.squares1.setPos(0,10,0)
        self.squares1.setColor(0,0,0)
        self.squares1.setTag('myObjectTag', '1')
        
        self.squares2 = loader.loadModel("models/square.egg")
        self.squares2.reparentTo(render)
        self.squares2.setPos(1,9,0)
        self.squares2.setColor(1,1,1)
        self.squares2.setTag('myObjectTag', '2')
        
        self.Handler = CollisionHandlerQueue()
        self.picker = CollisionTraverser()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.Handler)
        

        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,10,6)
        self.camera.setHpr(0,-90,0)
        
        self.accept("mouse1", self.mousePressed)
        
    def mousePressed(self):
#         mousePos = self.win.getPointer(0)
#         print(mousePos.getX(), mousePos.getY())
#         pass
        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
        self.pickerRay.setFromLens(self.camNode, x, y)
        print(self.pickerRay)
        self.picker.traverse(render)
        # Assume for simplicity's sake that myHandler is a CollisionHandlerQueue.
        if self.Handler.getNumEntries() > 0:
            # This is so we get the closest object
            self.Handler.sortEntries()
            self.pickedObj = self.Handler.getEntry(0).getIntoNodePath()
            self.pickedObj = self.pickedObj.findNetTag('myObjectTag')
            if not self.pickedObj.isEmpty():
                a = self.pickedObj.getColor()
                print(a)
                if a == (0,0,0,1):
                    self.pickedObj.setColor(1,1,1)
                else:
                    self.pickedObj.setColor(0,0,0)
                self.pickedObj = None
    def update(self, task):
        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
            print(x, y)
        return task.cont
        
game = KeyBoardTask()
game.run()



