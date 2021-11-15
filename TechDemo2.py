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


def color(r,g,b): # changes a rgb code into a range between 0 and 1 values 
    return((r/255,g/255,b/255))

def PointAtZ(z, point, vec): # Not my function
    return point + vec * ((z - point.getZ()) / vec.getZ())

# Checks whether two vectors are close enough
def checkPos(p1, p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
#     z1 = p1.getZ()
#     z2 = p2.getZ()
    return abs(x1-x2) <= 0.5 and abs(y1-y2) <= 0.5 

# Main class
class MouseTask(ShowBase):
    def __init__(self):
        
        super().__init__() # Inheriting all the attributes of Showbase class
        
        self.disableMouse()
        
        self.squares = [] # Storing the models of square
        self.pieces = [] # Storing the models of pieces
        
        count = 0
        for index in range(1, 65): # 1 chess board 
            self.squares += [index]
            self.pieces += [index]
            
        
        
        index = -1
        count= 1
        for x in range(-3,5): # Random range of 8 unit gap
            # going to next row
            for y in range(13,5,-1):# Random range of 8 unit gap
                index += 1
                # going through a next column
                if count % 2 == 0:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    # Loading the egg file in a variable
                    self.squares[index].reparentTo(render)
                    # Adding to parent node
                    self.squares[index].setPos(x,y,0)
                    # Setting the location
                    self.squares[index].setColor(0,0,0)
                    # Black color code
                    count+= 1
                else:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(render)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(1, 1, 1)
                    count+= 1
            count+= 1
        
        index = -1
        count= 1
        for x in range(-3,5): # 32 Pieces in 64 squares
            # going to next row
            for y in range(13,5,-1):
                index += 1
                # going throug a constant row
                # PAWN
                if y == 12:
                    self.pieces[index] = loader.loadModel("models/pawn.egg")
                    self.pieces[index].reparentTo(render)
                    self.pieces[index].setPos(x,y,0)
                    self.pieces[index].setColor(1,1,1)
                    
                elif y == 7:
                    self.pieces[index] = loader.loadModel("models/pawn.egg")
                    self.pieces[index].reparentTo(render)
                    self.pieces[index].setPos(x,y,0)
                    self.pieces[index].setColor(color(150, 75, 0)[0],
                                    color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown color
                    
                    # Rook
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
                        self.pieces[index].setColor(color(150, 75, 0)[0],
                                        color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown color
                        # Knight
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
                        self.pieces[index].setColor(color(150, 75, 0)[0],
                            color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown color
                        # Bishop
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
                        self.pieces[index].setColor(color(150, 75, 0)[0],
                                    color(150, 75, 0)[1],color(150, 75, 0)[2])
                        # KIng
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
                        self.pieces[index].setColor(color(150, 75, 0)[0],
                                    color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown color
                        # Queen
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
                        self.pieces[index].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                count+= 1
            count+= 1

        self.pickerRay = CollisionRay() # Instance of the collision ray class
        
        self.setBackgroundColor(color(0,0,125)[0],
                                color(0,125,0)[1],color(0,0,125)[2]) # Any 
        self.camera.setPos(0.5,-5,10)
        # 0.5 along x and -5 along y and 10 along z
        self.camera.setHpr(0,-30,0)
        # Heading 0 degree, pitch -30 and roll 0 degree
        self.setupLights()
        
        self.accept("mouse1", self.mousePressed) # Only left click
        
        self.taskMgr.add(self.update, "update")# Calls the self.update funtion each frame
        
        self.pieceSelected = None
        self.piece = None
        
        
    def mousePressed(self):
        if self.pieceSelected == None: # 1st time left click
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
                    if not isinstance(self.pieces[index], int):
                        # Non objects are filled with integers; requires changes
                        if checkPos(self.pieces[index], point):
                            # Checks for the identical positions
                            self.piece = self.pieces[index] # Storing that piece
                
                            self.pieceSelected = "Yes"
                    
        elif self.pieceSelected != None: # 2nd time left click
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
                # Converts the vectors and points into readable coordinates
                for index in range(64):
                    posOfSq = self.squares[index].getPos()
                    if checkPos(point, posOfSq):
                        self.piece.setPos(posOfSq) # placing the piece
                        self.piece = None
                        self.pieceSelected = None
            
        
    def setupLights(self): # Not my function 
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))

    def update(self, task):  #  moves the piece along with the pointer
        if self.piece != None:
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
                self.piece.setPos(point) # Moving the piece
            
        return Task.cont # For infinite call
    

        
game = MouseTask()
game.run()










