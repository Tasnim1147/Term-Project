 1from direct.showbase.ShowBase import ShowBase
  2from direct.showbase.DirectObject import DirectObject
  3from direct.interval.IntervalGlobal import Sequence, Func, Wait
  4from panda3d.core import CollisionTraverser, CollisionHandlerEvent
  5from panda3d.core import CollisionNode, CollisionSphere
  6
  7
  8class World(DirectObject):
  9
 10    def __init__(self):
 11        # Initialize the traverser.
 12        base.cTrav = CollisionTraverser()
 13
 14        # Initialize the handler.
 15        self.collHandEvent = CollisionHandlerEvent()
 16        self.collHandEvent.addInPattern('into-%in')
 17        self.collHandEvent.addOutPattern('outof-%in')
 18
 19        # Make a variable to store the unique collision string count.
 20        self.collCount = 0
 21
 22        # Load a model. Reparent it to the camera so we can move it.
 23        s = base.loader.loadModel('smiley')
 24        s.reparentTo(base.camera)
 25        s.setPos(0, 25, 0)
 26
 27        # Setup a collision solid for this model.
 28        sColl = self.initCollisionSphere(s, True)
 29
 30        # Add this object to the traverser.
 31        base.cTrav.addCollider(sColl[0], self.collHandEvent)
 32
 33        # Accept the events sent by the collisions.
 34        self.accept('into-' + sColl[1], self.collide3)
 35        self.accept('outof-' + sColl[1], self.collide4)
 36        print(sColl[1])
 37
 38        # Load another model.
 39        t = base.loader.loadModel('smiley')
 40        t.reparentTo(base.render)
 41        t.setPos(5, 25, 0)
 42
 43        # Setup a collision solid for this model.
 44        tColl = self.initCollisionSphere(t, True)
 45
 46        # Add this object to the traverser.
 47        base.cTrav.addCollider(tColl[0], self.collHandEvent)
 48
 49        # Accept the events sent by the collisions.
 50        self.accept('into-' + tColl[1], self.collide)
 51        self.accept('outof-' + tColl[1], self.collide2)
 52        print(tColl[1])
 53
 54        print("WERT")
 55
 56    def collide(self, collEntry):
 57        print("WERT: object has collided into another object")
 58        collParent = collEntry.getFromNodePath().getParent()
 59        Sequence(
 60            Func(collParent.setColor, (1, 0, 0, 1)),
 61            Wait(0.2),
 62            Func(collParent.setColor, (0, 1, 0, 1)),
 63            Wait(0.2),
 64            Func(collParent.setColor, (1, 1, 1, 1)),
 65        ).start()
 66
 67    def collide2(self, collEntry):
 68        print("WERT.: object is no longer colliding with another object")
 69
 70    def collide3(self, collEntry):
 71        print("WERT2: object has collided into another object")
 72
 73    def collide4(self, collEntry):
 74        print("WERT2: object is no longer colliding with another object")
 75
 76    def initCollisionSphere(self, obj, show=False):
 77        # Get the size of the object for the collision sphere.
 78        bounds = obj.getChild(0).getBounds()
 79        center = bounds.getCenter()
 80        radius = bounds.getRadius() * 1.1
 81
 82        # Create a collision sphere and name it something understandable.
 83        collSphereStr = 'CollisionHull{0}_{1}'.format(self.collCount, obj.name)
 84        self.collCount += 1
 85        cNode = CollisionNode(collSphereStr)
 86        cNode.addSolid(CollisionSphere(center, radius))
 87
 88        cNodepath = obj.attachNewNode(cNode)
 89        if show:
 90            cNodepath.show()
 91
 92        # Return a tuple with the collision node and its corresponding string so
 93        # that the bitmask can be set.
 94        return (cNodepath, collSphereStr)
 95
 96
 97base = ShowBase()
 98# Run the world. Move around with the mouse to create collisions.
w = World()
base.run()