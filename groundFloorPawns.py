from direct.showbase.ShowBase import *

class MyApp(ShowBase):
    def __init__(self):
        self.squares= []
        self.pawns = []
        self.KBR = []
        for squares in range (64):
            self.squares+= [squares]
        for pawns in range(16):
            self.pawns += [pawns]
        
            
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
                
                # going throug a constant row
                if y == 12:
                    index += 1
                    self.pawns[index] = loader.loadModel("models/pawn.egg")
                    self.pawns[index].reparentTo(render)
                    self.pawns[index].setPos(x,y,0)
                    self.pawns[index].setColor(0,125,0)
                    count+= 1
                elif y == 7:
                    index += 1
                    self.pawns[index] = loader.loadModel("models/pawn.egg")
                    self.pawns[index].reparentTo(render)
                    self.pawns[index].setPos(x,y,0)
                    self.pawns[index].setColor(255,0,0)
                    count+= 1
            count+= 1
            
            
#             index += 1
        
        self.setBackgroundColor(125,125,0)
        self.camera.setPos(0,-3,6)
        self.camera.setHpr(0,-30,0)
        
app = MyApp()
app.run()
 
        