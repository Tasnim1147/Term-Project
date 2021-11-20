from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32, LPoint3f
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

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
def check(p1,p2):
    return p1 == p2
    

# Change the color format
def color(r,g,b):
    return((r/255,g/255,b/255))

class MilleniumChess(ShowBase):
    
    # Forms Board place the pieces
    # And draws the selected (floating) square
    def formBoardAndPieces(self):
        
        z = 0
        count = 1
        for x in range(-3,5):
            # going to next row
            for y in range(13,5,-1):
                # going throug a constant row
                if count % 2 == 0:
                    self.squares[(x, y, z)] = loader.loadModel("models/square.egg")
                    self.squares[(x, y, z)].reparentTo(render)
                    self.squares[(x, y, z)].setPos(x,y+(8 * z) ,(z))
                    self.squares[(x, y, z)].setColor(0,0,0)
#                     count+= 1
                else:
                    self.squares[(x, y, z)] = loader.loadModel("models/square.egg")
                    self.squares[(x, y, z)].reparentTo(render)
                    self.squares[(x, y, z)].setPos(x ,y+(8 * z),(z))
                    self.squares[(x, y, z)].setColor(1,1,1)
                if y == 12   and z != -1:
                    self.pieces[(x, y, z)] = loader.loadModel("models/pawn.egg")
                    self.pieces[(x, y, z)].reparentTo(render)
                    self.pieces[(x, y, z)].setPos(x ,y+(8 * z),(z))
                    self.pieces[(x, y, z)].setColor(1,1,1)
                    
                elif y == 7  and z != 1:
                    self.pieces[(x, y, z)] = loader.loadModel("models/pawn.egg")
                    self.pieces[(x, y, z)].reparentTo(render)
                    self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                    self.pieces[(x, y, z)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)] :
                    if y == 13 and z != -1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/rook.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(1,1,1)
                    elif y == 6 and z != 1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/rook.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]:
                    if y == 13 and z != -1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/knight.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(1,1,1)
                    elif y == 6 and z != 1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/knight.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]:
                    if y == 13 and z != -1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/bishop.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(1,1,1)
                    elif y == 6 and z != 1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/bishop.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                elif (x, y) in [(0, 13), (0,6)]:
                    if y == 13 and z != -1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/king.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(1,1,1)
                    elif y == 6 and z != 1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/king.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                elif (x, y) in [(1, 13), (1,6)]:
                    if y == 13 and z != -1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/queen.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(1,1,1)
                    elif y == 6 and z != 1:
                        self.pieces[(x, y, z)] = loader.loadModel("models/queen.egg")
                        self.pieces[(x, y, z)].reparentTo(render)
                        self.pieces[(x, y, z)].setPos(x,y+(8 * z),(z))
                        self.pieces[(x, y, z)].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                count+= 1
            count+= 1

    # Not my function
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
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
    
    def __init__(self):
        super().__init__()
        
        self.squares = {}
        self.pieces = {}
        
        self.formBoardAndPieces()
        
        self.disableMouse()
        
        self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],)
        
        self.camera.setPos(0.5,-10,16)
        self.camera.setHpr(0,-42.5,0)
        self.setupLights()
        
#         self.square
        
        self.accept("arrow_left", updateKeyMap, ["left"])
        self.accept("arrow_right", updateKeyMap, ["right"])
        self.accept("arrow_up", updateKeyMap, ["up"])
        self.accept("arrow_down", updateKeyMap, ["down"])
        self.accept("u", updateKeyMap, ["u"])
        self.accept("d", updateKeyMap, ["d"] )
        self.accept("enter", updateKeyMap, ["enter"])
        
        self.square = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(4,10,0.01)
        self.square.setColor(0,0,1)
        
        self.select = None
        self.pieceSelected = False
        self.dx = 1
        
        self.taskMgr.add(self.update, "update")
        
        
 

game = MilleniumChess()
game.run()


