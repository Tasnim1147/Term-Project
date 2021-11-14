from direct.showbase.ShowBase import *
from direct.task import Task
from direct.showbase import DirectObject
from direct.actor.Actor import Actor
from panda3d.core import LPoint3, LVector3, BitMask32
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib

def color(r,g,b):
    return((r/255,g/255,b/255))

def SquarePos(i):
#     print(LPoint3((i % 8) - 3.5, int(i // 8) - 3.5, 0))
    return LPoint3(1,10,0)

class ChessBoard(ShowBase):
    def __init__(self):
        
        ShowBase.__init__(self)
        
#         self.disable_mouse()
       
        self.mousePressed = taskMgr.add(self.mousePressed, 'mousePressed')
#         self.accept("mouse1",self.mousePressed )
        
        self.squares1 = loader.loadModel("models/square.egg")
        self.squares1.reparentTo(render)
        self.squares1.setPos(0,10,0)
        self.squares1.setColor(0,0,0)
        
        self.squares2 = loader.loadModel("models/square.egg")
        self.squares2.reparentTo(render)
        self.squares2.setPos(1,10,0)
        self.squares2.setColor(1,1,1)
        
        self.squares3= loader.loadModel("models/square.egg")
        self.squares3.reparentTo(render)
        self.squares3.setPos(1,9,0)
        self.squares3.setColor(0,0,0)
        
        self.squares4= loader.loadModel("models/square.egg")
        self.squares4.reparentTo(render)
        self.squares4.setPos(0,9,0)
        self.squares4.setColor(1,1,1)
        
        self.pawn = loader.loadModel("models/pawn.egg")
        self.pawn.reparentTo(render)
        self.pawn.setPos(0,9,0)
        self.pawn.setColor(color(125,0,255)[0],color(125,0,255)[1],color(125,0,255)[2])

#         if self.mouseWatcherNode.hasMouse():
#             # get the mouse position
#             mpos = self.mouseWatcherNode.getMouse()
#             print(mpos)
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,-7,10)
        self.camera.setHpr(0,-30,0)
        self.setupLights()
    
    def mousePressed(self, task):
        if self.mouseWatcherNode.hasMouse():
            # get the mouse position
            mpos = self.mouseWatcherNode.getMouse()
            print(mpos)
        
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
chess = ChessBoard()
chess.run()