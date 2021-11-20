from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
import sys

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

def updateKeyMap(key, state):
    keyMap[key] = state
    
    

def color(r,g,b):
    return((r/255,g/255,b/255))

class MyApp(ShowBase):
    def __init__(self):
        self.squares= []
        self.pieces = []
        for squares in range (64):
            self.squares+= [squares]
        for pieces in range(64):
            self.pieces += [pieces]
            
        
            
#         print(self.sq)
        ShowBase.__init__(self)
        
        self.disable_mouse()
        
        index = -1
        count= 1
        for x in range(-3,5):
            # going to next row
            for y in range(13,5,-1):
                index += 1
                # going throug a constant row
                if count % 2 == 0:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(render)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(0,0,0)
                    count+= 1
                else:
                    self.squares[index] = loader.loadModel("models/square.egg")
                    self.squares[index].reparentTo(render)
                    self.squares[index].setPos(x,y,0)
                    self.squares[index].setColor(255,255,255)
                    count+= 1
            count+= 1
            
        self.square = loader.loadModel("models/square.egg")
        self.square.reparentTo(render)
        self.square.setPos(0,10,0.01)
        self.square.setColor(0,0,1)     
            
        index = -1
        count= 1
        for x in range(-3,5):
            # going to next row
            for y in range(13,5,-1):
                index += 1
                # going throug a constant row
                if y == 12:
                    self.pieces[index] = loader.loadModel("models/pawn.egg")
                    self.pieces[index].reparentTo(render)
                    self.pieces[index].setPos(x,y,0)
                    self.pieces[index].setColor(1,1,1)
                    
                elif y == 7:
                    self.pieces[index] = loader.loadModel("models/pawn.egg")
                    self.pieces[index].reparentTo(render)
                    self.pieces[index].setPos(x,y,0)
                    self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                if (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/rook.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/rook.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/knight.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/knight.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/bishop.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/bishop.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(0, 13), (0,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/king.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/king.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                if (x, y) in [(1, 13), (1,6)]:
                    if y == 13:
                        self.pieces[index] = loader.loadModel("models/queen.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(1,1,1)
                    elif y == 6:
                        self.pieces[index] = loader.loadModel("models/queen.egg")
                        self.pieces[index].reparentTo(render)
                        self.pieces[index].setPos(x,y,0)
                        self.pieces[index].setColor(color(150, 75, 0)[0],color(150, 75, 0)[1],color(150, 75, 0)[2])
                    
                count+= 1
            count+= 1

        
        
        self.setBackgroundColor(color(0,0,125)[0],color(0,125,0)[1],color(0,0,125)[2],)
        self.camera.setPos(0.5,-3,6)
        self.camera.setHpr(0,-30,0)
        self.setupLights()
        
        self.accept("arrow_left", updateKeyMap, ["left", True])
        self.accept("arrow_right", updateKeyMap, ["right", True])
        self.accept("arrow_up", updateKeyMap, ["up", True])
        self.accept("arrow_down", updateKeyMap, ["down", True])
        self.accept("u", updateKeyMap, ["u", True])
        self.accept("d", updateKeyMap, ["d", True])
        self.accept("enter", updateKeyMap, ["enter", True])
        
        self.dx = 1
        self.pieceSelected = False
        
        self.taskMgr.add(self.update, "update")
        
        self.select = None
        
    def update(self, task):
        posOfSq = self.square.getPos()
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
            posOfSq.z += self.dx
            keyMap["u"] = False
        elif keyMap["d"]:
            posOfSq.z -= self.dx
            keyMap["d"] = False
        self.square.setPos(posOfSq)
        
        if keyMap["enter"]:
            if self.select == None and self.pieceSelected == False:
                for i in range(64):
                    if isinstance(self.pieces[i], int) == False:
                        posOfPiece = self.pieces[i].getPos()
                        if self.compare(posOfPiece, posOfSq) :
                            self.select = i
                            self.pieceSelected = True
                            keyMap["enter"] = False
                            break
            elif self.select != None and self.pieceSelected != False:
                self.select = None
                self.pieceSelected = False
                keyMap["enter"] = False
        elif self.select != None and keyMap["enter"] == False:
                self.pieces[self.select].setPos(posOfSq)
        return task.cont

    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
    def compare(self, p1, p2):
        if p1.getX() == p2.getX() and p1.getY() == p2.getY():
            if abs(p1.getZ() - p2.getZ()) <= 0.05:
                return True
            else:
                return False
        else:
            return False
        
app = MyApp()
app.run()
 
        






