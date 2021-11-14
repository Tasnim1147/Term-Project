from direct.showbase.ShowBase import *
from direct.task import Task
from direct.showbase import DirectObject
from direct.actor.Actor import Actor
from panda3d.core import LPoint3, LVector3, BitMask32
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
import string

def color(r,g,b):
    return((r/255,g/255,b/255))

def checkColor(piece):
    if piece in string.ascii_uppercase:
        return "brown"
    else:
        return "white"

class ChessBoard(ShowBase):
    def __init__(self): 
        ShowBase.__init__(self)
        self.disableMouse()
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,-7,10)
        self.camera.setHpr(0,-30,0)
        self.allPieces = "RP----prHP----phBP----pbKP----pkQP----pqBP----pbHP----phRP----pr"

        # Since we are using collision detection to do picking, we set it up like
        # any other collision detection system with a traverser and a handler
        self.picker = CollisionTraverser()  # Make a traverser
        self.pq = CollisionHandlerQueue()  # Make a handler
        # Make a collision node for our picker ray
        self.pickerNode = CollisionNode('mouseRay')
        # Attach that node to the camera since the ray will need to be positioned
        # relative to it
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        # Everything to be picked will use bit 1. This way if we were doing other
        # collision we could separate it
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()  # Make our ray
        # Add it to the collision node
        self.pickerNode.addSolid(self.pickerRay)
        # Register the ray as something that can cause collisions
        self.picker.addCollider(self.pickerNP, self.pq)
        # self.picker.showCollisions(render)

        self.setupLights()
        self.drawAllSquare()
        self.drawAllPieces()
        
        
        
    def drawAllSquare(self):
        self.allSquares = dict()
        index = 1
        count = 1
        for row in range(-3,5):
            for col in range(13,5,-1):
                if count % 2 == 0:
                    self.allSquares[index] = Squares(row, col, 0, "white")
                else:
                    self.allSquares[index] = Squares(row, col, 0, "brown")
        
                self.allSquares[index].find("**/polygon").node().setIntoCollideMask(
                    BitMask32.bit(1))
                # Set a tag on the square's node so we can look up what square this is
                # later during the collision pass
                self.allSquares[index].find("**/polygon").node().setTag('square', str(i))

                index += 1
                count += 1
            count += 1
            
    def drawAllPieces(self):
        self.recordPieces = {}
        index = 0
        count = 1
        for row in range(-3,5):
            for col in range(13,5,-1):
                piece = self.allPieces[index]
                if piece != "-":
                    self.recordPieces[(row, col)] = Pieces(row, col, 0, piece)    
                index += 1
                
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
                

        
    
            
class Pieces(object):
    def __init__(self, x, y, z, piece):
        self.x = x
        self.y = y
        self.z = z
        self.piece = piece
        self.color = checkColor(self.piece)
        self.drawPiece()
        
        
    def drawPiece(self):
        if self.piece in "Pp":
            Pawn(self.x, self.y, self.z, self.color)
        elif self.piece in "Hh":
            Knight(self.x, self.y, self.z, self.color)
        elif self.piece in "Kk":
            King(self.x, self.y, self.z, self.color)
            
        elif self.piece in "Qq":
            Queen(self.x, self.y, self.z, self.color)
        elif self.piece in "Rr":
            Rook(self.x, self.y, self.z, self.color)
        elif self.piece in "Bb":
            Bishop(self.x, self.y, self.z, self.color)
        
class Pawn(Pieces):
    def __init__(self, x, y, z, color):
        self.model = loader.loadModel("models/pawn.egg")
        self.x, self.y, self.z, self.color = x, y, z, color
        self.drawPawn()
        
    def drawPawn(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
        elif self.color == "white":
            self.model.setColor(1,1,1)
            
class Rook(Pieces):
    def __init__(self, x, y, z, color):
        self.model = loader.loadModel("models/rook.egg")
        self.x, self.y, self.z, self.color = x, y, z, color
        self.drawRook()
        
    def drawRook(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
        elif self.color == "white":
            self.model.setColor(1,1,1)
            
class Knight(Pieces):
    def __init__(self, x, y, z, color):
        self.model = loader.loadModel("models/knight.egg")
        self.x, self.y, self.z, self.color = x, y, z, color
        self.drawKnight()
        
    def drawKnight(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
        elif self.color == "white":
            self.model.setColor(1,1,1)
            
class Bishop(Pieces):
    def __init__(self, x, y, z, color):
        self.model = loader.loadModel("models/bishop.egg")
        self.x, self.y, self.z, self.color = x, y, z, color
        self.drawBishop()
        
    def drawBishop(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
        elif self.color == "white":
            self.model.setColor(1,1,1)
            
class King(Pieces):
    def __init__(self, x, y, z, color):
        self.model = loader.loadModel("models/king.egg")
        self.x, self.y, self.z, self.color = x, y, z, color
        self.drawKing()
        
    def drawKing(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
        elif self.color == "white":
            self.model.setColor(1,1,1)
        
class Queen(Pieces):
    def __init__(self, x, y, z, color):
        self.model = loader.loadModel("models/queen.egg")
        self.x, self.y, self.z, self.color = x, y, z, color
        self.drawQueen()
        
    def drawQueen(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
        elif self.color == "white":
            self.model.setColor(1,1,1)
        

        
class Squares(object):
    def __init__(self, x, y, z, color):
        
        self.model = loader.loadModel("models/square.egg")
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.drawSquare()
        
    def drawSquare(self):
        self.model.reparentTo(render)
        self.model.setPos(self.x, self.y, self.z)
        if self.color == "brown":
            self.model.setColor(0,0,0)
        elif self.color == "white":
            self.model.setColor(1,1,1)
        

        
chess = ChessBoard()
chess.run()
