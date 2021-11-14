from direct.showbase.ShowBase import *

class MyApp(ShowBase):
    def __init__(self):

        ShowBase.__init__(self)
        
        self.disable_mouse()
        
        
        self.p1 = loader.loadModel("models/pawn.egg")
        self.p1.reparentTo(render)
        self.p1.setPos(0,5,0)
        self.p1.setColor(0,0,0)
        
        self.p2 = loader.loadModel("models/pawn.egg")
        self.p2.reparentTo(render)
        self.p2.setPos(0,10,0)
        self.p2.setColor(0,255,0)
        
        self.p3 = loader.loadModel("models/pawn.egg")
        self.p3.reparentTo(render)
        self.p3.setPos(0,-10,0)
        self.p3.setColor(255,0,0)

        self.p4 = loader.loadModel("models/pawn.egg")
        self.p4.reparentTo(render)
        self.p4.setPos(1,10,0)
        self.p4.setColor(0,0,255)
        
        # Ground floor

        
        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(3,13,0)
        self.sq1.setColor(0,0,0)

        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(2,12,0)
        self.sq1.setColor(0,0,0)

        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(1,11,0)
        self.sq1.setColor(0,0,0)
        
        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(0,10,0)
        self.sq1.setColor(0,0,0)

        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(-1,11,0)
        self.sq1.setColor(0,0,0)

        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(-2,12,0)
        self.sq1.setColor(0,0,0)

        self.sq1 = loader.loadModel("models/square.egg")
        self.sq1.reparentTo(render)
        self.sq1.setPos(-3,13,0)
        self.sq1.setColor(0,0,0)

        self.sq2 = loader.loadModel("models/square.egg")
        self.sq2.reparentTo(render)
        self.sq2.setPos(0,9,0)
        self.sq2.setColor(255,255,255)

        self.sq3 = loader.loadModel("models/square.egg")
        self.sq3.reparentTo(render)
        self.sq3.setPos(0,11,0)
        self.sq3.setColor(255,255,255)
        
        # 1st Floor
        
        self.sq4 = loader.loadModel("models/square.egg")
        self.sq4.reparentTo(render)
        self.sq4.setPos(0,10,1)
        self.sq4.setColor(255,0,255)


        self.setBackgroundColor(125,125,0)
        self.camera.setPos(0,-3,6)
        self.camera.setHpr(0,-30,0)


app = MyApp()
app.run()