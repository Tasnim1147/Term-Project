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
    return point + vec * ((z - point.getZ()) / vec.getZ())

def checkPos(p1, p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    z1 = p1.getZ()
    z2 = p2.getZ()
    return abs(x1-x2) <= 0.5 and abs(y1-y2) <= 0.5 


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
                self.squares[index].setTag('squares', str(index))
            count+= 1
        
        
        self.pawn = loader.loadModel("models/pawn.egg")
        self.pawn.reparentTo(render)
        self.pawn.setColor(color(0, 0, 255)[0],color(0, 0, 255)[1],color(0, 0, 255)[2])
        self.pawn.setPos(0,10,0)
        

        self.pickerRay = CollisionRay()
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0.5,-3,6)
        self.camera.setHpr(0,-30,0)
        
        self.accept("mouse1", self.mousePressed)
        self.taskMgr.add(self.update, "update")
        
        self.pieceSelected = None
        self.piece = None
        
        
    def mousePressed(self):
        if self.pieceSelected == None:
            if self.mouseWatcherNode.hasMouse():
                # get the mouse position
                mpos = self.mouseWatcherNode.getMouse()

                # Set the position of the ray based on the mouse position
                self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                
                pointOfRay = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                # Same thing with the direction of the ray
                vectorOfRay = render.getRelativeVector(
                    camera, self.pickerRay.getDirection())
                point = PointAtZ(0.01, pointOfRay, vectorOfRay)
                if checkPos(self.pawn, point):
                    self.piece = self.pawn
                    self.pieceSelected = "Yes"
                    
        elif self.pieceSelected != None:
            if self.mouseWatcherNode.hasMouse():
                # get the mouse position
                mpos = self.mouseWatcherNode.getMouse()

                # Set the position of the ray based on the mouse position
                self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                
                pointOfRay = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                # Same thing with the direction of the ray
                vectorOfRay = render.getRelativeVector(
                    camera, self.pickerRay.getDirection())
                point = PointAtZ(0.01, pointOfRay, vectorOfRay)
                for index in range(64):
                    posOfSq = self.squares[index].getPos()
                    if checkPos(point, posOfSq):
                        self.piece.setPos(posOfSq)
                        self.piece = None
                        self.pieceSelected = None
            
#             print(nearPoint, nearVec)
        
        

    def update(self, task):
        if self.piece != None:
            if self.mouseWatcherNode.hasMouse():
                
                mpos = self.mouseWatcherNode.getMouse()

                # Set the position of the ray based on the mouse position
                self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                
                pointOfRay = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                # Same thing with the direction of the ray
                vectorOfRay = render.getRelativeVector(
                    camera, self.pickerRay.getDirection())
                point = PointAtZ(0.01, pointOfRay, vectorOfRay)
                self.piece.setPos(point)
            
        return Task.cont
    

        
game = MouseTask()
game.run()









