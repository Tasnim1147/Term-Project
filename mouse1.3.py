from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d.core import Lens, OrthographicLens
import sys


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
        self.pieces = []
        
        count = 0
        for index in range(192):
            self.squares += [index]
            if index < 64:
                self.pieces += [index]
 
        index = -1
        for z in range (-1,2):
            
            count= 1
        
            for x in range(-3,5):
                # going to next row
                for y in range(13,5,-1):
                    index += 1
                    # going throug a constant row
                    if count % 2 == 0:
                        self.squares[index] = loader.loadModel("models/square.egg")
                        self.squares[index].reparentTo(render)
                        self.squares[index].setPos(x-(8 * z),y,abs(z))
                        self.squares[index].setColor(0,0,0)
    #                     count+= 1
                    else:
                        self.squares[index] = loader.loadModel("models/square.egg")
                        self.squares[index].reparentTo(render)
                        self.squares[index].setPos(x-(8 * z),y,abs(z))
                        self.squares[index].setColor(255,255,255)
                        
                    count+= 1
                count += 1
        
        index = -1
        count= 1
        for x in range(-3,5):
            # going to next row
            for y in range(13,5,-1):
                index += 1
                # going throug a constant row
                if y == 12:
                    self.pieces[index] = loader.loadModel("models/pawn.egg")
                    self.pieces[index].reparentTo(render)
                    self.pieces[index].setPos(x,y,0)
                    self.pieces[index].setColor(1,1,1)
                    
                elif y == 7:
                    self.pieces[index] = loader.loadModel("models/pawn.egg")
                    self.pieces[index].reparentTo(render)
                    self.pieces[index].setPos(x,y,0)
                    self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                if (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/rook.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/rook.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/knight.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/knight.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/bishop.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/bishop.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(0, 13), (0,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/king.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/king.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(1, 13), (1,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/queen.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/queen.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                count+= 1
            count+= 1

        self.pickerRay = CollisionRay()
        
        self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],)
        self.camera.setPos(0.5,-5,10)
        self.camera.setHpr(0,-30,0)
        self.setupLights()
        
        self.accept("mouse1", self.mousePressedLeft)
        self.accept("mouse3", self.mousePressedRight)
        self.taskMgr.add(self.update, "update")
        
        self.pieceSelected = None
        self.piece = None
        self.current_z = 0.01
        
        
    def mousePressedLeft(self):
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
                point = PointAtZ(self.current_z, pointOfRay, vectorOfRay)
                if point.getX() > 5 or point.getX() < -3:
                    point.setZ(1)
                for index in range(64):
                    if not isinstance(self.pieces[index], int):
                        if checkPos(self.pieces[index], point):
                            self.piece = self.pieces[index]
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
                point = PointAtZ(0, pointOfRay, vectorOfRay)
                if point.getX() > 5 or point.getX() < -3:
                    point.setZ(1)
                    self.current_z = 1
                else:
                    point.setZ(0)
                    self.current_z = 0
                for index in range(192):
                    posOfSq = self.squares[index].getPos()
                    if checkPos(point, posOfSq):
                        self.piece.setPos(posOfSq)
                        self.piece = None
                        self.pieceSelected = None
                        
        
    def mousePressedRight(self):
        if self.mouseWatcherNode.hasMouse():   
            mpos = self.mouseWatcherNode.getMouse()
            print(mpos)
            if mpos.getX() >= 0.73 and self.camera.getPos() == (0.5, -5, 10):
                self.camera.setPos(8,-5,10)
            elif self.camera.getPos() == (8, -5, 10) and mpos.getX() < -0.73:
                self.camera.setPos(0.5,-5,10)
            elif self.camera.getPos() == (0.5, -5, 10) and mpos.getX() < -0.73:
                self.camera.setPos(-8,-5,10)
            if mpos.getX() >= 0.73 and self.camera.getPos() == (-8, -5, 10):
                self.camera.setPos(0.5, -5, 10)
            
        
    def setupLights(self):  
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))

    def update(self, task):
        if self.piece != None:
            if self.mouseWatcherNode.hasMouse():
                
                mpos = self.mouseWatcherNode.getMouse()
                
#                 print(mpos)


                self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                
                pointOfRay = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                vectorOfRay = render.getRelativeVector(
                    camera, self.pickerRay.getDirection())
                
                point = PointAtZ(self.current_z, pointOfRay, vectorOfRay)
                print(point)
                
                # The shift
                if int(point.getX()) > 4 or int(point.getX()) < -3:
                    point.setZ(1)
#                     mpos.setY(mpos.getY() + 0.1)#
                    self.current_z = 1
#                     self.win.movePointer(0, mpos.getX() , mpos.getY()+0.1)
                elif point.getX() <= 4 and point.getX() >= -3:
                    point.setZ(0)
                    self.current_z = 0.01
                
                self.piece.setPos(point)

                
            
        return Task.cont
    

        
game = MouseTask()
game.run()










