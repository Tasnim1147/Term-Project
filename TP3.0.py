    # Running this file will directly start the game 
from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32, LPoint3f, LMatrix4f
from direct.gui.OnscreenText import OnscreenText, TextNode
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task  

# REFERENCE: https://www.panda3d.org/
def PointAtZ(z, point, vec): 
    return point + vec * ((z - point.getZ()) / vec.getZ())

# Takes any tuple of 3 numbers and returns a tuple of the round of each number
def roundTuple(t): 
    t = tuple(t)
    a = round(t[0])
    b = round(t[1])
    c = round(t[2])
    return (a, b, c)

# Mapping the key Presed
keyMap = {
        "up" : False, "down" : False, "left": False, "right": False,
        "u": False, "d": False, "enter":False, "space":False, "m": False} 
        # m is for mouse false for not using mouse and true for using mouse
  
# Checks whether to tupples are equal 
def checkEqTuples(p1,p2):
    return p1 == p2
    

# Change the color format into 0 to 1 range.
def color(r,g,b):
    return((r / 255, g / 255, b / 255))

class MilleniumChess(ShowBase): 
    # Forms Board place the pieces
    # And draws the selected (floating) square
    def formBoardAndPieces(self):
        for z in range (1,-2,-1):
            count= 1
            for x in range(-3,5):
                # going to next row
                for y in range(13,5,-1):
                    cord = (x, y + (8 * z), z)
                    # going throug a constant row
                    if count % 2 == 0:
                        square = loader.loadModel("models/square.egg")
                        self.squares[(cord)] = square
                        self.squares[(cord[0], cord[1], -1 * cord[2])] = square
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(0,0,0)
                        self.recordColor[(cord)] = (0,0,0)
                        self.recordColor[(cord[0], cord[1], -1 * cord[2])] = (0,0,0)
                        self.pieces[(cord)] = None
                        self.pieces[(cord[0], cord[1], -1 * cord[2])] = None
                        self.sCord[square] = cord
                    else:
                        square = loader.loadModel("models/square.egg")
                        self.squares[(cord)] = square
                        self.squares[(cord[0], cord[1], -1 * cord[2])] = square
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(1,1,1)
                        self.recordColor[(cord)] = (1,1,1)
                        self.recordColor[(cord[0], cord[1], -1 * cord[2])] = (1,1,1)
                        self.pieces[(cord)] = None
                        self.pieces[(cord[0], cord[1], -1 * cord[2])] = None
                        self.sCord[square] = cord
                    if y == 12 and z != 0  and z != -1:
                        piece = loader.loadModel("models/pawn.egg")
                        self.pCord[piece] = cord
                        self.pieces[(cord)] = piece
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(x ,y + (8 * z), z)
                        self.pieces[(cord)].setColor(1,1,1) 
                    elif y == 7 and z != 0 and z != 1:
                        piece = loader.loadModel("models/pawn.egg")
                        self.pCord[piece] = cord
                        self.pieces[(cord)] = piece
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(cord)
                        self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                            color(150, 75, 0)[1], color(150, 75, 0)[2]) 
                    elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)] and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/rook.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1) 
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/rook.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2]) 
                    elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/knight.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1)
                            #self.records["lightKnight"] = self.pieces[(cord)]
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/knight.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                        color(150, 75, 0)[1],color(150, 75, 0)[2]) 
                    elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/bishop.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1) 
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/bishop.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                        color(150, 75, 0)[1],color(150, 75, 0)[2]) 
                    elif (x, y) in [(0, 13), (0,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/king.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1) 
                            self.records["lightKing"] = piece
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/king.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2])
                            self.records["darkKing"] = piece
                            
                    elif (x, y) in [(1, 13), (1,6)]and z != 0:
                        if y == 13 and z != -1:
                            piece = loader.loadModel("models/queen.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1,1,1) 
                        elif y == 6 and z != 1:
                            piece = loader.loadModel("models/queen.egg")
                            self.pCord[piece] = cord
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                    color(150, 75, 0)[1],color(150, 75, 0)[2]) 
                    count+= 1
                count+= 1  

        # Floating square (blue)
        self.square  = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(1, 8, 0.01)
        self.square.setColor(0,0,1,1)

    #Takes a piece in path form and returns cords in tuple
    def findCords(self, piece):
        for key in self.pieces:
            if self.pieces[key] == piece:
                return key
        else:
            return False
        
    # REFERENCE: https://www.panda3d.org/
    def setupLights(self):  # This function sets up some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.7, .7, .7, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.5, 0.5, 0.5, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
    # Checks whether a square is free or not 
    # If True then Free else not free
    def checkFreeSq(self, square): 
        if square not in self.pieces:
            return True
        elif square in self.pieces:
            return self.pieces[square] == None
        

    # CALLED every frame
    # Changes the position based on blue sq
    def update(self, task): 
        if self.phase == 2: # Game phase
            # Changing the camera position
            if self.phaseName == "gamePhase": 
                if self.turn == 0:
                    self.camera.setPos(0.5,-20,25)
                    self.camera.setHpr(0,-42.5,0)
                    self.dx = 1
                     # For inverse directional movement
                else: 
                    self.camera.setPos(0.5,39,25)
                    self.camera.setHpr(180,-42.5 ,0)
                    self.dx = -1
                if keyMap["m"]: # Changing the input device
                    self.keyboard = 0
                elif keyMap["m"] == False:
                    self.keyboard = 1
                if self.keyboard:
                    self.updateKeyBoard(task)
                else:
                    self.updateMouse(task)
                if self.state == 0: 
                   self.endGame() # Game over 
        return task.cont

    # Similar to update this function is called every frame and 
    # tracks the pointer.
    def updateMouse(self, task):
        if self.phase == 2 and self.phaseName == "gamePhase": 
            if self.state == 0:
                self.endGame()
            if self.mouseWatcherNode.hasMouse():
                # Get the mouse position
                mpos = self.mouseWatcherNode.getMouse()
                # Set the position of the ray based on the mouse position
                self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                
                pointOfRay = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                # Same thing with the direction of the ray
                vectorOfRay = render.getRelativeVector(
                    camera, self.pickerRay.getDirection())
                self.changeCurrent_Z()
                point = PointAtZ(self.current_z, pointOfRay, vectorOfRay) 
                point = roundTuple(point)
                if point in self.squares:
                    self.square.setPos(point[0], point[1], point[2] + 0.01)
                    if self.piece != None:
                        self.piece.setPos(point)
            if self.state == 0:
                self.endGame()
            elif self.phase == 1:
                return 
        return task.cont

    # Approximating the value of z coord of the mouse pointer
    # within the 3D environment
    def changeCurrent_Z(self):
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
            pointY = roundTuple(point)[1]
            if self.turn == 0:
                if -3 <= pointY <= 5.25:
                    self.current_z = - 0.99
                elif 5.25 < pointY <= 14.25:
                    self.current_z = 0.01
                elif 15 <= pointY <= 23.25:
                    self.current_z = 1.01
            elif self.turn == 1:
                if -3 <= pointY <= 5.25:
                    self.current_z = 1.01
                elif 5.25 < pointY <= 14.25:
                    self.current_z = 0.01
                elif 15 <= pointY <= 23.25:
                    self.current_z = -0.99
                    pass

    # This function is called when right click is done
    # Selects or places or moves squares and pieces
    def mousePressedLeft(self): 
        if self.phase == 2 and self.phaseName == "gamePhase":
            if keyMap["m"] and self.state:
                if self.select == False:
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
                        point = roundTuple(point) 
                        # Check whther the non blue sq is empty or not
                        if self.checkFreeSq(point):
                            return
                        elif self.checkFreeSq(point) == False: # If the square contains something
                            self.piece = self.pieces[point] # It would same point as the posofsq 
                            self.colorOfPiece = roundTuple(self.piece.getColor())
                            if self.turn == 1 and self.colorOfPiece == (1, 1, 1):
                                self.select = True # Seleect thaat piece
                                self.pieceKey = point # The key needs to be stored for future ref
                                self.showMoves() # potential check point for pinned
                            elif self.turn == 0 and self.colorOfPiece != (1, 1, 1):
                                self.select = True # Seleect thaat piece
                                self.pieceKey = point # The key needs to be stored for future ref
                                self.showMoves() # potential check point for pinned
                            else:
                                self.piece = None
                                self.colorOfPiece = None 
                elif self.select :
                    if self.mouseWatcherNode.hasMouse():
                        # get the mouse position
                        mpos = self.mouseWatcherNode.getMouse()

                        # Set the position of the ray based on the mouse position
                        self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
                        
                        pointOfRay = render.getRelativePoint(camera, self.pickerRay.getOrigin())
                        # Same thing with the direction of the ray
                        vectorOfRay = render.getRelativeVector(
                            camera, self.pickerRay.getDirection())
                        point = roundTuple(PointAtZ(self.current_z, pointOfRay, vectorOfRay))
                    if point in self.squares and self.squares[point] != None and \
                        roundTuple(self.squares[point].getColor()) == (0, 1, 0):
                        if point == self.pieceKey:
                            self.piece.setPos(self.pieceKey)
                            self.select = False # Now we donot have the piece
                            self.piece = None # No piece is selected
                            self.pieceKey = None # Then there is no piece key
                            self.reColorSq()
                        else: 
                            if self.pieces[point] != None:
                                self.pCord[self.pieces[point]] = (100, 100, 100)
                                self.pieces[point].setPos(100, 100, 100)
                            if "pawn" in str(self.piece):
                                self.checkPromotion()
                            self.piece.setPos(point)
                            self.pieces[point] = self.piece # Replacing/ placing the piece
                            self.pCord[self.piece] = point
                            if point != self.pieceKey:
                            # If point not in the dictionary 
                            # then the piece will be lost from the dictionary
                                self.pieces[self.pieceKey] = None
                                # Change the previous place to None 
                            self.select = False # Now we donot have the piece 
                            self.piece = None # No piece is selected
                            self.pieceKey = None # Then there is no piece key
                            self.reColorSq() 
                            self.square.setPos(1, 8, 0.01) 
                            self.checkCheckMate()
                            self.switch() 
                    else:
                        self.piece.setPos(self.pieceKey)
                        self.select = False # Now we donot have the piece
                        self.piece = None # No piece is selected
                        self.pieceKey = None #  there is no piece key
                        self.reColorSq()
        elif self.phase == 1 and self.phaseName == "startPhase": 
            self.phase = 2
            if self.mouseWatcherNode.hasMouse():
                # Get the mouse position
                mpos = self.mouseWatcherNode.getMouse() 
                if -0.62 <= mpos.getX() <= - 0.17 and  -0.34 >= mpos.getY() >= -0.5:
                    self.startPhase()
                    self.gamePhase()
                elif 0.2 <= mpos.getX() <=  0.63 and -0.34 >= mpos.getY() >= -0.5:
                    self.startPhase()
                    self.gamePhase()
                    self.switch()
                else:
                    self.phase = 1

    # Promotes a pawn if possible
    def checkPromotion(self):
        if self.colorOfPiece == (1, 1, 1) and self.piece.getY() == -2:
            self.piece.setPos(100, 100, 100)
            self.piece = loader.loadModel("models/queen.egg")
            self.piece.reparentTo(render)
            self.piece.setColor(1, 1, 1)
        elif self.piece.getY() == 21:
            self.piece.setPos(100, 100, 100)
            self.piece = loader.loadModel("models/queen.egg")
            self.piece.reparentTo(render)
            self.piece.setColor(color(150, 75, 0)[0],
                color(150, 75, 0)[1],color(150, 75, 0)[2])

    # Similar to update function is function tracks everything 
    # that done using keyboard
    def updateKeyBoard(self, task): 
        if self.phase == 1: # Nothing can be done in phase 1
            return
        if self.phase == 2 and self.phaseName == "gamePhase":
            if self.state == 0:
                self.endGame()
            if self.turn == 0:
                self.camera.setPos(0.5,-20,12)
                self.camera.setHpr(0,-22.5,0)
                self.dx = 1
            else: 
                self.camera.setPos(0.5,39,12)
                self.camera.setHpr(180,-22.5 ,0)
                self.dx = -1
            posOfSq = self.square.getPos() # The blue square position
            # Now start checking which button is pressed and change position accordingly 
            if keyMap["left"]:
                posOfSq.x -= self.dx 
                if posOfSq.x < -3: # restart blue sq from right
                    posOfSq.setX(4)
                elif posOfSq.x > 4: # restart blue sq from left
                    posOfSq.setX(-3) 
                keyMap["left"] = False  
            elif keyMap["right"]:
                posOfSq.x += self.dx 
                if posOfSq.x > 4: # restart blue sq from left
                    posOfSq.setX(-3) 
                elif posOfSq.x < -3: # restart blue sq from right
                    posOfSq.setX(4)
                keyMap["right"] = False  
            elif keyMap["up"]: 
                posOfSq.y += self.dx
                if self.turn == 0:
                    if 13 >= posOfSq.y > 5  : # Going to 2nd level in from 1st level
                        posOfSq.setZ(0.01)
                        
                    elif 21 >= posOfSq.y > 13 : # Going to 3 level in from 2nd level
                        posOfSq.setZ(1.01)
                        
                    elif 5 >= posOfSq.y > -2: # Staying in the first level 
                        posOfSq.setZ(-0.99)
                        
                    elif posOfSq.y > 21: # Going back to 1st chess board from 3rd board
                        posOfSq.setY(-2)
                        posOfSq.setZ(-0.99)
                else: # If flipped
                    if 13 >= posOfSq.y > 5 :
                        posOfSq.setZ(0.01)
                        
                    elif 21 >= posOfSq.y > 13  :
                        posOfSq.setZ(-0.99)
                        
                    elif 5 >= posOfSq.y > -2:
                        posOfSq.setZ(1.01)
                        
                    elif posOfSq.y < -2:
                        posOfSq.setY(21)
                        posOfSq.setZ(-0.99)
                keyMap["up"] = False 
            elif keyMap["down"]:
                posOfSq.y -= self.dx
                if self.turn == 1:
                    if 13 >= posOfSq.y > 5  : # Going to 2nd level in from 1st level
                        posOfSq.setZ(0.01)
                        
                    elif 21 >= posOfSq.y > 13 : # Going to 3 level in from 2nd level
                        posOfSq.setZ(-0.99)
                        
                    elif 5 >= posOfSq.y > -2: # Staying in the first level 
                        posOfSq.setZ(1.01)
                        
                    elif posOfSq.y > 21: # Going back to 1st chess board from 3rd board
                        posOfSq.setY(-2)
                        posOfSq.setZ(-0.99)
                else: # if flipped
                    if 13 >= posOfSq.y > 5 :
                        posOfSq.setZ(0.01)
                        
                    elif 21 >= posOfSq.y > 13  :
                        posOfSq.setZ(1.01)
                        
                    elif 5 >= posOfSq.y > -2:
                        posOfSq.setZ(-0.99)
                        
                    elif posOfSq.y < -2:
                        posOfSq.setY(21)
                        posOfSq.setZ(1.01)
                keyMap["down"] = False 
            elif keyMap["u"]: # Going through + z cordinate
                posOfSq.z += abs(self.dx) 
                if self.turn == 0:
                    if 0 < posOfSq.z < 1 and -2 <= posOfSq.y <= 5:
                        posOfSq.y += 8
                    elif 1 < posOfSq.z < 2 and 6 <= posOfSq.y <= 13:
                        posOfSq.y += 8
                    elif posOfSq.z > 2 and 14 <= posOfSq.y <=21:
                        posOfSq.y -= 16
                        posOfSq.z = -0.99
                elif self.turn == 1:
                    if 0 < posOfSq.z < 1 and 14 <= posOfSq.y <= 21:
                        posOfSq.y -= 8
                    elif 1 < posOfSq.z < 2 and 6 <= posOfSq.y <= 13:
                        posOfSq.y -= 8
                    elif posOfSq.z > 2 and -2 <= posOfSq.y <= 5:
                        posOfSq.y += 16
                        posOfSq.z = -0.99
                keyMap["u"] = False
                
            elif keyMap["d"]:# Going through -z cordinate
                posOfSq.z -= abs(self.dx) 
                if self.turn == 0:
                    if 0 < posOfSq.z < 1 and 14 <= posOfSq.y <= 21:
                        posOfSq.y -= 8
                    elif -1 < posOfSq.z < 0 and 6 <= posOfSq.y <= 13:
                        posOfSq.y -= 8
                    elif posOfSq.z < -1 and -2 <= posOfSq.y <= 5:
                        posOfSq.y += 16
                        posOfSq.z = 1.01
                elif self.turn == 1:
                    if 0 < posOfSq.z < 1 and -2 <= posOfSq.y <= 5:
                        posOfSq.y += 8
                    elif -1 < posOfSq.z < 0 and 6 <= posOfSq.y <= 13:
                        posOfSq.y += 8
                    elif posOfSq.z < -1 and 14 <= posOfSq.y <= 21:
                        posOfSq.y -= 16
                        posOfSq.z = 1.01
                keyMap["d"] = False 

            if keyMap["enter"]:  
                self.enterPressed(posOfSq)
                posOfSq = self.square.getPos()
            elif keyMap["enter"] == False and self.select:
                self.pieces[self.pieceKey].setPos(roundTuple(posOfSq)) 
            self.square.setPos(posOfSq) 
            if self.state:
                return task.cont
            elif self.state == 0:
                self.endGame()
    
    def enterPressed(self, posOfSq):
        if self.phase == 2 and self.phaseName == "gamePhase":
            cord = roundTuple(posOfSq) 
            if self.select == False:
                # Check whether the non blue sq is empty or not
                if self.checkFreeSq(cord):
                    keyMap["enter"] = False # Does not do any thing if an empty sq is selected
                    return
                elif self.checkFreeSq(cord) == False: # If the square contains something
                    self.piece = self.pieces[cord] # It would same cord as the posofsq
                    self.colorOfPiece = roundTuple(self.piece.getColor())
                    if self.turn == 1 and self.colorOfPiece == (1, 1, 1):
                        self.select = True # Seleect thaat piece
                        self.pieceKey = cord # The key needs to be stored for future ref
                        keyMap["enter"] = False # Reset the keymap
                        self.showMoves() # potential check point for pinned
                    elif self.turn == 0 and self.colorOfPiece != (1, 1, 1):
                        self.select = True # Seleect thaat piece
                        self.pieceKey = cord # The key needs to be stored for future ref
                        keyMap["enter"] = False # Reset the keymap
                        self.showMoves() # potential check point for pinned
                    else:
                        keyMap["enter"] = False # Does not do any thing if an empty sq is selected
                        self.piece = None
                        self.colorOfPiece = None
                        return 
            elif self.select: # When we have the piece in our hand and pressed enter 
                if cord in self.squares and self.squares[cord] != None and roundTuple(self.squares[cord].getColor()) == (0, 1, 0):
                    if cord == self.pieceKey:
                        self.piece.setPos(self.pieceKey)
                        self.select = False # Now we donot have the piece
                        self.piece = None # No piece is selected
                        self.pieceKey = None # Then there is no piece key
                        self.reColorSq()
                        keyMap["enter"] = False # Reset the keymap
                    else:
                        if self.pieces[cord] != None:
                            self.pCord[self.pieces[cord]] = (100, 100, 100)
                            self.pieces[cord].setPos(100, 100, 100)
                        self.pieces[cord] = self.piece # Replacing/ placing the piece
                        self.pCord[self.piece] = cord
                        if cord != self.pieceKey:
                        # If not then the piece will be lost from the dictionary
                            self.pieces[self.pieceKey] = None
                            # Change the previous place to None 
                        self.select = False # Now we donot have the piece
                        self.piece = None # No piece is selected
                        self.pieceKey = None # Then there is no piece key
                        self.reColorSq()
                        keyMap["enter"] = False # Reset the keymap  
                        self.checkCheckMate()
                        self.square.setPos(1, 8, 0.01)
                        self.switch()  
                else:
                    self.piece.setPos(self.pieceKey)
                    self.select = False # Now we donot have the piece
                    self.piece = None # No piece is selected
                    self.pieceKey = None # Then there is no piece key
                    self.reColorSq()
                    keyMap["enter"] = False # Reset the keymap
                return
    # Changes the top most board to lowest and vice versa 
    def switch(self):
        self.turn = int(not self.turn)
        for square in self.sCord:
            self.squares[self.sCord[square]] = None
            square.setZ(square.getZ() * -1) 
            self.sCord[square] = roundTuple(square.getPos())
            self.squares[self.sCord[square]] = square
        for piece in self.pCord:
            self.pieces[self.pCord[piece]] = None
            piece.setZ(piece.getZ() * -1)
            self.pCord[piece] = roundTuple(piece.getPos())
            self.pieces[self.pCord[piece]] = piece
        # Conditions to move a piece
    

        # Removing the green color
    
    # Changes the color of the square back to its original ones
    def reColorSq(self):
        for square in self.squares:
            if self.squares[square] != None:
                x = self.recordColor[square][0]
                y = self.recordColor[square][1]
                z = self.recordColor[square][2]
                self.squares[square].setColor(x, y, z)

    # Showing the valid moves by green square 
    def showMoves(self):
        validMoves = None
        nameOfPiece = str(self.piece).split("/")[1][0:-4] 
        if nameOfPiece == "knight":
            validMoves = self.findKnightMoves()
            self.showValidKnightSq(validMoves)
        elif nameOfPiece == "rook":
            validMoves = self.findValidRookSq()
            self.showValidSq(validMoves)
        elif nameOfPiece == "bishop":
            validMoves = self.findValidBishopSq()
            self.showValidSq(validMoves)
        elif nameOfPiece == "queen":
            self.showValidQueenSq()
        elif nameOfPiece == "king":
            validMoves = self.findKingMoves() 
            self.showValidSq(validMoves)
        elif nameOfPiece == "pawn":
            validMoves = self.findPawnMoves()
            self.showValidPawnSq(validMoves) 

    def showValidPawnSq(self, validMoves):
        normalMoves = validMoves[0]
        attackingMoves = validMoves[1]
        for move in normalMoves:
            if move in self.pieces and self.pieces[move] == None:
                if move in self.squares and self.squares[move] != None:
                    self.squares[move].setColor(0, 1, 0)
            elif move in self.pieces and self.pieces[move] == self.piece:
                if move in self.squares and self.squares[move] != None:
                    self.squares[move].setColor(0,1,0)
        for move in attackingMoves:
            if move in self.squares and self.squares[move] != None:
                if self.pieces[move] != None:
                    if roundTuple(self.pieces[move].getColor()) != self.colorOfPiece: 
                        self.squares[move].setColor(0, 1, 0)
                
    # Returns all possible moves by a pawn
    def findPawnMoves(self, currentSq = None):
        if currentSq == None:
            currentSq= self.pieceKey
        posOfPawn = currentSq  
        x = posOfPawn[0]
        y = posOfPawn[1]
        z = posOfPawn[2] 
        attackingMoves = [] 
        moves = [(x, y, z)]
        if self.turn == 0 : # Brown pawn
            moves += [(x, y + 1, z)]
            moves += [(x, y + 8, z + 1)] + [(x, y + 9, z + 1)]
            moves += [(x, y - 8, z - 1)] + [(x, y - 7, z - 1)]
            attackingMoves += [(x + 1, y + 1, z)] + [(x - 1, y + 1, z)]
            attackingMoves += [(x + 1, y + 9, z + 1)] + [(x - 1, y + 9, z + 1)]
            attackingMoves += [(x + 1, y - 9, z - 1)] + [(x - 1, y + 9, z - 1)]
            if y == -1:
                moves += [(x, y + 2, z)]
                moves += [(x, y + 18, z+2)]
                moves += [(x, y + 16, z + 2 )]
        elif self.turn == 1 :
            moves += [(x, y - 1, z)]
            moves += [(x, y - 8, z + 1)] + [(x, y - 9, z + 1)]
            moves += [(x, y + 8, z - 1)] + [(x, y + 7, z - 1)]
            moves += [(x, y + 8, z + 1)] + [(x, y + 7, z + 1)]
            attackingMoves += [(x + 1, y - 1, z)] + [(x - 1, y - 1, z)]
            attackingMoves += [(x + 1, y - 9, z + 1)] + [(x - 1, y - 9, z + 1)]
            attackingMoves += [(x + 1, y + 9, z - 1)] + [(x - 1, y + 9, z - 1)]
            if y == 20:
                moves += [(x, y - 2, z)]
                moves += [(x, y - 18, z + 2)]
                moves += [(x, y - 16, z + 2 )]
        attackingMoves = list(set(self.removeExtra(attackingMoves))) 
        for move in attackingMoves:
            if move in self.pieces and self.pieces[move] != None :
                moves += [move]
        moves = list(set(self.removeExtra(moves)))
        return moves, attackingMoves
# Returns all possible moves by a king
    def findKingMoves(self, square = None, threat = True, findType = 1, check = False):
        if square == None:
            square = self.piece.getPos() 
        if check:
            self.turn = not self.turn
        posOfKing = roundTuple(square)  
        x = posOfKing[0]
        y = posOfKing[1]
        z = posOfKing[2]
        moves = []
        moves += [(x + 1, y, z)] + [(x - 1, y, z)] 
        moves += [(x , y+ 1, z)] + [(x , y - 1, z)]
        moves += [(x + 1, y + 1, z)] + [(x - 1, y - 1, z)]
        moves += [(x - 1, y+ 1, z)] + [(x + 1, y - 1, z)]
        if self.turn == 0:
            moves += [(x , y - 8, z - 1)] + [(x - 1, y + 8, z + 1)]
            moves += [(x + 1, y + 8, z + 1)] + [(x - 1, y + 8, z + 1)]
            moves += [(x + 1, y - 8, z - 1)] + [(x - 1, y - 8, z - 1)]
            moves += [(x , y+ 9, z+1)] + [(x , y - 9, z-1)]
            moves += [(x, y + 8, z + 1)] + [(x, y - 8, z - 1)] + [(x, y, z)]
            moves += [(x, y + 7, z + 1)] + [(x, y - 7, z - 1)]
            moves += [(x + 1, y + 7, z + 1)] + [(x + 1, y - 7, z - 1)]
            moves += [(x - 1, y + 7, z + 1)] + [(x - 1, y - 7, z - 1)]
            moves += [(x + 1 , y+ 9, z + 1)] + [(x + 1 , y - 9, z-1)]
            moves += [(x - 1 , y+ 9, z + 1)] + [(x - 1 , y - 9, z-1)]
        else:
            moves += [(x , y + 8, z - 1)] + [(x - 1, y - 8, z + 1)]
            moves += [(x + 1, y - 8, z + 1)] + [(x - 1, y - 8, z + 1)]
            moves += [(x + 1, y + 8, z - 1)] + [(x - 1, y + 8, z - 1)]
            moves += [(x , y - 9, z+1)] + [(x , y + 9, z - 1)]
            moves += [(x, y - 8, z + 1)] + [(x, y + 8, z - 1)] + [(x, y, z)]
            moves += [(x, y - 7, z + 1)] + [(x, y + 7, z - 1)]
            moves += [(x + 1, y - 7, z + 1)] + [(x + 1, y + 7, z - 1)]
            moves += [(x - 1, y - 7, z + 1)] + [(x - 1, y + 7, z - 1)]
            moves += [(x + 1 , y - 9, z + 1)] + [(x + 1 , y + 9, z-1)]
            moves += [(x - 1 , y - 9, z + 1)] + [(x - 1 , y + 9, z-1)]  

        if check:
            return moves

        moves = list(set(self.removeExtra(moves))) #   removal of extras squares 
        if threat and findType: # Findtype for linear blocks
            for cord in moves[:]: 
                if self.checkThreat(cord): 
                    moves.remove(cord) 
        if findType:
            kingThreats = self.checkNearbyKing()
            for risk in kingThreats:
                if risk in moves[:]:
                    moves.remove(risk) 
        return moves 

    # Returns the possible moves if there is a king nearby
    def checkNearbyKing(self):
        if self.turn % 2 == 1:
            moves = self.findKingMoves(self.records["darkKing"].getPos(), False, 0) 
            # Finds all possible moves by the opponent king without considering the threats
            return moves
        elif self.turn % 2 == 0:
            moves = self.findKingMoves(self.records["lightKing"].getPos(), False, 0)
            return moves 

    # Checks whether a square is under threat 
    def checkThreat(self, square, color = None):
        self.tempColor = self.colorOfPiece
        if color != None:
            self.colorOfPiece = color
        self.pieces[self.pieceKey] = None
        x = square[0]
        y = square[1]
        z = square[2] 
        findPotentialRookPos = self.findValidRookSq(square)
        for sq in findPotentialRookPos:
            pos = self.sCord[sq] 
            if pos in self.pieces and self.pieces[pos] != None:
               if "rook"  in str(self.pieces[pos]) or "queen" in str(self.pieces[pos]):
                   if roundTuple(self.pieces[pos].getColor()) != self.colorOfPiece and pos != square:
                       return True  
        findPotentialBishopPos = self.findValidBishopSq(square)
        for sq in findPotentialBishopPos:
            pos = self.sCord[sq]
            if pos in self.pieces and self.pieces[pos] != None:
               if "bishop"  in str(self.pieces[pos]) or "queen"  in str(self.pieces[pos]):
                   if roundTuple(self.pieces[pos].getColor()) != self.colorOfPiece and pos != square:
                       return True 
        findPotentialKnightPos = self.findKnightMoves(square)
        for pos in findPotentialKnightPos:
           if pos in self.pieces and self.pieces[pos] != None:
               if "knight"  in str(self.pieces[pos]) and pos != square:
                   if roundTuple(self.pieces[pos].getColor()) != self.colorOfPiece:
                       return True 
        findPotentialPawnPos = self.findPawnMoves(square)[1]
        for pos in findPotentialPawnPos:
           if pos in self.pieces and self.pieces[pos] != None:
               if "pawn"  in str(self.pieces[pos]) :
                   if roundTuple(self.pieces[pos].getColor()) != self.colorOfPiece:
                       return True 

        self.pieces[self.pieceKey] = self.piece
        self.colorOfPiece = self.tempColor
        return False  

    def checkPiece(self, potentialThreats, piece):
        for square in potentialThreats:
            if square in self.pieces and piece in str(self.pieces[square]):
                if self.colorOfPiece != self.pieces[square].getColor():
                    return True
        else:
            return False  
    
    def removeExtra(self, moves):
        for move in moves[:]:
            if move not in self.squares:
                moves.remove(move)
            elif move in self.pieces and self.pieces[move] != None:
                if roundTuple(self.pieces[move].getColor()) == self.colorOfPiece:
                    if self.piece != self.pieces[move]:
                        moves.remove(move)
        return moves  
    
    def showValidSq(self, validMoves):
        # Valid moves are in a list of tuples
        for move in validMoves:
            if isinstance(move, type((1,2))) == False: 
                move.setColor(0, 1, 0)
            elif isinstance(move, type((1,2))):
                if self.squares[move] != None:
                    self.squares[move].setColor(0, 1, 0) 
    
    def showValidQueenSq(self):
        validMoves = []
        validMoves += self.findValidRookSq()
        validMoves += self.findValidBishopSq()
        self.showValidSq(validMoves) 
    
    def findValidBishopSq(self, currentSq = None):
        # Changes the color of valid squares of bishop into green
        if currentSq == None:
            currentSq = self.pieceKey
        posOfBishop = currentSq 
        x = posOfBishop[0]
        y = posOfBishop[1]
        z = posOfBishop[2]
        validSq = []
        for i in range(9): # Top right corners
            a = x + i
            b = y + i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                elif self.pieces[potentialSq] == self.piece:
                    validSq += [self.squares[potentialSq]]
                else:
                    break
        for i in range(1, 9): # Top left corners
            a = x - i
            b = y + i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9): # Bottom left corners
            a = x - i
            b = y - i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9): # Bottom right corners
            a = x + i
            b = y - i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                else:
                    break
        if self.turn == 0:
            for i in range(1, 3): # upper top right
                a = x + i
                b = y + (8 * i) + i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper bottom right
                a = x + i
                b = y + (8 * i) - i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper top left
                a = x - i
                b = y + (8 * i) + i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper bottom left
                a = x - i
                b = y + (8 * i) - i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # lower top right
                a = x + i
                b = y - (8 * i) + i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower bottom right
                a = x + i
                b = y - (8 * i) - i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower top left
                a = x - i
                b = y - (8 * i) + i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower bottom left
                a = x - i
                b = y - (8 * i) - i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
        elif self.turn == 1:
            for i in range(1, 3): # upper top right
                a = x + i
                b = y - (8 * i) + i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper bottom right
                a = x + i
                b = y - (8 * i) - i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper top left
                a = x - i
                b = y - (8 * i) + i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper bottom left
                a = x - i
                b = y - (8 * i) - i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # lower top right
                a = x + i
                b = y + (8 * i) + i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower bottom right
                a = x + i
                b = y + (8 * i) - i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower top left
                a = x - i
                b = y + (8 * i) + i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower bottom left
                a = x - i
                b = y + (8 * i) - i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
        return validSq   
    
    def findValidRookSq(self, currentSq = None):
        # Changes the color of valid squares into green
        if currentSq == None:
            currentSq = self.pieceKey
        posOfRook = currentSq 
        x = posOfRook[0]
        y = posOfRook[1]
        z = posOfRook[2]
        validSq = [] 
        for i in range(9): # going positive x axis
            a = x + i
            potentialSq = (a, y, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                elif self.pieces[potentialSq] == self.piece:
                    validSq += [self.squares[potentialSq]]
                else:
                    break
        for i in range(1, 9):# going neg x axis
            a = x - i
            potentialSq = (a, y, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9):# going positive y axis
            a = y + i
            potentialSq = (x, a, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9):# going neg y axis
            a = y - i
            potentialSq = (x, a, z)
            if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                validSq += [self.squares[potentialSq]]
            elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.squares[potentialSq]]
                    break
                else:
                    break
        if self.turn == 0:
            for i in range(1, 3):# going positive z axis
                a = z + i
                b = y + (i * 8)
                potentialSq = (x, b, a) 
                if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3):# going neg z axis
                a = z - i
                b = y - (i * 8)
                potentialSq = (x, b, a)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # Upper level rights
                a = x + i
                b = y + (8 * i)
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # Upper level lefts
                a = x - i
                b = y + (8 * i)
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower level lefts
                a = x - i
                b = y - (8 * i)
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower level rights
                a = x + i
                b = y - (8 * i)
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3):# Upper level ups
                a = x  
                b = y + (8 * i) + i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower level down
                a = x 
                b = y - (8 * i) - i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper level down
                a = x 
                b = y + (8 * i) - i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # lower level ups
                a = x 
                b = y - (8 * i) + i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
        elif self.turn == 1:
            for i in range(1, 3):# going positive z axis
                a = z + i
                b = y - (i * 8)
                potentialSq = (x, b, a) 
                if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3):# going neg z axis
                a = z - i
                b = y + (i * 8)
                potentialSq = (x, b, a)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # Upper level rights
                a = x + i
                b = y - (8 * i)
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # Upper level lefts
                a = x - i
                b = y - (8 * i)
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower level lefts
                a = x - i
                b = y + (8 * i)
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower level rights
                a = x + i
                b = y + (8 * i)
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3):# Upper level ups
                a = x  
                b = y - (8 * i) + i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # lower level down
                a = x 
                b = y + (8 * i) - i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
            for i in range(1, 3): # upper level down
                a = x 
                b = y - (8 * i) - i
                c = z + i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
                    
            for i in range(1, 3): # lower level ups
                a = x 
                b = y + (8 * i) + i
                c = z - i
                potentialSq = (a, b, c)
                if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    validSq += [self.squares[potentialSq]]
                elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        validSq += [self.squares[potentialSq]]
                        break
                    else:
                        break
        return validSq
    
    def showValidKnightSq(self, validMoves):
        # Exclusive only to knight as we are hardcoding all possible positions
        for move in validMoves:
            if self.checkFreeSq(move):
                if move in self.squares and self.squares[move] != None:
                    self.squares[move].setColor(0, 1, 0)
            elif not self.checkFreeSq(move):
                if roundTuple(self.pieces[move].getColor()) != self.colorOfPiece:
                    self.squares[move].setColor(0, 1, 0)
                elif self.piece == self.pieces[move]:
                    self.squares[move].setColor(0, 1, 0) 
    
    def findKnightMoves(self, currentSq = None):
        if currentSq == None:
            currentSq= self.pieceKey 
        posOfKnight = currentSq
        colorOfKnight = self.colorOfPiece
        x = posOfKnight[0]
        y = posOfKnight[1]
        z = posOfKnight[2]
        moves = [(x, y, z)]
        moves += [(x + 1, y + 2 , z), (x - 1, y + 2, z), (x + 2, y + 1, z), (x -2, y + 1, z)]
        moves += [(x + 1, y - 2 , z), (x - 1, y - 2, z), (x + 2, y - 1, z), (x -2, y - 1, z)] 
        if self.turn == 0:
            moves += [(x, y + 10, z + 1), (x, y + 6 , z + 1), (x, y - 10, z - 1),(x, y - 6 , z -1)]
            moves += [(x + 2, y + 8, z + 1),(x - 2, y + 8, z + 1),(x + 2, y - 8, z + 1),(x - 2, y - 8, z + 1)]
            moves += [(x + 2, y - 8, z - 1),(x - 2, y - 8, z - 1) ]
            moves += [(x, y + 17, z + 2), (x, y + 15, z + 2), (x, y - 17, z - 2), (x, y - 15, z - 2), (x + 1, y + 16, z + 2)]
            moves += [(x - 1, y + 16, z + 2), (x + 1, y - 16, z - 2), (x - 1, y - 16, z - 2)]
        elif self.turn == 1:
            moves += [(x, y - 10, z + 1), (x, y - 6 , z + 1), (x, y + 10, z - 1),(x, y + 6 , z - 1),
                (x, y - 17, z + 2),(x, y - 15, z + 2), (x, y + 17, z - 2),(x, y + 15, z - 2),(x + 1, y - 16, z + 2), 
                (x - 1, y - 16, z + 2),(x + 1, y + 16, z -2 ), (x - 1, y + 16, z - 2), (x + 2, y - 8 , z + 1),
                (x - 2, y - 8 , z + 1), (x + 2, y + 8, z - 1), (x - 2, y + 8, z - 1)]
            
        return moves 
    
    def checkCheckMate(self):  
        brownKing = self.records["darkKing"]
        whiteKing = self.records["lightKing"]
        if whiteKing.getPos() == (100, 100, 100):
            self.winner = "Brown"
            self.endGame()
        elif brownKing.getPos() == (100, 100, 100):
            self.winner = "White"
            self.endGame()

    # This function sets up the environment to play the game
    def gamePhase(self): 
        self.formBoardAndPieces() 
        self.setBackgroundColor(color(0,0,125)[0],
        color(0,125,0)[1],color(0,0,125)[2]) # Any
        # For perfect viewing 
        self.camera.setPos(0.5,-20,25)
        self.camera.setHpr(0,-42.5,0)
        

        self.phaseName = "gamePhase"

    # The starting page of the game
    def startPhase(self):
        #self.disableMouse()
        if self.phase == 1 and self.phaseName == "startPhase":
            # Store variables
            self.squares = {}
            self.pieces = {}
            self.recordColor = {} 
            self.pCord = {}
            self.sCord = {}
            self.records = {}
            # Updating the required updates
            self.taskMgr.add(self.update, "update")
            # Change in unit
            self.dx = 1
            # Piece variables
            self.select = False
            self.turn = 0
            self.piece = None
            self.colorOfPiece = None
            self.state = 1
            self.keyboard = 1 
            # Mouse stufs
            self.current_z = 0.01
            self.pickerRay = CollisionRay()

            self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],)  
     
            self.title =  OnscreenText(text="Millenium Chess", parent=base.aspect2d ,
                         fg=(1, 1, 0, 1), pos=(0, 0.7), scale=.3, shadow=(0, 0, 0, 0.5),
                         align = TextNode.ACenter)

            self.side1 = OnscreenText(text="Brown", parent=base.a2dBottomLeft,align=TextNode.ALeft,
                         fg=(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2], 1), 
                         pos=(0.5, 0.5), scale=.2, shadow=(0, 0, 0, 0.5))
            self.side2 = OnscreenText(text="White", parent=base.a2dBottomRight,align=TextNode.ARight,
                         fg=(1, 1, 1, 1), pos=(-0.5, 0.5), scale=.2, shadow=(0, 0, 0, 0.5), )
        elif self.phase != 1 or self.phaseName != "startPhase": # If phase is changed
            self.title.destroy()
            self.side1.destroy()
            self.side2.destroy()

    # Changes the above mapping of the keys
    def updateKeyMap(self, key):
        if self.phase == 2 and self.phaseName == "gamePhase":
            if key != "m":
                keyMap[key] = not keyMap[key]
            elif key == "m":
                keyMap[key] = not keyMap[key]
    # Restarts the game
    def restartGame(self):
        if self.phase != 1:
            if self.phase == 2:
                for piece in self.pCord:
                    piece.detachNode() 
                for square in self.sCord:
                    square.detachNode() 
                self.square.detachNode()
            elif self.phase == 3:
                self.over.detachNode()
                self.winnerName.detachNode()
                self.winner = None
            self.phase = 1 
            self.phaseName = "startPhase"
            self.startPhase()

    # Game over phase
    def endGame(self):
        if self.phase != 3:
        # Find the type of the ending
            if self.phase == 2:
                for piece in self.pCord:
                    piece.detachNode() 
                for square in self.sCord:
                    square.detachNode() 
                self.square.detachNode()
            if self.phase == 1:
                self.title.detachNode()
                self.side1.detachNode()
                self.side2.detachNode()
            self.phase = 3
            self.state = 0
            self.phaseName = "endGame"
            self.setBackgroundColor(1, 1, 1)
            self.over =  OnscreenText(text="Game Over", parent=base.aspect2d ,
                fg=(1, 0, 0, 1), pos=(0, 0.7), scale=.3, shadow=(1, 0, 0, 0.7),
                align = TextNode.ACenter)
            self.winnerName = OnscreenText(text="Winner: " + str(self.winner),
                 parent=base.aspect2d, fg=(0, 0, 0, 1), pos=(0, 0), scale=.2, 
                 align = TextNode.ACenter)

    
    def __init__(self):
        # Inheriting all attributes
        super().__init__()
        
        #self.disableMouse() # For camera issues

        self.phase = 1
        self.phaseName = "startPhase" 


        # Setupping the lights
        self.setupLights()

        # Accepting the commands
        self.accept("arrow_left", self.updateKeyMap, ["left"])
        self.accept("arrow_right", self.updateKeyMap, ["right"])
        self.accept("arrow_up",self. updateKeyMap, ["up"])
        self.accept("arrow_down", self.updateKeyMap, ["down"])
        self.accept("u", self.updateKeyMap, ["u"])
        self.accept("d",self. updateKeyMap, ["d"] )
        self.accept("m", self.updateKeyMap, ["m"])
        self.accept("r", self.restartGame)
        self.accept("e", self.endGame)
        self.accept("enter", self.updateKeyMap, ["enter"])
        self.accept("mouse1", self.mousePressedLeft)
        self.winner = "None"
 
        self.startPhase() 

game = MilleniumChess()
game.run()










