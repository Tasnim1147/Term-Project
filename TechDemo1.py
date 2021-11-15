from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

# Moving a piece in all diection without subsituting error and without continuous pressing of enter key

keyMap = {
        "up" : False,
        "down" : False,
        "left": False,
        "right": False,
         "u": False,
          "d": False,
        "enter":False,
        "space":False}

# Changes the above dictionary based on the latest key input
def updateKeyMap(key, state): # Not my function
    keyMap[key] = state
    
    
# changes a rgb code into a range between 0 and 1 values 
def color(r,g,b):
    return((r/255,g/255,b/255))

# Main class
class MyApp(ShowBase):
    def __init__(self):
        self.squares = [] # Storing the models of square
        self.pieces = [] # Storing the models of pieces
        for index in range (192): # 3 chess boards. (3 * 64 = 192)
            self.squares += [index]
            self.pieces += [index]
            

        ShowBase.__init__(self)
        # Inheriting all the attributes of Showbase class
        
        self.disable_mouse()
        # Comment this out for free mouse movement
        
        index = -1
        for z in range (-1,2): # For the upper chess boards
            count= 1
            for x in range(-3,5): # Random range of 8 unit gap
                # going to next row
                for y in range(13,5,-1): # Random range of 8 unit gap
                    index += 1
                    # going through a next column
                    if count % 2 == 0: # For black squares
                        self.squares[index] = loader.loadModel("models/square.egg")
                        # Loading the egg file
                        self.squares[index].reparentTo(render)
                        # Adding to parent node
                        self.squares[index].setPos(x - (8 * z), y, abs(z))
                        # Setting the location
                        self.squares[index].setColor(0,0,0)
                        # Black color code
                    else:
                        self.squares[index] = loader.loadModel("models/square.egg")
                        self.squares[index].reparentTo(render)
                        self.squares[index].setPos(x - (8 * z), y, abs(z))
                        self.squares[index].setColor(1, 1, 1) # white color code
                    if y == 12:
                        self.pieces[index] = loader.loadModel("models/pawn.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x-(8 * z),y,abs(z))
                        self.pieces[index].setColor(1, 1, 1) # white pawns
                        
                    elif y == 7:
                        self.pieces[index] = loader.loadModel("models/pawn.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x-(8 * z),y,abs(z))
                        self.pieces[index].setColor(color(150, 75, 0)[0],
                            color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown pawns
                        
                    elif (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)]:
                        # Rock is at the four corners of the board
                        if y == 13:
                            self.pieces[index] = loader.loadModel("models/rook.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x- (8 * z), y, abs(z))
                            self.pieces[index].setColor(1, 1, 1) # White color code
                        elif y == 6:
                            self.pieces[index] = loader.loadModel("models/rook.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2])
                            # Brown color code
                            
                    elif (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]:
                        # Knights are beside the rook at the four corners of the board
                        if y == 13:
                            self.pieces[index] = loader.loadModel("models/knight.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x - (8 * z), y, abs(z))
                            self.pieces[index].setColor(1, 1, 1) # White color code
                        elif y == 6:
                            self.pieces[index] = loader.loadModel("models/knight.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x - (8 * z), y, abs(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],
                                color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown color  code
                            
                    elif (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]:
                        # Bishops beside the knights
                        if y == 13:
                            self.pieces[index] = loader.loadModel("models/bishop.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x-(8 * z), y, abs(z))
                            self.pieces[index].setColor(1, 1, 1) # White color code
                        elif y == 6:
                            self.pieces[index] = loader.loadModel("models/bishop.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x-(8 * z), y, abs(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],
                                    color(150, 75, 0)[1],color(150, 75, 0)[2]) # Brown color
                    elif (x, y) in [(0, 13), (0,6)]:
                        if y == 13:
                            self.pieces[index] = loader.loadModel("models/king.egg")
                            # White king at white square
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x- (8 * z), y, abs(z))
                            self.pieces[index].setColor(1, 1, 1)
                        elif y == 6:
                            self.pieces[index] = loader.loadModel("models/king.egg")
                            # Brown king at dark square
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],
                                        color(150, 75, 0)[1],color(150, 75, 0)[2])
                    elif (x, y) in [(1, 13), (1,6)]:
                        if y == 13:
                            self.pieces[index] = loader.loadModel("models/queen.egg")
                            # Remaining is the queens
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x - (8 * z), y, abs(z))
                            self.pieces[index].setColor(1,1,1)
                        elif y == 6:
                            self.pieces[index] = loader.loadModel("models/queen.egg")
                            self.pieces[index].reparentTo(render)
                            self.pieces[index].setPos(x - (8 * z), y, abs(z))
                            self.pieces[index].setColor(color(150, 75, 0)[0],
                                        color(150, 75, 0)[1],color(150, 75, 0)[2])
                        
                    count+= 1
                count+= 1

        self.square = loader.loadModel("models/square.egg") # The blue square
        self.square.reparentTo(render)
        self.square.setPos(4,10,0.01)
        # Minimum height is required to be visible
        self.square.setColor(0,0,1)
        # Blue color code
            
        
        self.setBackgroundColor(color(0,0,125)[0],
                                color(0,125,0)[1],color(0,0,125)[2]) # Any
        self.camera.setPos(0.5, -7, 10)
        # 0.5 along x and -7 along y and 10 along z
        self.camera.setHpr(0, -30, 0)
        # Heading 0 degree, pitch -30 and roll 0 degree
        self.setupLights()
        
        # Takes the inputs
        self.accept("arrow_left", updateKeyMap, ["left", True])
        self.accept("arrow_right", updateKeyMap, ["right", True])
        self.accept("arrow_up", updateKeyMap, ["up", True])
        self.accept("arrow_down", updateKeyMap, ["down", True])
        self.accept("u", updateKeyMap, ["u", True])
        self.accept("d", updateKeyMap, ["d", True])
        self.accept("enter", updateKeyMap, ["enter", True])
        
        self.dx = 1 # Change in position in any axis
        
        self.pieceSelected = False
        
        self.taskMgr.add(self.update, "update") # Calls the self.update funtion each frame
        
        self.select = None
        
    def update(self, task):
        
        posOfSq = self.square.getPos() # Position of the blue square
        
        if keyMap["left"]: # Moves left
            posOfSq.x -= self.dx
            keyMap["left"] = False
            # Changing the board if necessary
            if posOfSq.x < -3:
                self.camera.setPos(-6,-7,10)
                posOfSq.setZ(1.001)
            elif -3 <= posOfSq.x <= 4:
                self.camera.setPos(0.5,-7,10)
                posOfSq.setZ(0.001)
                
        elif keyMap["right"]:# Moves right
            posOfSq.x += self.dx
            keyMap["right"] = False
            # Changing the board if necessary
            if -3 <= posOfSq.x <= 4:
                self.camera.setPos(0.5,-7,10)
                posOfSq.setZ(0.001)
            elif posOfSq > 4:
                self.camera.setPos(7,-7,10)
                posOfSq.setZ(1.001)
                
        elif keyMap["up"]: # Moves along +y
            posOfSq.y += self.dx
            keyMap["up"] = False
            
        elif keyMap["down"]: # Moves along -y
            posOfSq.y -= self.dx
            keyMap["down"] = False
            
        elif keyMap["u"]: # Moves +z
            posOfSq.z += self.dx
            keyMap["u"] = False
            
        elif keyMap["d"]: # Moves -z
            posOfSq.z -= self.dx
            keyMap["d"] = False
            
        self.square.setPos(posOfSq) # Reseting the blue square's position
        
        if keyMap["enter"]: # Selecting/ placing a piece
            if self.select == None and self.pieceSelected == False:
                for i in range(192): # 3 boards
                    if isinstance(self.pieces[i], int) == False:
                        # Non objects are filled with integers; requires changes
                        posOfPiece = self.pieces[i].getPos()
                        # Getting the position of corresponding piece
                        if self.compare(posOfPiece, posOfSq) :
                            # Checks for the identical positions
                            self.select = i # Stores that piece
                            # reseting the values
                            self.pieceSelected = True
                            keyMap["enter"] = False
                            break
                else:
                    keyMap["enter"] = False
                    
            elif self.select != None and self.pieceSelected != False:
                self.select = None
                self.pieceSelected = False
                keyMap["enter"] = False
                
        elif self.select != None and keyMap["enter"] == False:
            self.pieces[self.select].setPos(posOfSq)
            # Moving the piece with the blue square
            
        return task.cont # For infinite call

    def setupLights(self): # Not my function
        # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
    def compare(self, p1, p2):
        # Checks whether a square has the provided chess piece
        if abs(p1.getX() - p2.getX()) <= 0.05 and p1.getY() == p2.getY():
            if abs(p1.getZ() - p2.getZ()) <= 0.05:
                return True
            else:
                return False
        else:
            return False
        
app = MyApp()
app.run()
 
        


