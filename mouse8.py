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

def PointAtZ(z, point, vec):
#     print(point + vec * ((z - point.getZ()) / vec.getZ()))
    return point + vec * ((z - point.getZ()) / vec.getZ())


class MouseTask(ShowBase):
    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
        self.squares = []
        
        count = 0
        for index in range(1, 65):
            self.squares += [index]
            
        self.squareRoot = render.attachNewNode("squareRoot")
        
        index = -1
        for x in range(-3,5):
            # going to next row
            for y in range(13,5,-1):
                index += 1
#                 print(index)
                # going throug a constant row
                if count % 2 == 0:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(self.squareRoot)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(0,0,0)
                    
                    count+= 1
                else:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(self.squareRoot)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(255,255,255)
                    count+= 1
                self.squares[index].find("**/polygon").node().setIntoCollideMask(
                    BitMask32.bit(1))
                self.squares[index].find("**/polygon").node().setTag('squares', str(index))
            count+= 1
        
        
        self.pawn = loader.loadModel("models/pawn.egg")
        self.pawn.reparentTo(render)
        self.pawn.setColor(color(0, 0, 255)[0],color(0, 0, 255)[1],color(0, 0, 255)[2])
        self.pawn.setPos(0,10,0)
        self.pawn.setTag("pawns", "1")
        
        self.Handler = CollisionHandlerQueue()
        self.picker = CollisionTraverser()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.Handler)
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0.5,-3,6)
        self.camera.setHpr(0,-30,0)
        
        self.accept("mouse1", self.movePiece)
        self.accept("mouse1-up", self.movePiece)
        self.taskMgr.add(self.update, "update")
        
        
        
    def mousePressed(self):
        if not mapClicks["mouse1"]:
            mapClicks["mouse1"] = True
        
    def update(self, task):

        # Check to see if we can access the mouse. We need it to do anything
        # else
        if self.mouseWatcherNode.hasMouse():
            # get the mouse position
            mpos = self.mouseWatcherNode.getMouse()
#             print("enter")
            # Set the position of the ray based on the mouse position
            self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                # Gets the point described by pickerRay.getOrigin(), which is relative to
                # camera, relative instead to render
            nearPoint = render.getRelativePoint(
                camera, self.pickerRay.getOrigin())
            # Same thing with the direction of the ray
            nearVec = render.getRelativeVector(
                camera, self.pickerRay.getDirection())
#             self.pieces[self.dragging].obj.setPos(
#                 PointAtZ(.5, nearPoint, nearVec))

            # Do the actual collision pass (Do it only on the squares for
            # efficiency purposes)
            self.picker.traverse(self.squareRoot)
            if self.Handler.getNumEntries() > 0:
                # if we have hit something, sort the hits so that the closest
                # is first, and highlight that node
                self.Handler.sortEntries()
                print(self.Handler.getEntry(0).getIntoNode().getTag('square'))
#                 i = int(self.Handler.getEntry(0).getIntoNode().getTag('square'))
#                 print(i)

        return Task.cont
    
    def movePiece(self):
        pass
    
    def dragPiece(self):
        self.drag = True
        self.release = False
        
    def releasePiece(self):
        self.drag = False
        self.release = True
        
game = MouseTask()
game.run()








