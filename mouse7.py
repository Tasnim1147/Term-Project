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

mapClicks = {"mouse1":False,
             "mouse2":False,
             "mouse3":False}

def color(r,g,b):
    return((r/255,g/255,b/255))


class MouseTask(ShowBase):
    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
        self.squares = []
        
        count = 0
        for index in range(1, 65):
            self.squares += [index]
        
        index = -1
        for x in range(-3,5):
            # going to next row
            for y in range(13,5,-1):
                index += 1
#                 print(index)
                # going throug a constant row
                if count % 2 == 0:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(render)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(0,0,0)
                    self.squares[index].setTag('squares', str(index))
                    count+= 1
                else:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(render)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(255,255,255)
                    self.squares[index].setTag('squares', str(index))
                    count+= 1
            count+= 1
        
        self.Handler = CollisionHandlerQueue()
        self.picker = CollisionTraverser()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.Handler)
        
        self.pawn = loader.loadModel("models/pawn.egg")
        self.pawn.reparentTo(render)
        self.pawn.setColor(color(0, 0, 255)[0],color(0, 0, 255)[1],color(0, 0, 255)[2])
        self.pawn.setPos(0,10,0)
        self.pawn.setTag("pawns", "1")
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0.5,-3,6)
        self.camera.setHpr(0,-30,0)
        
        self.accept("mouse1", self.mousePressed)
        self.taskMgr.add(self.update, "update")
        
        
        
    def mousePressed(self):
        if not mapClicks["mouse1"]:
            mapClicks["mouse1"] = True
        pass
    def update(self, task):
        if base.mouseWatcherNode.hasMouse():
            if mapClicks["mouse1"]:
                print("eyes")
                x = base.mouseWatcherNode.getMouseX()
                y = base.mouseWatcherNode.getMouseY()
                self.pickerRay.setFromLens(self.camNode, x, y)
                self.picker.traverse(render)
                if self.Handler.getNumEntries() > 0:
                    self.Handler.sortEntries()
                    print(self.Handler)
                    self.pickedObj = self.Handler.getEntry(0).getIntoNodePath()
                    self.pickedObj = self.pickedObj.findNetTag('pawns')
                    if not self.pickedObj.isEmpty():
                        self.pickedObj.setX(self.pickedObj.getX()+ 1)
                    
        return task.cont
        
game = MouseTask()
game.run()







