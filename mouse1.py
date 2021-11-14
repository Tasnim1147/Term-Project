from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
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
        

        
        self.taskMgr.add(self.update, "update")
        
        self.accept("mouse1", self.mousePressed)
        
        # Since we are using collision detection to do picking, we set it up like
        # any other collision detection system with a traverser and a handler
#         self.picker = CollisionTraverser()  # Make a traverser
#         self.pq = CollisionHandlerQueue()  # Make a handler
        # Make a collision node for our picker ray
        self.pickerNode = CollisionNode('mouseRay')
        # Attach that node to the camera since the ray will need to be positioned
        # relative to it
#         self.pickerNP = camera.attachNewNode(self.pickerNode)
        # Everything to be picked will use bit 1. This way if we were doing other
        # collision we could separate it
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()  # Make our ray
        # Add it to the collision node
        self.pickerNode.addSolid(self.pickerRay)
        # Register the ray as something that can cause collisions
#         self.picker.addCollider(self.pickerNP, self.pq)
        # self.picker.showCollisions(render)
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,10,6)
        self.camera.setHpr(0,-90,0)
#         self.camLens.setFov(20,60)
#         self.camLens.setNearFar(near_dist, far_dist)
#         lens = OrthographicLens()
#         lens.setFilmSize(20, 15)  # Or whatever is appropriate for your scene
#         self.cam.node().setLens(lens)
    def mousePressed(self):
        mousePos = self.win.getPointer(0)
        print(mousePos.getX(), mousePos.getY())
        pass
        
    def update(self, task):
        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
            self.pickerRay.setFromLens(self.camNode, x, y)
            nearPoint = render.getRelativePoint(
                        camera, self.pickerRay.getOrigin())
            print(nearPoint)
            print(camera)
        return task.cont
        
game = KeyBoardTask()
game.run()

