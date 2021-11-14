from direct.showbase.ShowBase import *
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import LPoint3, LVector3, BitMask32

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

    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
        
app = MyApp()
app.run()
 
        
