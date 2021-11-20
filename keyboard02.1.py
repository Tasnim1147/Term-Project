from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32, LPoint3f
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

# Takes any tuple of 3 numbers and returns a tuple of the round of each number
def roundTuple(t):
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
                        self.squares[(cord)] = loader.loadModel("models/square.egg")
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(0,0,0)
    #                     count+= 1
                    else:
                        self.squares[(cord)] = loader.loadModel("models/square.egg")
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(1,1,1)
                    if y == 12 and z != 0  and z != -1:
                        self.pieces[(cord)] = loader.loadModel("models/pawn.egg")
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(x ,y+(8 * z),(z))
                        self.pieces[(cord)].setColor(1,1,1)
                        
                    elif y == 7 and z != 0 and z != 1:
                        self.pieces[(cord)] = loader.loadModel("models/pawn.egg")
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(cord)
                        self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                        
                    elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)] and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[(cord)] = loader.loadModel("models/rook.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[(cord)] = loader.loadModel("models/rook.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[(cord)] = loader.loadModel("models/knight.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[(cord)] = loader.loadModel("models/knight.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[(cord)] = loader.loadModel("models/bishop.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[(cord)] = loader.loadModel("models/bishop.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(0, 13), (0,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[(cord)] = loader.loadModel("models/king.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[(cord)] = loader.loadModel("models/king.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(1, 13), (1,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[(cord)] = loader.loadModel("models/queen.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[(cord)] = loader.loadModel("models/queen.egg")
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])    
                    count+= 1
                count+= 1
                
    def check(self, d):
        L = []
        for k in d:
            L += [(d[k], k)]
        return dict(L)
    
    #Takes a piece in path form and returns cords in tuple
    def findCords(self, piece):
        for key in self.pieces:
            if self.pieces[key] == piece:
                return key
        else:
            return False
        
    # Not my function
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
    # Checks whether a square is free or not
    # If True then Free else not free
    def checkFreeSq(self, square):
#         print(square)
#         print(self.pieces)
        if square not in self.pieces:
            return True
        elif square in self.pieces:
            return self.pieces[square] == None
        

    # CALLED every frame
    # Changes the position based on blue sq
    def update(self, task):
        # gets the current position of the blue sq
        posOfSq = self.square.getPos()
        
        # Now start check which button is pressed and change position accordingly
        if keyMap["left"]:
            posOfSq.x -= self.dx
            
            # resetting the values
            keyMap["left"] = False
            
            if posOfSq.x < -3: # restart blue sq from right
                posOfSq.setX(4)

        elif keyMap["right"]:
            posOfSq.x += self.dx
            
            # resetting the values
            keyMap["right"] = False
            
            if posOfSq.x > 4: # restart blue sq from left
                posOfSq.setX(-3)
                
        elif keyMap["up"]:
            
            posOfSq.y += self.dx
            keyMap["up"] = False
            
            if 13 >= posOfSq.y > 5  : # Going to 2nd level in from 1st level
                posOfSq.setZ(0.01)
                
            elif 21 >= posOfSq.y > 13 : # Going to 3 level in from 2nd level
                posOfSq.setZ(1.01)
                
            elif 5 >= posOfSq.y > -2: # Staying in the first level 
                posOfSq.setZ(-0.99)
                
            elif posOfSq.y > 21: # Going back to 1st chess board from 3rd board
                posOfSq.setY(-2)
                posOfSq.setZ(-0.99)
                
        elif keyMap["down"]:
            posOfSq.y -= self.dx
            keyMap["down"] = False
            
            if 13 >= posOfSq.y > 5 :
                posOfSq.setZ(0.01)
                
            elif 21 >= posOfSq.y > 13  :
                posOfSq.setZ(1.01)
                
            elif 5 >= posOfSq.y > -2:
                posOfSq.setZ(-0.99)
                
            elif posOfSq.y < -2:
                posOfSq.setY(21)
                posOfSq.setZ(1.01)
                
        elif keyMap["u"]:
            posOfSq.z += self.dx
            if 0 < posOfSq.z < 1 and -2 <= posOfSq.y <= 5:
                posOfSq.y += 8
            elif 1 < posOfSq.z < 2 and 6 <= posOfSq.y <= 13:
                posOfSq.y += 8
            keyMap["u"] = False
            
        elif keyMap["d"]:
            posOfSq.z -= self.dx
            keyMap["d"] = False
            
        if keyMap["enter"]:
            self.enterPressed(posOfSq)
        elif keyMap["enter"] == False and self.select:
            self.pieces[self.pieceKey].setPos(roundTuple(posOfSq))

            
        self.square.setPos(posOfSq)
        
        return task.cont
    
    def enterPressed(self, posOfSq):
        cord = roundTuple(posOfSq)
        # Check whther the blue sq is empty (self.select == False)
        if self.select == False:
            # Check whther the non blue sq is empty or not
            if self.checkFreeSq(cord):
                keyMap["enter"] = False # Does not do any thing if an empty sq is selected
                return
            elif self.checkFreeSq(cord) == False: # If the square contains something
                self.select = True # Seleect thaat piece
                self.piece = self.pieces[cord] # It would same cord as the posofsq
                self.pieceKey = cord # The key needs to be stored for future ref
                keyMap["enter"] = False # Reset the keymap
                return
        elif self.select: # When we have the piece in our hand and pressed enter
#             if cord not in self.pieces:
            self.pieces[cord] = self.piece # Replacing/ placing the piece
            self.pieces[self.pieceKey] = None # Change the previous place to None
            self.select = False # Now we donot have the piece
            self.piece = None # No piece is selected
            self.pieceKey = None # Then there is no piece key
            keyMap["enter"] = False # Reset the keymap
            return # unnecessary?

            

    
    def __init__(self):
        # Inheriting all attributes
        super().__init__()
        # Store variables
        self.squares = {}
        self.pieces = {}
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
        # Setupping the lights
        self.setupLights()
        # Accepting the commands
        self.accept("arrow_left", updateKeyMap, ["left"])
        self.accept("arrow_right", updateKeyMap, ["right"])
        self.accept("arrow_up", updateKeyMap, ["up"])
        self.accept("arrow_down", updateKeyMap, ["down"])
        self.accept("u", updateKeyMap, ["u"])
        self.accept("d", updateKeyMap, ["d"] )
        self.accept("enter", updateKeyMap, ["enter"])
        # Updating the required updates
        self.taskMgr.add(self.update, "update")
        # Change in unit
        self.dx = 1
        # Is a piece currently selected?
        self.select = False
        
#         print((self.findCords(self.pieces[(1,13,1)]))) # For testing any info
        

 

game = MilleniumChess()
game.run()

