from direct.showbase.ShowBase import *

class MyApp(ShowBase):
    def __init__(self):
        self.squares1= []
        self.pieces1 = []
        self.squares2= []
        self.pieces2 = []
        self.squares3= []
        self.pieces3 = []
        for index in range (64):
            self.squares1+= [index]
            self.squares2+= [index]
            self.squares3+= [index]
            self.pieces1 += [index]
            self.pieces2 += [index]
            self.pieces3 += [index]
            
        
            
#         print(self.sq)
        ShowBase.__init__(self)
        
#         self.disable_mouse()
        
        for z in range (-1,2):
            index = -1
            count= 1
        
            for x in range(-3,5):
                # going to next row
                for y in range(13,5,-1):
                    index += 1
                    # going throug a constant row
                    if count % 2 == 0:
                        self.squares1[index] = loader.loadModel("models/square.egg")
                        self.squares1[index].reparentTo(render)
                        self.squares1[index].setPos(x-(8 * z),y,abs(z))
                        self.squares1[index].setColor(0,0,0)
    #                     count+= 1
                    else:
                        self.squares1[index] = loader.loadModel("models/square.egg")
                        self.squares1[index].reparentTo(render)
                        self.squares1[index].setPos(x-(8 * z),y,abs(z))
                        self.squares1[index].setColor(255,255,255)
    #                     count+= 1
    #             count+= 1
    #             
    #         index = -1
    #         count= 1
    #         for x in range(-3,5):
    #             # going to next row
    #             for y in range(13,5,-1):
    #                 index += 1
    #                 # going throug a constant row
                    if y == 12:
                        self.pieces1[index] = loader.loadModel("models/pawn.egg")
                        self.pieces1[index].reparentTo(render)
                        self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                        self.pieces1[index].setColor(0,125,0)
                        
                    elif y == 7:
                        self.pieces1[index] = loader.loadModel("models/pawn.egg")
                        self.pieces1[index].reparentTo(render)
                        self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                        self.pieces1[index].setColor(255,0,0)
                        
                    if (x, y) in [(-3, 13), (4,13), (-3,6), (4,6)]:
                        if y == 13:
                            self.pieces1[index] = loader.loadModel("models/rook.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(0,125,0)
                        elif y == 6:
                            self.pieces1[index] = loader.loadModel("models/rook.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(255,0,0)
                    if (x, y) in [(-2, 13), (3,13), (-2,6), (3,6)]:
                        if y == 13:
                            self.pieces1[index] = loader.loadModel("models/knight.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(0,125,0)
                        elif y == 6:
                            self.pieces1[index] = loader.loadModel("models/knight.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(255,0,0)
                    if (x, y) in [(-1, 13), (2,13), (-1,6), (2,6)]:
                        if y == 13:
                            self.pieces1[index] = loader.loadModel("models/bishop.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(0,125,0)
                        elif y == 6:
                            self.pieces1[index] = loader.loadModel("models/bishop.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(255,0,0)
                    if (x, y) in [(0, 13), (0,6)]:
                        if y == 13:
                            self.pieces1[index] = loader.loadModel("models/king.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(0,125,0)
                        elif y == 6:
                            self.pieces1[index] = loader.loadModel("models/king.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(255,0,0)
                    if (x, y) in [(1, 13), (1,6)]:
                        if y == 13:
                            self.pieces1[index] = loader.loadModel("models/queen.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(0,125,0)
                        elif y == 6:
                            self.pieces1[index] = loader.loadModel("models/queen.egg")
                            self.pieces1[index].reparentTo(render)
                            self.pieces1[index].setPos(x-(8 * z),y,abs(z))
                            self.pieces1[index].setColor(0.525,0.525,0.525,0)
                        
                    count+= 1
                count+= 1

            
        
        self.setBackgroundColor(0.5,0.5,0)
        self.camera.setPos(0,-7,10)
        self.camera.setHpr(0,-30,0)
        
app = MyApp()
app.run()
 
        

