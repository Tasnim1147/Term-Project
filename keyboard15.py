from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32, LPoint3f
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

keyMap = {
        "up" : False,
        "down" : False,
        "left": False,
        "right": False,
         "u": False,
          "d": False,
        "enter":False,
        "space":False}

def updateKeyMap(key):
    keyMap[key] = True
    
def check(p1,p2):
    return p1 == p2
    


def color(r,g,b):
    return((r/255,g/255,b/255))





class MilleniumChess(ShowBase):
    def formBoardAndPieces(self):
        
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
                        self.squares[index].setPos(x,y+(8 * z) ,(z))
                        self.squares[index].setColor(0,0,0)
    #                     count+= 1
                    else:
                        self.squares[index] = loader.loadModel("models/square.egg")
                        self.squares[index].reparentTo(render)
                        self.squares[index].setPos(x ,y+(8 * z),(z))
                        self.squares[index].setColor(1,1,1)
                    if y == 12 and z != 0  and z != -1:
                        self.pieces[index] = loader.loadModel("models/pawn.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x ,y+(8 * z),(z))
                        self.pieces[index].setColor(1,1,1)
                        
                    elif y == 7 and z != 0 and z != 1:
                        self.pieces[index] = loader.loadModel("models/pawn.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y+(8 * z),(z))
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                        
                    elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)] and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[index] = loader.loadModel("models/rook.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[index] = loader.loadModel("models/rook.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[index] = loader.loadModel("models/knight.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[index] = loader.loadModel("models/knight.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[index] = loader.loadModel("models/bishop.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[index] = loader.loadModel("models/bishop.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(0, 13), (0,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[index] = loader.loadModel("models/king.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[index] = loader.loadModel("models/king.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(1, 13), (1,6)]and z != 0:
                        if y == 13 and z != -1:
                            self.pieces[index] = loader.loadModel("models/queen.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(1,1,1)
                        elif y == 6 and z != 1:
                            self.pieces[index] = loader.loadModel("models/queen.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x,y+(8 * z),(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                        
                    count+= 1
                count+= 1
    
        self.square = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(4,0,-0.99)
        self.square.setColor(0,0,1)
        
        for element in self.pieces[:]:
            if isinstance(element, int):
                self.pieces.remove(element)
                
    def redrawSquares(self):
        index = -1
        for z in range (-1,2):
            
            count= 1
        
            for x in range(-3,5):
                # going to next row
                for y in range(13,5,-1):
                    index += 1
                    # going throug a constant row
                    if count % 2 == 0:
#                         self.squares[index].setPos(x,y+(8 * z) ,(z))
                        self.squares[index].setColor(0,0,0)
    #                     count+= 1
                    else:
#                         self.squares[index].setPos(x ,y+(8 * z),(z))
                        self.squares[index].setColor(1,1,1)
                    count += 1
                count += 1
                    
        
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
    def compare(self, p1, p2):
        if abs(p1.getX() - p2.getX()) <= 0.05 and p1.getY() == p2.getY():
            if abs(p1.getZ() - p2.getZ()) <= 0.05:
                return True
            else:
                return False
        else:
            return False
        
    def update(self, task):
        posOfSq = self.square.getPos()
        if keyMap["left"]:
            posOfSq.x -= self.dx
            keyMap["left"] = False
            if posOfSq.x < -3:
                posOfSq.setX(4)

        elif keyMap["right"]:
            posOfSq.x += self.dx
            keyMap["right"] = False
            if posOfSq.x > 4:
                posOfSq.setX(-3)
        elif keyMap["up"]:
            posOfSq.y += self.dx
            keyMap["up"] = False
            if 13 >= posOfSq.y > 5  :
                posOfSq.setZ(0.01)
            elif 21 >= posOfSq.y > 13  :
                posOfSq.setZ(1.01)
            elif 5 >= posOfSq.y > -2:
                posOfSq.setZ(-0.99)
            elif posOfSq.y > 21:
                posOfSq.setY(-2)
                posOfSq.setZ(-0.99)
        elif keyMap["down"]:
            posOfSq.y -= self.dx
            keyMap["down"] = False
            if 13 >= posOfSq.y > 5  :
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
            if self.select == None and self.pieceSelected == False:
                l = []
                for i in range(32):
                    if isinstance(self.pieces[i], int) == False:
                        posOfPiece = self.pieces[i].getPos()
                        if self.compare(posOfPiece, posOfSq) :
                            self.select = i
                            self.pieceSelected = True
                            keyMap["enter"] = False
                            print(self.pieces[self.select])
                            self.showMoves(self.pieces[self.select])
                            self.initialPosition = self.pieces[self.select].getPos()
                            break
                            
                
                else:
                    keyMap["enter"] = False
                    
            elif self.select != None and self.pieceSelected != False:
                if self.checkPlacement(posOfSq):
                    self.pieces[self.select].setPos(posOfSq)
                    print(self.pieces.count(self.pieces[self.select]))
                    self.pieceSelected = False
                    keyMap["enter"] = False
                    self.redrawSquares()
                    self.initialPosition = None
                    posOfSq.z = self.pieces[self.select].getZ() + 0.01
                    self.select = None
                    
                else:
                    print("not allowed")
                    self.pieces[self.select].setPos(self.initialPosition)
                    self.pieceSelected = False
                    self.redrawSquares()
                    self.initialPosition = None
                    posOfSq.z = self.pieces[self.select].getZ() + 0.01
                    self.select = None
        elif self.select != None and keyMap["enter"] == False:
            self.pieces[self.select].setPos(posOfSq)
        self.square.setPos(posOfSq)
        return task.cont
    
    def checkPlacement(self, position):
        position.setZ(round(position.getZ()))
        for index in range(192):
            targetSq = self.squares[index]
            if targetSq.getPos() == position and targetSq.getColor() == (0,1,0,1):
                return True
            
    def checkForSameColorPieces(self, squares, piece):
        for square in squares:
            if square != tuple(piece.getPos()):
                for piece in self.pieces:
                    if tuple(piece.getPos()) == square:
                        self.changeColor(square, (1,0,0))
                        
    def changeColor(self, cords, color):
        for index in range(len(self.squares)):
            if tuple(self.squares[index].getPos()) == cords:
                self.squares[index].setColor(1, 0, 0)
                break
    
    def checkForBlockingPiece(self, squares, piece):
        pass
        
                
    
    def showMoves(self, piece):
        legalSquares =  self.getMoves(piece)
        if legalSquares != None:
            for m in legalSquares:
                for index in range(192):
                    if check(m,tuple(self.squares[index].getPos()) ):
                        self.squares[index].setColor(0,1,0,1)
            self.checkForSameColorPieces(legalSquares, piece)

    def getMoves(self, piece):
        nameOfPiece= str(piece).split("/")[1]
        if "pawn" in nameOfPiece:
            return self.findPawnMoves(piece)
        elif "knight" in nameOfPiece:
            return self.findKnightMoves(piece)
        elif "bishop" in nameOfPiece:
            return self.findBishopMoves(piece)
        elif "queen" in nameOfPiece:
            return self.findQueenMoves(piece)
        elif "king" in nameOfPiece:
            return self.findKingMoves(piece)
        elif "rook" in nameOfPiece:
            return self.findRookMoves(piece)
        pass
        
    def findPawnMoves(self, piece):
        print("pawn time")
        posOfPawn = piece.getPos()
        print(posOfPawn)
        colorOfPawn = piece.getColor()
        x = posOfPawn.getX()
        y = posOfPawn.getY()
        z = round(posOfPawn.getZ())
        points = []
        if colorOfPawn[0] < 1 and colorOfPawn[1] < 1 and colorOfPawn[2] < 1 :
            points += [(x, y + 1, z)]
            points += [(x, y, z)] + [(x, y + 8, z + 1)] + [(x, y + 9, z + 1)]
            points += [(x, y - 8, z - 1)] + [(x, y - 7, z - 1)]
            if y == -1:
                points += [(x, y + 2, z)]
                points += [(x, y + 18, z+2)]
                points += [(x, y + 16, z + 2 )]
        elif colorOfPawn[0] == 1 and colorOfPawn[1] == 1 and colorOfPawn[2] == 1 :
            points += [(x, y - 1, z)]
            points += [(x, y, z)] + [(x, y - 8, z - 1)] + [(x, y - 9, z - 1)]
            points += [(x, y - 8, z - 1)] + [(x, y - 9, z - 1)]
            points += [(x, y + 8, z + 1)] + [(x, y + 7, z + 1)]
            if y == 20:
                points += [(x, y - 2, z)]
                points += [(x, y - 18, z - 2)]
                points += [(x, y - 16, z - 2 )]
        return points
        
    def findKnightMoves(self, piece):
        print("knight itme")
        posOfKnight = piece.getPos()
        colorOfKnight = piece.getColor()
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
        print(posOfKnight)
        print([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16])
        return [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24]
    
    def findBishopMoves(self, piece):
        print("bishop itme")
        posOfBishop = piece.getPos()
        x = posOfBishop.getX()
        y = posOfBishop.getY()
        z = round(posOfBishop.getZ())
        points = []
        for i in range (-8, 9):
            points += [(x + i, y + i, z)]
            points += [(x - i, y + i, z)]
            if i in [-2, -1, 0, 1, 2]:
                points += [(x + i, y + i + (i * 8), z + i)]
                points += [(x - i, y + i + (i * 8), z + i)]
                points += [(x + i, y + i - (i * 8), z - i)]
                points += [(x - i, y + i - (i * 8), z - i)]
        
        points = self.removeExtras(points)
        return points
    
    def findRookMoves(self, piece):
        print("rook time")
        posOfRook = piece.getPos()
        x = posOfRook.getX()
        y = posOfRook.getY()
        z = round(posOfRook.getZ())
        points = []
        for i in range(-8, 9):
            points += [(x, y + i, z)] + [(x + i, y, z)]
        for i in range(-2,3):
            points += [(x, y+i+ (8 * i), z + i )]
            points += [(x, y - i + (8 * i), z + i)]
            points += [(x + i, y + (8 * i), z + i )]
            points += [(x - i, y   + (8 * i), z + i)]
            points += [(x, y + (8 * i), z + i)]
            
        points = self.removeExtras(points)
        return points
    
    def findQueenMoves(self, piece):
        print("queens time")
        posOfQueen = piece.getPos()
        x = posOfQueen.getX()
        y = posOfQueen.getY()
        z = round(posOfQueen.getZ())
        points = []
        for i in range(-8, 9):
            points += [(x, y + i, z)] + [(x + i, y, z)]
        for i in range(-2,3):
            points += [(x, y+i+ (8 * i), z + i )]
            points += [(x, y - i + (8 * i), z + i)]
            points += [(x + i, y + (8 * i), z + i )]
            points += [(x - i, y   + (8 * i), z + i)]
            points += [(x, y + (8 * i), z + i)]
        for i in range (-8, 9):
            points += [(x + i, y + i, z)]
            points += [(x - i, y + i, z)]
            if i in [-2, -1, 0, 1, 2]:
                points += [(x + i, y + i + (i * 8), z + i)]
                points += [(x - i, y + i + (i * 8), z + i)]
                points += [(x + i, y + i - (i * 8), z - i)]
                points += [(x - i, y + i - (i * 8), z - i)]
        points = self.removeExtras(points)
        return points
    
    def findKingMoves(self, piece):
        print("king time")
        posOfKing = piece.getPos()
        x = posOfKing.getX()
        y = posOfKing.getY()
        z = round(posOfKing.getZ())
        points = []
        points += [(x + 1, y, z)] + [(x - 1, y, z)]
        points += [(x , y+ 1, z)] + [(x , y - 1, z)]
        points += [(x + 1, y + 1, z)] + [(x - 1, y - 1, z)]
        points += [(x - 1, y+ 1, z)] + [(x + 1, y - 1, z)]
        points += [(x , y - 8, z - 1)] + [(x - 1, y + 8, z + 1)]
        points += [(x + 1, y + 8, z + 1)] + [(x - 1, y + 8, z + 1)]
        points += [(x + 1, y - 8, z - 1)] + [(x - 1, y - 8, z - 1)]
        points += [(x , y+ 9, z+1)] + [(x , y - 9, z-1)]
        points += [(x, y + 8, z + 1)] + [(x, y - 8, z - 1)] + [(x, y, z)]
        points += [(x, y + 7, z + 1)] + [(x, y - 7, z - 1)]
        points += [(x + 1, y + 7, z + 1)] + [(x + 1, y - 7, z - 1)]
        points += [(x - 1, y + 7, z + 1)] + [(x - 1, y - 7, z - 1)]
        points += [(x + 1 , y+ 9, z+1)] + [(x + 1 , y - 9, z-1)]
        points += [(x - 1 , y+ 9, z+1)] + [(x - 1 , y - 9, z-1)]

        return points
        
    def removeExtras(self, l):
        validCords = []
        for square in self.squares:
            validCords += [square.getPos()]
        for cords in l[:]:
            if cords not in validCords:
                l.remove(cords)
        return l
    

    def __init__(self):
        
        super().__init__()
        
        self.disableMouse()
        
        self.squares = []
        self.pieces = []
        
        for index in range(192):
            self.squares += [index]
            self.pieces += [index]
                
        self.formBoardAndPieces()
        
        self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],)
        self.camera.setPos(0.5,-20,25)
        self.camera.setHpr(0,-42.5,0)
        self.setupLights()
        
        self.inputDevice = "keyboard"
        self.accept("arrow_left", updateKeyMap, ["left"])
        self.accept("arrow_right", updateKeyMap, ["right"])
        self.accept("arrow_up", updateKeyMap, ["up"])
        self.accept("arrow_down", updateKeyMap, ["down"])
        self.accept("u", updateKeyMap, ["u"])
        self.accept("d", updateKeyMap, ["d"] )
        self.accept("enter", updateKeyMap, ["enter"])
        
        self.dx = 1
        self.pieceSelected = False
        
        self.taskMgr.add(self.update, "update")
        
        self.select = None
        
        pass
    

            

game = MilleniumChess()
game.run()





