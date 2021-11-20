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
        self.square.setPos(4,10,0.01)
        self.square.setColor(0,0,1)
        
        for element in self.pieces[:]:
            if isinstance(element, int):
                self.pieces.remove(element)
        
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
                            break
#                         print(l)
#                         if len(l) > 31:
#                             print(l)
#                             return task.done
                            
                
                else:
                    keyMap["enter"] = False
                    
            elif self.select != None and self.pieceSelected != False:
                self.select = None
                self.pieceSelected = False
                keyMap["enter"] = False
        elif self.select != None and keyMap["enter"] == False:
            self.pieces[self.select].setPos(posOfSq)
        self.square.setPos(posOfSq)
        return task.cont
    
    def showMoves(self, piece):
        legalSquares =  self.getMoves(piece)
        if legalSquares != None:
            for m in legalSquares:
                for index in range(192):
                    if check(m,tuple(self.squares[index].getPos()) ):
                        self.squares[index].setColor(0,1,0)

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
        colorOfPawn = piece.getColor()
#         temp = posOfPawn
        print(colorOfPawn)
        if colorOfPawn[0] < 1 and colorOfPawn[1] < 1 and colorOfPawn[2] < 1 :
            m1 = (posOfPawn.getX(),posOfPawn.getY() + 1,posOfPawn.getZ())
            m2 = (posOfPawn.getX(),posOfPawn.getY() + 2,posOfPawn.getZ())
            m3 = (posOfPawn.getX(),posOfPawn.getY()+8 ,posOfPawn.getZ() + 1)
            m4 = (posOfPawn.getX(),posOfPawn.getY() + 9,posOfPawn.getZ() + 1)
            m5 = (posOfPawn.getX(),posOfPawn.getY()+16 ,posOfPawn.getZ() + 2)
            m6 = (posOfPawn.getX(),posOfPawn.getY() + 18,posOfPawn.getZ() + 2)
            print(m1, m2, m3, m4,m5,m6)
            return [m1, m2, m3, m4,m5,m6]
        elif colorOfPawn[0] == 1 and colorOfPawn[1] == 1 and colorOfPawn[2] == 1 :
            m1 = (posOfPawn.getX(),posOfPawn.getY() - 1,posOfPawn.getZ())
            m2 = (posOfPawn.getX(),posOfPawn.getY() - 2,posOfPawn.getZ())
            print(m1, m2)
            return [m1, m2]

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