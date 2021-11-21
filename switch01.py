from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32, LPoint3f
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
#####################################
# Perfect two player game
####################################


# Takes any tuple of 3 numbers and returns a tuple of the round of each number
def roundTuple(t):
    # print(t)
    t = tuple(t)
    a = round(t[0])
    b = round(t[1])
    c = round(t[2])
    return (a, b, c)

# Mapping the key Presed
keyMap = {
        "up" : False,
        "down" : False,
        "left": False,
        "right": False,
         "u": False,
          "d": False,
        "enter":False,
        "space":False}

# Changes the above mapping of the keys
def updateKeyMap(key):
    keyMap[key] = True
    
# Checks whether to tupples are equal????
def checkEqTuples(p1,p2):
    return p1 == p2

def convertSq(s):
    s = tuple(s)
    x = 3 + s[0]
    y = 2 + s[1]
    z = 1 + s[2]
    return (x,y,z)
    

# Change the color format
def color(r,g,b):
    return((r/255,g/255,b/255))
class MilleniumChess(ShowBase):
    
    # Forms Board place the pieces
    # And draws the selected (floating) square
    def formBoardAndPieces(self):
        for z in range (-1,2):
            count= 1
            for x in range(-3,5):
                # going to next row
                for y in range(13,5,-1):
                    cord = (x, y+(8 * z), z)
                    # going throug a constant row
                    if count % 2 == 0:
                        square = loader.loadModel("models/square.egg")
                        self.squares[(cord)] = square
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(0,0,0)
                        self.recordColor[(cord)] = (0,0,0)
                        self.pieces[(cord)] = None
                        self.sqCord[square] = cord
    #                     count+= 1
                    else:
                        square = loader.loadModel("models/square.egg")
                        self.squares[(cord)] = square
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(1,1,1)
                        self.recordColor[(cord)] = (1,1,1)
                        self.pieces[(cord)] = None
                        self.sqCord[square] = cord
                    if y == 12 and z != 0  and z != -1:
                        piece = loader.loadModel("models/pawn.egg")
                        self.pieceCord[piece] = cord
                        self.pieces[(cord)] = piece
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(x ,y+(8 * z),(z))
                        self.pieces[(cord)].setColor(1,1,1)
#                         #self.records["lightPawn"] = self.pieces[(cord)]
                        
                    elif y == 7 and z != 0 and z != 1:
                        piece = loader.loadModel("models/pawn.egg")
                        self.pieceCord[piece] = cord
                        self.pieces[(cord)] = piece
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(cord)
                        self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
#                         #self.records["darkPawn"] = self.pieces[(cord)]
                        
                    elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)] and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/rook.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
#                             #self.records["lightRook"] = self.pieces[(cord)]
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/rook.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                            #self.records["darkRook"] = self.pieces[(cord)]
                    elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/knight.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                            #self.records["lightKnight"] = self.pieces[(cord)]
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/knight.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                            #self.records["darkKnight"] = self.pieces[(cord)]
                    elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/bishop.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                            #self.records["lightBishop"] = self.pieces[(cord)]
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/bishop.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                            #self.records["darkBishop"] = self.pieces[(cord)]
                    elif (x, y) in [(0, 13), (0,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/king.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                            self.records["lightKing"] = piece
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/king.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                            self.records["darkKing"] = piece
                    elif (x, y) in [(1, 13), (1,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/queen.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                            #self.records["lightQueen"] = self.pieces[(cord)]
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/queen.egg")
                            self.pieceCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                            #self.records["darkQueen"] = self.pieces[(cord)]
                    count+= 1
                count+= 1
#         print(self.pieces)

    def __init__(self):
        # Inheriting all attributes
        super().__init__()
        # Store variables
        self.squares = {}
        self.pieces = {}
        self.recordColor = {}
        self.sqCord = {}
        self.pieceCord = {}
        # Record the kings by their names
        self.records = {}
        # Just as the name says
        self.formBoardAndPieces()
        
        self.disableMouse() # For camera issues
        
        self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],) # Any
        # For perfect viewing 
        self.camera.setPos(0.5,-20,25)
        self.camera.setHpr(0,-42.5,0)
        
        # Floating square of current location(blue)
        self.square  = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(1, 8, 0.01)
        self.square.setColor(0,0,1,1)
        # Test piece
#         self.testPieceWhite = loader.loadModel("models/pawn.egg")
#         self.testPieceWhite.reparentTo(render)
#         self.testPieceWhite.setPos(0, 0, - 10)
#         self.testPieceWhite.setColor(1,1,1)
        # Setupping the lights
        self.setupLights()
        # Accepting the commands
#         self.accept("arrow_left", updateKeyMap, ["left"])
#         self.accept("arrow_right", updateKeyMap, ["right"])
#         self.accept("arrow_up", updateKeyMap, ["up"])
#         self.accept("arrow_down", updateKeyMap, ["down"])
#         self.accept("u", updateKeyMap, ["u"])
#         self.accept("d", updateKeyMap, ["d"] )
        self.accept("enter", updateKeyMap, ["enter"])
        # Updating the required updates
        self.taskMgr.add(self.update, "update")
        # Change in unit
        self.dx = 1
        # Is a piece currently selected?
        self.select = False
        self.turn = 0
        
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
        
#         ## print((self.findCords(self.pieces[(1,13,1)]))) # For testing any info

    def update(self, task):
        if keyMap["enter"]:
            print("entters")
            self.switch()
            keyMap["enter"] = False
            self.turn = not(self.turn)
            if self.turn == 0:
                self.camera.setPos(0.5,-20,25)
                self.camera.setHpr(0,-42.5,0)
            else:
    #             self.camera.setPos(0.5,43,38)
    #             self.camera.setHpr(180,-50,0)
                self.camera.setPos(-0.5,39,25)
                self.camera.setHpr(180,-42.5 ,0)
                
        return task.cont
        
    def switch(self):
        for square in list(self.squares.values()):
            square.setZ(square.getZ() * -1)
        for piece in list(self.pieces.values()):
            if piece != None:
                piece.setZ(piece.getZ() * -1)
            
        

 

game = MilleniumChess()
game.run()
