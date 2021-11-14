from cmu_112_graphics import *
import random

def appStarted(app): # Model
    app.timerDelay = 100
    app.colors = ["red", "green", "yellow", "blue"]
    app.initialColors = ["red", "green", "yellow", "blue"]
    app.lightColor = [] +[random.choice(["lightyellow", "lightblue", "lightgreen", "#E25F61"])]
    app.blip = 0
    app.userInputs = None
    app.turn = 0
    app.index = 0
    app.counter = 0
    app.cords = ()
    app.on = False
    app.lvl = 1
    app.click = -1
    app.mode = None
    app.timer = 0
    app.difficulty = 5
    app.textSize = int(min(app.width, app.height) * 0.05)
    app.phase = 1
    app.points = 0
    app.flash = False
    app.blips = 0
    app.userColors = []
    app.inputColors = []
    app.timer = 10
    pass

def timerFired(app):
    if app.phase == 2:
        checkPhase(app)
        app.blip += 1
        if app.blip % app.difficulty == 0:
    #         app.timer
            if app.turn == 0:
                if app.on:
                    app.cords = colorCords(app)
                else:
                    app.cords = ()
                app.on = not app.on
        if app.turn == 1:
            if app.blip % 5 == 0:
                app.timer -= 0.5
                if app.timer == 0:
                    app.phase = 3
                pass
            pass
        if app.click + 1 == len(app.lightColor):
#                     app.phase = 3
            app.lightColor.append(random.choice(["lightyellow", "lightblue","lightgreen","#E25F61"]))
            app.turn = 0
            app.click = -1
            app.lvl += 1
            app.counter = 0
            app.timer = 10
            app.inputColors = []

def mousePressed(app, event):
        
    if app.phase == 2:
        if app.turn == 1:
            app.click += 1
            x = event.x
            y = event.y
            locateClick(app, x, y)
            recordClick(app)
            
def checkPhase(app):
    if app.userInputs == app.lightColor[app.click]:
        print("entered")
        print(app.userInputs)
        app.points += 1
        if app.click + 1 == len(app.lightColor):
    #                     app.phase = 3
            app.lightColor.append(random.choice(["lightyellow", "lightblue","lightgreen","#E25F61"]))
            app.turn = 0
            app.click = -1
            app.lvl += 1
            app.counter = 0
            app.timer = 10
            app.inputColors = []
            
    #                 else:
    #                     pass
    #                     print(app.click, app.lightColor, app.userInputs)
    #                     app.phase = 3

    else:
        print(app.click, app.lightColor, app.userInputs, "2nd")
        app.phase = 3
                
def recordClick(app):
    if app.userInputs == "lightgreen":
        app.inputColors  += ["G"]
    elif app.userInputs == "lightblue":
        app.inputColors += ["B"]
    elif app.userInputs == "lightyellow":
        app.inputColors += ["Y"]
    elif app.userInputs == "#E25F61":
        app.inputColors += ["R"]
    elif app.userInputs == "N":
        app.inputColors = app.inputColors[1:] + [""]


def locateClick(app, x, y):
    if x > 0 and x <= app.width//2:
        if y > 0 and y <= app.height // 2:
            app.userInputs = "lightgreen"
        elif y > app.height // 2 and y <= app.height:
            app.userInputs = "lightyellow"
    elif x > app.width // 2 and x <= app.width:
        if y > 0 and y <= app.height // 2:
            app.userInputs = "#E25F61"
        elif y > app.height // 2 and y <= app.height:
            app.userInputs = "lightblue"
    else:
        app.userInputs = "N"
    
        
def colorCords(app):
    if app.counter < app.lvl:
        color = app.lightColor[app.counter]
        app.counter += 1
        if color == "lightgreen":
            return ((0,0,app.width//2,app.height//2, color))
        elif color == "lightblue":
            return ((app.width//2,app.height//2,app.width,app.height, color))
        elif color == "lightyellow":
            return ((0,app.height//2,app.width//2,app.height, color))
        elif color == "#E25F61":
            return (app.width//2,0,app.width,app.height//2,color)
    else:
        app.turn = 1
                
                
def keyPressed(app, event):
    if app.phase == 1 and event.key in "123":
        changeDifficulty(app, event)
    elif app.phase == 2:
        if app.turn == 1:
            app.userColors.append(event.key)
            
            pass 
            
            
def changeDifficulty(app, event):
    if event.key == 1:
        app.difficulty = 1
    elif event.key == 2:
        app.difficulty = 2
    else:
        app.difficulty = 5
    app.phase = 2
    
def drawPhase1(app, canvas):
    canvas.create_rectangle(0,0,app.width, app.height, fill = "white")
    canvas.create_text(app.width //2, app.height // 4 , text = "Simon",
                       font = f"Arial {app.textSize} " )
    canvas.create_text(app.width //2, app.height // 4  * 3,
                       text = '''Press 1 for Easy\nPress 2 for Normal\nPress 3 for Hard''',
                       font = f"Arial {int(app.textSize * 0.5)} " )
    
def drawPhase2(app, canvas):
    canvas.create_rectangle(0,0,app.width//2,app.height//2, fill = app.colors[1], width = 10)
    canvas.create_rectangle(app.width//2,app.height//2,app.width,app.height, fill = app.colors[-1], width = 10)
    canvas.create_rectangle(app.width//2,0,app.width,app.height//2, fill = app.colors[0], width = 10)
    canvas.create_rectangle(0,app.height//2,app.width//2,app.height, fill = app.colors[2], width = 10)
    if app.cords:
        i = app.cords
        (x0,y0,x1,y1) = (i[0],i[1],i[2],i[3])
        canvas.create_rectangle(x0,y0,x1,y1,fill = i[4])
    canvas.create_rectangle(app.width//3 , 0,app.width//3 * 2, app.height // 10, fill ="#FFCA00",width=1)
    if len(app.inputColors) == 0:
        pass
    elif len(app.inputColors) == 1:
        canvas.create_text(app.width//2 ,app.height // 20, text = str(app.inputColors[0]), font = "Arial 16 bold")
    elif len(app.inputColors) == 2:
        canvas.create_text(app.width//2 - app.width//48 ,app.height // 20, text = str(app.inputColors[0]), font = "Arial 16 bold")
        canvas.create_text(app.width//2 + app.width//48 ,app.height // 20, text = str(app.inputColors[1]), font = "Arial 16 bold")
    elif len(app.inputColors) >= 3:
        canvas.create_text(app.width//2 - app.width//24 ,app.height // 20, text = str(app.inputColors[-3]), font = "Arial 16 bold")
        canvas.create_text(app.width//2  ,app.height // 20, text = str(app.inputColors[-2]), font = "Arial 16 bold")
        canvas.create_text(app.width//2 + app.width//24 ,app.height // 20, text = str(app.inputColors[-1]), font = "Arial 16 bold")
    if app.turn == 1:
        canvas.create_text(25,25,text = f"{app.timer}", font = "Arial 10")
        
def drawPhase3(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill = "white")
    canvas.create_text(app.width // 2, app.height//4, text = "Game Over", font = "Arial {int(app.textSize * 0.5)} bold")


def redrawAll(app, canvas):
    if app.phase == 1:
        drawPhase1(app,canvas)
    elif app.phase == 2:
        drawPhase2(app, canvas)
    elif app.phase == 3:
        drawPhase3(app, canvas)
        
runApp(width = 800, height = 800)

    
