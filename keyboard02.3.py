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
                        self.recordColor[(cord)] = (0,0,0)
    #                     count+= 1
                    else:
                        self.squares[(cord)] = loader.loadModel("models/square.egg")
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(1,1,1)
                        self.recordColor[(cord)] = (1,1,1)
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
                self.showMoves()
                return
        elif self.select: # When we have the piece in our hand and pressed enter
#             if cord not in self.pieces:
            self.pieces[cord] = self.piece # Replacing/ placing the piece
            self.pieces[self.pieceKey] = None # Change the previous place to None
            self.select = False # Now we donot have the piece
            self.piece = None # No piece is selected
            self.pieceKey = None # Then there is no piece key
            self.reColorSq()
            keyMap["enter"] = False # Reset the keymap
            return # unnecessary?
        
    def reColorSq(self):
        for square in self.squares:
            x = self.recordColor[square][0]
            y = self.recordColor[square][1]
            z = self.recordColor[square][2]
            self.squares[square].setColor(x, y, z)
    
    def showMoves(self):
        nameOfPiece = str(self.piece).split("/")[1][0:-4]
        self.colorOfPiece = roundTuple(self.piece.getColor())
        if nameOfPiece == "knight":
            validMoves = self.findKnightMoves()
            self.showValidKnightSq(validMoves)
        elif nameOfPiece == "rook":
            self.showValidRookSq()
        elif nameOfPiece == "bishop":
            self.showValidBishopSq()
        elif nameOfPiece == "queen":
            self.showValidQueenSq()
            
    def showValidQueenSq(self):
        self.showValidBishopSq()
        self.showValidRookSq()
        
            
    def showValidBishopSq(self):# Changes the color of valid squares of bishop into green
        posOfBishop = roundTuple(self.piece.getPos())
        self.squares[posOfBishop].setColor(0, 1, 0)
        x = posOfBishop[0]
        y = posOfBishop[1]
        z = posOfBishop[2]
        for i in range(1, 9): # Top right corners
            a = x + i
            b = y + i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 9): # Top right corners
            a = x - i
            b = y + i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 9): # Bottom left corners
            a = x - i
            b = y - i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 9): # Bottom right corners
            a = x + i
            b = y - i
            potentialSq = (a, b, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # upper top right
            a = x + i
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # upper bottom right
            a = x + i
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # upper top left
            a = x - i
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # upper bottom left
            a = x - i
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
                
        for i in range(1, 3): # lower top right
            a = x + i
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower bottom right
            a = x + i
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower top left
            a = x - i
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower bottom left
            a = x - i
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
            
            
    def showValidRookSq(self): # Changes the color of valid squares into green
        posOfRook = roundTuple(self.piece.getPos())
        self.squares[posOfRook].setColor(0, 1, 0)
        x = posOfRook[0]
        y = posOfRook[1]
        z = posOfRook[2]
#         print(posOfRook)
#         print(x, y, z)
        for i in range(1, 9): # going positive x axis
            a = x + i
            potentialSq = (a, y, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 9):# going neg x axis
            a = x - i
            potentialSq = (a, y, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 9):# going positive y axis
            a = y + i
            potentialSq = (x, a, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 9):# going neg y axis
            a = y - i
            potentialSq = (x, a, z)
            if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3):# going positive z axis
            a = z + i
            b = y + (i * 8)
            potentialSq = (x, b, a)
            print(potentialSq)
            if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3):# going neg z axis
            a = z - i
            b = y - (i * 8)
            potentialSq = (x, b, a)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
                
        for i in range(1, 3): # Upper level rights
            a = x + i
            b = y + (8 * i)
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
                
        for i in range(1, 3): # Upper level lefts
            a = x - i
            b = y + (8 * i)
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower level lefts
            a = x - i
            b = y - (8 * i)
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower level lefts
            a = x + i
            b = y - (8 * i)
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3):# Upper level ups
            a = x  
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower level down
            a = x 
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # upper level down
            a = x 
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
        for i in range(1, 3): # lower level ups
            a = x 
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                self.squares[potentialSq].setColor(0, 1, 0)
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    self.squares[potentialSq].setColor(0, 1, 0)
                    break
                else:
                    break
                




    def showValidKnightSq(self, validMoves):
        for move in validMoves:
            if self.checkFreeSq(move):
                if move in self.squares:
                    self.squares[move].setColor(0, 1, 0)
            elif not self.checkFreeSq(move):
                if roundTuple(self.pieces[move].getColor()) != self.colorOfPiece:
                    self.squares[move].setColor(0, 1, 0)
            
    def findKnightMoves(self):
        print("knight itme")
        posOfKnight = self.piece.getPos()
        colorOfKnight = self.piece.getColor()
        self.squares[posOfKnight].setColor(0, 1, 0)
        x = posOfKnight.getX()
        y = posOfKnight.getY()
        z = round(posOfKnight.getZ())
        m1 = (x + 1, y + 2 , z)
        m2 = (x - 1, y + 2, z)
        m3 = (x + 2, y + 1, z)
        m4 = (x -2, y + 1, z)
        m5 = (x + 1, y - 2 , z)
        m6 = (x - 1, y - 2, z)
        m7 = (x + 2, y - 1, z)
        m8 = (x -2, y - 1, z)
        m9 = (x, y + 10, z + 1)
        m10 = (x, y + 6, z + 1)
        m11 = (x, y - 10, z - 1)
        m12 = (x, y - 6, z -1)
        m13 = (x + 2, y + 8, z + 1)
        m14 = (x - 2, y + 8, z + 1)
        m15 = (x + 2, y - 8, z -1 )
        m16 = (x - 2, y  - 8, z - 1)
        m17 = (x, y + 17, z + 2)
        m18 = (x, y + 15, z + 2)
        m19 = (x, y - 17, z - 2)
        m20 = (x, y - 15, z -2)
        m21 = (x + 1, y + 16, z + 2)
        m22 = (x - 1, y + 16, z + 2)
        m23 = (x + 1, y - 16, z -2 )
        m24 = (x - 1, y  - 16, z - 2)
#         print(posOfKnight)
#         print([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16])
        return [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24]
            

    
    def __init__(self):
        # Inheriting all attributes
        super().__init__()
        # Store variables
        self.squares = {}
        self.pieces = {}
        self.recordColor = {}
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



