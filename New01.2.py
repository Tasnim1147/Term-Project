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

# Change the color format into computer readable format
def color(r,g,b):
    return ((r/255, g/255, b/255))

class MilleniumChess(ShowBase):

    # CALLED every frame
    # Changes the position based on blue sq
    def update(self, task):
        if self.turn == 1:
            self.camera.setPos(0.5,-20,25)
            self.camera.setHpr(0,-42.5,0)
            self.dx = 1
#             self.square.setPos(1, -1, -0.99)
        else: 
            self.camera.setPos(0.5,39,25)
            self.camera.setHpr(180,-42.5 ,0)
#             self.square.setPos(1, 13, -0.99)
            self.dx = -1
        # First get the current location of 
        posOfSq = self.square.getPos()
        
        # Now start check which button is pressed and change position accordingly
        if keyMap["left"]:
            posOfSq.x -= self.dx 
            keyMap["left"] = False
            
        elif keyMap["right"]:
            posOfSq.x += self.dx 
            keyMap["right"] = False
            
        elif keyMap["up"]: 
            posOfSq.y += self.dx
            keyMap["up"] = False 
                
        elif keyMap["down"]:
            posOfSq.y -= self.dx
            keyMap["down"] = False 
                
        elif keyMap["u"]:
            posOfSq.z += abs(self.dx) 
            keyMap["u"] = False
            
        elif keyMap["d"]:
            posOfSq.z -= abs(self.dx)
            keyMap["d"] = False
            
        if keyMap["enter"]:
            self.enterPressed(posOfSq)
        elif keyMap["enter"] == False and self.select:
            if self.turn == 1:
                self.pieces[self.pieceKey].setPos(roundTuple(posOfSq))
            else:
                self.inverseP[self.pieceKey].setPos(roundTuple(posOfSq))
            
        self.square.setPos(posOfSq)
        
        return task.cont
    
    def enterPressed(self, posOfSq):
        cord = roundTuple(posOfSq)
        if self.turn == 1:
            if self.select == False:
                if self.pieces[cord] ==None:
                    keyMap["enter"] = False
                else:
                    self.piece = self.pieces[cord]
                    self.pieceKey = cord
                    keyMap["enter"] = False
                    self.select = True
                    self.showMoves()
            elif self.select == True:
                if self.pieces[cord] == None:
                    self.piece = None
                    self.pieceKey = None
                    keyMap["enter"] = False
                    self.select = False
                    self.switch()
                    self.recolorSq()
                else:
                    self.pieces[cord].setPos(100,100,100)
                    self.pieces[cord] = self.piece
                    self.piece = None
                    self.pieceKey = None
                    self.select= False
                    keyMap["enter"] = False
                    self.switch()
                    self.recolorSq()
        elif self.turn == 0:
            if self.select == False:
                if self.inverseP[cord] ==None:
                    keyMap["enter"] = False
                else:
                    self.piece = self.inverseP[cord]
                    self.pieceKey = cord
                    keyMap["enter"] = False
                    self.select = True
                    self.showMoves()
            elif self.select == True:
                if self.inverseP[cord] == None:
                    self.piece = None
                    self.pieceKey = None
                    keyMap["enter"] = False
                    self.select = False
                    self.switch()
                    self.recolorSq()
                else:
                    self.inverseP[cord].setPos(100,100,100)
                    self.inverseP[cord] = self.piece
                    self.piece = None
                    self.pieceKey = None
                    self.select= False
                    keyMap["enter"] = False
                    self.switch()
                    self.recolorSq()
        return
    
    
    def switch(self):
        self.turn = int(not self.turn)
        for square in self.sCord:
            square.setZ(square.getZ() * -1)
            self.inverseP[roundTuple(square.getPos())] = None
            self.inverseS[roundTuple(square.getPos())] = square
        for piece in self.pCord:
            piece.setZ(piece.getZ() * -1)
            self.pCord[piece] = roundTuple(piece.getPos())
            self.inverseP[roundTuple(piece.getPos())] = piece

                    
    

    def formBoardAndPieces(self):
        
        for z in range(-1,2): # The change in z axis
            count = 1 # For color serial
            for x in range(-3,5): # For changing col
                for y in range(13,5,-1):
                    # The current cord
                    cord = (x, y + (8 * z), z)
                    # Forming the squares
                    if count % 2 == 0: # Even count will be black squares
                        square = loader.loadModel("models/square.egg")
                        self.squares[(cord)] = square 
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(0, 0, 0) 
                        self.pieces[(cord)] = None
                        self.sCord[square] = cord
                        self.recordColor[square] = (0, 0, 0)
                        
                        # For removing future errors of not found
                    else: # Odd count will be black squares
                        square = loader.loadModel("models/square.egg")
                        self.squares[(cord)] = square 
                        self.squares[(cord)].reparentTo(render)
                        self.squares[(cord)].setPos(cord)
                        self.squares[(cord)].setColor(1, 1, 1) 
                        self.pieces[(cord)] = None
                        self.sCord[square] = cord
                        self.recordColor[square] = (1, 1, 1)
                        # For removing future errors of not found
                    # Forming the pieces
                    # PAWN
                    if y == 12 and z != 0  and z != -1: # White Pawn
                        piece = loader.loadModel("models/pawn.egg")
                        self.pieces[(cord)] = piece
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(x, y + (8 * z), z)
                        self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                            color(150, 75, 0)[1],color(150, 75, 0)[2])
                        self.pCord[piece] = cord
                        
                    elif y == 7 and z != 0 and z != 1: # Dark Pawn
                        piece = loader.loadModel("models/pawn.egg")
                        self.pieces[(cord)] = piece
                        self.pieces[(cord)].reparentTo(render)
                        self.pieces[(cord)].setPos(cord)
                        self.pieces[(cord)].setColor(1, 1, 1)
                        self.pCord[piece] = cord
                    # ROOK
                    elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)] and z != 0:
                        # Positions of potential rook
                        if y == 13 and z != -1: # Dark rook
                            piece = loader.loadModel("models/rook.egg") 
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2])
                            self.pCord[piece] = cord
                            
                        elif y == 6 and z != 1: # Light Rook
                            piece = loader.loadModel("models/rook.egg") 
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1, 1, 1)
                            self.pCord[piece] = cord
                    # KNIGHT  
                    elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]and z != 0:
                        # Positions of potential KNIGHT
                        if y == 13 and z != -1: # Dark Knight
                            piece = loader.loadModel("models/knight.egg")
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1], color(150, 75, 0)[2])
                            self.pCord[piece] = cord
                        elif y == 6 and z != 1: # Light Knight
                            piece = loader.loadModel("models/knight.egg")
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1, 1, 1)
                            self.pCord[piece] = cord
                    # Bishop
                    elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]and z != 0:
                        # Positions of potential bishop
                        if y == 13 and z != -1: # Dark Bishop
                            piece = loader.loadModel("models/bishop.egg")
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2])
                            self.pCord[piece] = cord
                            
                        elif y == 6 and z != 1: # Light bishop
                            piece = loader.loadModel("models/bishop.egg")
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1, 1, 1)
                            self.pCord[piece] = cord
                    # King
                    elif (x, y) in [(0, 13), (0,6)]and z != 0:
                        # Potential position for king
                        if y == 13 and z != -1: # Dark King
                            piece = loader.loadModel("models/king.egg") 
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1], color(150, 75, 0)[2])
                            self.pCord[piece] = cord
                            self.records["darkKing"] = piece
                        elif y == 6 and z != 1: # Light King
                            piece = loader.loadModel("models/king.egg") 
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1, 1, 1)
                            self.pCord[piece] = cord
                            self.records["lightKing"] = piece
                    # Queen
                    elif (x, y) in [(1, 13), (1,6)]and z != 0:
                        # Potential position for queen
                        if y == 13 and z != -1: # Dark queen
                            piece = loader.loadModel("models/queen.egg") 
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1], color(150, 75, 0)[2])
                            self.pCord[piece] = cord
                        elif y == 6 and z != 1: # Light Queen
                            piece = loader.loadModel("models/queen.egg") 
                            self.pieces[(cord)] = piece
                            self.pieces[(cord)].reparentTo(render)
                            self.pieces[(cord)].setPos(cord)
                            self.pieces[(cord)].setColor(1, 1, 1)
                            self.pCord[piece] = cord
                    count+= 1
                count+= 1
                
    def recolorSq(self):
#         if self.turn == 0:
        for square in self.sCord:
            square.setColor(self.recordColor[square][0],
                self.recordColor[square][1],self.recordColor[square][2])

    def moveCondition(self, cord):
        initialPiece = None
        if self.turn == 1:
            potentialEmpSq = self.pCord[self.piece] # Taking the cord of currently selected piece
            self.pieces[potentialEmpSq] = None # Replacing with none
            if cord in self.pieces: 
                initialPiece = self.pieces[cord]
            self.pieces[cord] = self.piece
            if self.colorOfPiece == (1, 1, 1):
                print("yes")
                tempPiece = self.records["lightKing"]
                threatenedCord = self.pCord[tempPiece]
                check = self.checkThreat(threatenedCord)
            elif self.colorOfPiece != (1, 1, 1):
                tempPiece = self.records["darkKing"]
                threatenedCord = self.pCord[tempPiece] 
                check = self.checkThreat(threatenedCord)
            self.pieces[potentialEmpSq] = self.piece
            self.pieces[cord] = initialPiece
            return check
        elif self.turn == 0:
            potentialEmpSq = self.pCord[self.piece]
            self.inverseP[potentialEmpSq] = None
            if cord in self.inverseP:
                initialPiece = self.inverseP[cord]
            self.inverseP[cord] = self.piece
            if self.colorOfPiece == (1, 1, 1):
                print("yes")
                tempPiece = self.records["lightKing"]
                threatenedCord = self.pCord[tempPiece]
                check = self.checkThreat(threatenedCord)
            elif self.colorOfPiece != (1, 1, 1):
                tempPiece = self.records["darkKing"]
                threatenedCord = self.pCord[tempPiece]
                print(self.checkThreat(threatenedCord))
                check = self.checkThreat(threatenedCord)
            self.inverseP[potentialEmpSq] = self.piece
            self.inverseP[cord] = initialPiece
            return check
        
    def showMoves(self):
        validMoves = None
        nameOfPiece = str(self.piece).split("/")[1][0:-4]
        if nameOfPiece == "knight":
            validMoves = self.findKnightMoves()
            print(validMoves)
            self.showValidKnightSq(validMoves)
        elif nameOfPiece == "rook":
            validMoves = self.findValidRookSq()
            self.showValidSq(validMoves)
        elif nameOfPiece == "bishop":
            validMoves = self.findValidBishopSq()
#             print(validMoves)
            self.showValidSq(validMoves)
        elif nameOfPiece == "queen":
            self.showValidQueenSq()
        elif nameOfPiece == "king":
            validMoves = self.findKingMoves()
            self.showValidSq(validMoves)
        elif nameOfPiece == "pawn":
            validMoves = self.findPawnMoves()
            self.showValidSq(validMoves)
            
    def findKnightMoves(self, currentSq= None):
        if currentSq == None:
            currentSq= self.pieceKey 
        posOfKnight = currentSq
#         print(posOfKnight)
        colorOfKnight = self.colorOfPiece
        x = posOfKnight[0]
        y = posOfKnight[1]
        z = posOfKnight[2]
        if self.turn == 1:
            m1 = (x + 1, y + 2 , z)
            m2 = (x - 1, y + 2, z)
            m3 = (x + 2, y + 1, z)
            m4 = (x -2, y + 1, z)
            m5 = (x + 1, y - 2 , z)
            m6 = (x - 1, y - 2, z)
            m7 = (x + 2, y - 1, z)
            m8 = (x -2, y - 1, z)
            m25 = (x, y, z)
            m9  = (x, y + 10, z + 1)
            m10 = (x, y + 6 , z + 1)
            m11 = (x, y - 10, z - 1)
            m12 = (x, y - 6 , z -1)
            m13 = (x + 2, y + 2, z + 1)
            m14 = (x - 2, y + 2, z + 1)
            m15 = (x + 2, y - 2, z -1 )
            m16 = (x - 2, y - 2, z - 1)
            m17 = (x, y + 17, z + 2)
            m18 = (x, y + 15, z + 2)
            m19 = (x, y - 17, z - 2)
            m20 = (x, y - 15, z - 2)
            m21 = (x + 1, y + 16, z + 2)
            m22 = (x - 1, y + 16, z + 2)
            m23 = (x + 1, y - 16, z - 2)
            m24 = (x - 1, y - 16, z - 2)
        elif self.turn == 0:
            m1 = (x + 1, y - 2 , z)
            m2 = (x - 1, y - 2, z)
            m3 = (x + 2, y - 1, z)
            m4 = (x -2, y - 1, z)
            m5 = (x + 1, y + 2 , z)
            m6 = (x - 1, y + 2, z)
            m7 = (x + 2, y + 1, z)
            m8 = (x -2, y + 1, z)
            m25 = (x, y, z)
            m9  = (x, y - 10, z + 1)
            m10 = (x, y - 6 , z + 1)
            m11 = (x, y + 10, z - 1)
            m12 = (x, y + 6 , z -1)
            m13 = (x + 2, y - 2, z + 1)
            m14 = (x - 2, y - 2, z + 1)
            m15 = (x + 2, y + 2, z -1 )
            m16 = (x - 2, y + 2, z - 1)
            m17 = (x, y - 17, z + 2)
            m18 = (x, y - 15, z + 2)
            m19 = (x, y + 17, z - 2)
            m20 = (x, y + 15, z - 2)
            m21 = (x + 1, y - 16, z + 2)
            m22 = (x - 1, y - 16, z + 2)
            m23 = (x + 1, y + 16, z - 2)
            m24 = (x - 1, y + 16, z - 2)
        
        moves = self.removeExtra([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14,
                m15,m16,m17, m18, m19, m20, m21, m22, m23, m24, m25])
#         print(moves)
            
        return moves

    def showValidKnightSq(self, validMoves):
        # Exclusive only to knight as we are hardcoding all possible positions
        for move in validMoves:
            if self.turn == 1 and move in self.pieces: # The square exist
                if self.pieces[move] == None: # The sq is empty
                    self.squares[move].setColor(0, 1, 0)
                elif self.pieces[move] != None:# The sq is not empty
                    if roundTuple(self.pieces[move].getColor()) != self.colorOfPiece:
                        # opponent piece
                        self.squares[move].setColor(0, 1, 0)
                    elif self.piece == self.pieces[move]: # Its initial square
                        self.squares[move].setColor(0, 1, 0)
            elif self.turn == 0 and move in self.inverseP: # The square exist
                if self.inverseP[move] == None: # The sq is empty
                    self.inverseS[move].setColor(0, 1, 0)
                elif self.inverseP[move] != None:# The sq is not empty
                    if roundTuple(self.inverseP[move].getColor()) != self.colorOfPiece:
                        # opponent piece
                        self.inverseS[move].setColor(0, 1, 0)
                    elif self.inverseP == self.inverseP[move]: # Its initial square
                        self.inverseS[move].setColor(0, 1, 0)
                        
    def findValidRookSq(self, currentSq = None): # Changes the color of valid squares into green
        if currentSq == None:
            currentSq = self.pieceKey
        posOfRook = currentSq
#         self.squares[posOfRook].setColor(0, 1, 0)
        x = posOfRook[0]
        y = posOfRook[1]
        z = posOfRook[2]
        validSq = [] 
        for i in range(9): # going positive x axis
            a = x + i
            potentialSq = (a, y, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
 
        for i in range(1, 9):# going neg x axis
            a = x - i
            potentialSq = (a, y, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 9):# going positive y axis
            a = y + i
            potentialSq = (x, a, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 9):# going neg y axis
            a = y - i
            potentialSq = (x, a, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3):# going positive z axis 
            a = z + i
            b = y + (i * 8) 
            potentialSq = (x, b, a) 
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3):# going neg z axis
            a = z - i
            b = y - (i * 8)
            potentialSq = (x, b, a)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
                
        for i in range(1, 3): # Upper level rights
            a = x + i
            b = y + (8 * i)
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
                
        for i in range(1, 3): # Upper level lefts
            a = x - i
            b = y + (8 * i)
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # lower level lefts
            a = x - i
            b = y - (8 * i)
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # lower level lefts
            a = x + i
            b = y - (8 * i)
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3):# Upper level ups
            a = x  
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # lower level down
            a = x 
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # upper level down
            a = x 
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
                
        for i in range(1, 3): # lower level ups
            a = x 
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        return validSq
    
    def findValidBishopSq(self, currentSq = None):# Changes the color of valid squares of bishop into green
        if currentSq == None:
            currentSq = self.pieceKey
        posOfBishop = currentSq
#         self.squares[posOfBishop].setColor(0, 1, 0)
        x = posOfBishop[0]
        y = posOfBishop[1]
        z = posOfBishop[2]
        validSq = []
        for i in range(9): # Top right corners
            a = x + i
            b = y + i
            potentialSq = (a, b, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 9): # Top left corners
            a = x - i
            b = y + i
            potentialSq = (a, b, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        continue
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        continue
        for i in range(1, 9): # Bottom left corners
            a = x - i
            b = y - i
            potentialSq = (a, b, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 9): # Bottom right corners
            a = x + i
            b = y - i
            potentialSq = (a, b, z)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # upper top right
            a = x + i
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # upper bottom right
            a = x + i
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # upper top left
            a = x - i
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # upper bottom left
            a = x - i
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
                
        for i in range(1, 3): # lower top right
            a = x + i
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # lower bottom right
            a = x + i
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # lower top left
            a = x - i
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        for i in range(1, 3): # lower bottom left
            a = x - i
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.turn == 1 and potentialSq in self.squares: # Square exist
                if self.pieces[potentialSq] == None: # The square is empty
                    validSq += [self.squares[potentialSq]]
                else: # When not empty
                    if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.squares[potentialSq]]
                        break
                    elif self.pieces[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.squares[potentialSq]]
                    else: # Alias pieces
                        break
            elif self.turn == 0 and potentialSq in self.inverseS:
                if self.inverseP[potentialSq] == None: # The square is empty
                    validSq += [self.inverseS[potentialSq]]
                else: # When not empty
                    if roundTuple(self.inverseP[potentialSq].getColor()) != self.colorOfPiece:
                        # Opponent piece
                        validSq += [self.inverseS[potentialSq]]
                        break
                    elif self.inverseP[potentialSq] == self.piece:
                        # Own initial position
                        validSq += [self.inverseS[potentialSq]]
                    else: # Alias pieces
                        break
        return validSq
    
    def findPawnMoves(self, currentSq = None):
        if currentSq == None:
            currentSq= self.pieceKey
        posOfPawn = currentSq
        colorOfPawn = roundTuple(self.piece.getColor()) 
        x = posOfPawn[0]
        y = posOfPawn[1]
        z = posOfPawn[2]
        
        attackingMoves = []
        
        moves = [(x, y, z)]
        if self.turn == 1: # Light pawn
            moves += [(x, y + 1, z)]
            moves += [(x, y, z)] + [(x, y + 8, z + 1)] + [(x, y + 9, z + 1)]
            moves += [(x, y - 8, z - 1)] + [(x, y - 7, z - 1)]
            attackingMoves += [(x + 1, y + 1, z)] + [(x - 1, y + 1, z)]
            attackingMoves += [(x + 1, y + 9, z + 1)] + [(x - 1, y + 9, z + 1)]
            attackingMoves += [(x + 1, y - 9, z - 1)] + [(x - 1, y + 9, z - 1)]
            if y == -1:
                moves += [(x, y + 2, z)]
                moves += [(x, y + 18, z + 2)]
                moves += [(x, y + 16, z + 2 )]
        if self.turn == 0:
            moves += [(x, y - 1, z)]
            moves += [(x, y, z)] + [(x, y + 8, z - 1)] + [(x, y + 9, z - 1)]
            moves += [(x, y + 8, z - 1)] + [(x, y + 9, z - 1)]
            moves += [(x, y - 8, z + 1)] + [(x, y - 7, z + 1)]
            attackingMoves += [(x + 1, y - 1, z)] + [(x - 1, y - 1, z)]
            attackingMoves += [(x + 1, y - 9, z + 1)] + [(x - 1, y - 9, z + 1)]
            attackingMoves += [(x + 1, y + 9, z - 1)] + [(x - 1, y + 9, z - 1)]
            if y == 20:
                moves += [(x, y - 2, z)]
                moves += [(x, y - 18, z + 2)]
                moves += [(x, y - 16, z + 2 )]
        attackingMoves = list(set(self.removeExtra(attackingMoves)))
        if "king" in str(self.piece):
            return attackingMoves
        for move in attackingMoves:
            if move in self.pieces and self.pieces[move] != None :
                moves += [move]
        moves = list(set(self.removeExtra(moves)))
        return moves
    
    def findKingMoves(self, square = None):
        if square == None:
            square = self.piece.getPos()
        ## print("king time")
        posOfKing = roundTuple(square)
#         self.colorOfPiece
        x = posOfKing[0]
        y = posOfKing[1]
        z = posOfKing[2]

        if self.turn == 1:
            moves = [] + [(x, y, z)]
            moves += [(x + 1, y, z)] + [(x - 1, y, z)] 
            moves += [(x , y+ 1, z)] + [(x , y - 1, z)]
            moves += [(x + 1, y + 1, z)] + [(x - 1, y - 1, z)]
            moves += [(x - 1, y+ 1, z)] + [(x + 1, y - 1, z)]
            moves += [(x, y - 8, z - 1)] + [(x - 1, y + 8, z + 1)]
            moves += [(x + 1, y + 8, z + 1)] + [(x - 1, y + 8, z + 1)]
            moves += [(x + 1, y - 8, z - 1)] + [(x - 1, y - 8, z - 1)]
            moves += [(x, y + 9, z + 1)] + [(x , y - 9, z-1)]
            moves += [(x, y + 8, z + 1)] + [(x, y - 8, z - 1)] 
            moves += [(x, y + 7, z + 1)] + [(x, y - 7, z - 1)]
            moves += [(x + 1, y + 7, z + 1)] + [(x + 1, y - 7, z - 1)]
            moves += [(x - 1, y + 7, z + 1)] + [(x - 1, y - 7, z - 1)]
            moves += [(x + 1, y + 9, z + 1)] + [(x + 1, y - 9, z - 1)]
            moves += [(x - 1, y + 9, z + 1)] + [(x - 1, y - 9, z - 1)]
        elif self.turn == 0:
            moves = [] + [(x, y, z)]
            moves += [(x + 1, y, z)] + [(x - 1, y, z)] 
            moves += [(x , y+ 1, z)] + [(x , y - 1, z)]
            moves += [(x + 1, y + 1, z)] + [(x - 1, y - 1, z)]
            moves += [(x - 1, y+ 1, z)] + [(x + 1, y - 1, z)]
            moves += [(x, y + 8, z - 1)] + [(x - 1, y - 8, z + 1)]
            moves += [(x + 1, y - 8, z + 1)] + [(x - 1, y - 8, z + 1)]
            moves += [(x + 1, y + 8, z - 1)] + [(x - 1, y + 8, z - 1)]
            moves += [(x, y - 9, z + 1)] + [(x , y + 9, z-1)]
            moves += [(x, y - 8, z + 1)] + [(x, y + 8, z - 1)] 
            moves += [(x, y - 7, z + 1)] + [(x, y + 7, z - 1)]
            moves += [(x + 1, y - 7, z + 1)] + [(x + 1, y + 7, z - 1)]
            moves += [(x - 1, y - 7, z + 1)] + [(x - 1, y + 7, z - 1)]
            moves += [(x + 1, y - 9, z + 1)] + [(x + 1, y + 9, z - 1)]
            moves += [(x - 1, y - 9, z + 1)] + [(x - 1, y + 9, z - 1)]
        
        moves = list(set(self.removeExtra(moves))) # Perfect removal of extras 
        for cord in moves[:]: 
            if self.checkThreat(cord): 
                moves.remove(cord) 
        return moves
    
    def checkThreat(self, square):
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
                    
        #print("start checking pawn")
        findPotentialPawnPos = self.findPawnMoves(square)
        for pos in findPotentialPawnPos:
           if pos in self.pieces and self.pieces[pos] != None:
               if "pawn"  in str(self.pieces[pos]) :
                   if roundTuple(self.pieces[pos].getColor()) != self.colorOfPiece:
                       return True
    
    def checkPiece(self, potentialThreats, piece):
        for square in potentialThreats:
            if square in self.pieces and piece in str(self.pieces[square]):
                if self.colorOfPiece != self.pieces[square].getColor():
                    return True
        else:
            return False
    
# Removes the tuple cords that are outside the boards and tuple cords where the alies reside
    def removeExtra(self, moves):
        if self.turn == 1:
            for move in moves[:]:
                if move not in self.squares:
                    moves.remove(move)
                elif move in self.pieces and self.pieces[move] != None:
                    if roundTuple(self.pieces[move].getColor()) == self.colorOfPiece:
                        if self.piece != self.pieces[move]:
                            moves.remove(move)
        elif self.turn == 0:
            for move in moves[:]:
                if move not in self.inverseS:
                    moves.remove(move)
                elif move in self.inverseP and self.inverseP[move] != None:
                    if roundTuple(self.inverseP[move].getColor()) == self.colorOfPiece:
                        if self.piece != self.pieces[move]:
                            moves.remove(move)

        return moves
    
    # Given a list of tuples or list squares(path), this function will turn them green
    def showValidSq(self, validMoves):
        # Valid moves are in a list of tuples
        if self.turn == 1:
            for move in validMoves:
                if isinstance(move, type((1,2))) == False: 
                    move.setColor(0, 1, 0)
                elif isinstance(move, type((1,2))):
                    self.squares[move].setColor(0, 1, 0)
        elif self.turn == 0:
            for move in validMoves:
                if isinstance(move, type((1,2))) == False: 
                    move.setColor(0, 1, 0)
                elif isinstance(move, type((1,2))):
                    self.inverseS[move].setColor(0, 1, 0)
            
    def showValidQueenSq(self):
        validMoves = []
        validMoves += self.findValidRookSq()
        validMoves += self.findValidBishopSq()
        self.showValidSq(validMoves)
    # Not my function
    def setupLights(self):  # This function sets up some default lighting
        
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
    def __init__(self): # Initialization
        
        # Inheritance
        super().__init__()
        
        # Storing variables
        self.squares = {} # Keys are cords and the values are the object itself
        self.inverseS = {} # After switching 128 sq new born
        self.pieces = {}# Keys are cords and the values are the object itself
        self.inverseP = {} # New locations for the pieces
        self.sCord = {}# values are cords and the keys are the object itself
        self.pCord = {}# values are cords and the keys are the object itself
        self.recordColor = {} # squares are keys and color is the values
        self.records = {}
        
        # Forming the board and plcing the pieces
        self.formBoardAndPieces()
#         self.disable_mouse()
        
        # The light system
        self.setupLights()
        
        # Floating square of current location(blue)
        self.square  = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(1, -1, -0.99)
        self.square.setColor(0,0,1,1)
        
        # Accepting the commands
        self.accept("arrow_left", updateKeyMap, ["left"])
        self.accept("arrow_right", updateKeyMap, ["right"])
        self.accept("arrow_up", updateKeyMap, ["up"])
        self.accept("arrow_down", updateKeyMap, ["down"])
        self.accept("u", updateKeyMap, ["u"])
        self.accept("d", updateKeyMap, ["d"] )
        self.accept("enter", updateKeyMap, ["enter"])
        # Updating the required updates or calling the function every sec
        self.taskMgr.add(self.update, "update")
        self.dx = 1
        # For placing/ selecting/ moving piece
        self.piece = False
        self.colorOfPiece = None
        self.pieceKey = None
        self.turn = 1
        self.select = False
        
        self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],) # Any
        # For perfect viewing 
        self.camera.setPos(0.5,-20,25)
        self.camera.setHpr(0,-42.5,0)
                    
game = MilleniumChess()
game.run()
