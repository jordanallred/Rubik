from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def rightTriggerFix(theCube: Cube, face: Face):
    global solution
    solution += theCube.right_trigger(face)
    theCube.rotate('u')
    solution += 'u'
    theCube.left_trigger(face.right)    

def leftTriggerFix(theCube: Cube, face: Face):
    global solution
    solution += theCube.left_trigger(face)
    theCube.rotate('U')
    solution += 'U'
    theCube.right_trigger(face.left)

def solveMiddleLayer(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    counter = 0
    while not middleSolved(encodedCube):
        stuck = False
        stuck = stuck or moveColors(theCube, FTM, UBM, FRONT)
        stuck = stuck or moveColors(theCube, RTM, UMR, RIGHT)
        stuck = stuck or moveColors(theCube, BTM, UTM, BACK)
        stuck = stuck or moveColors(theCube, LTM, UML, LEFT)
        
        if not stuck:
            theCube.rotate('u')
            solution += 'u'
            counter += 1
        else:
            counter = 0
        if counter == 4:
            resetMiddle(theCube)
        
        encodedCube = theCube.get()
        
    return solution
    
def middleSolved(encodedCube) -> bool:    
    if encodedCube[FML] !=  encodedCube[FMM]:
        return False
    if encodedCube[FMR] !=  encodedCube[FMM]:
        return False
    
    if encodedCube[RML] !=  encodedCube[RMM]:
        return False
    if encodedCube[RMR] !=  encodedCube[RMM]:
        return False
    
    if encodedCube[BML] !=  encodedCube[BMM]:
        return False
    if encodedCube[BMR] !=  encodedCube[BMM]:
        return False
        
    if encodedCube[LML] !=  encodedCube[LMM]:
        return False
    if encodedCube[LMR] !=  encodedCube[LMM]:
        return False
    
    return True

def moveColors(theCube: Cube, frontTopMiddle: int, topBottomMiddle: int, side: Face):
    global solution
    encodedCube = theCube.get()
    
    if encodedCube[frontTopMiddle] == encodedCube[frontTopMiddle + 3]:
        if encodedCube[topBottomMiddle] == encodedCube[(frontTopMiddle + 3 + (NUM_ELEMENTS // NUM_FACES)) % (4 * (NUM_ELEMENTS // NUM_FACES))]:
            theCube.rotate('U')
            solution += 'U'
            rightTriggerFix(theCube, side)
            return True
        if encodedCube[topBottomMiddle] == encodedCube[(frontTopMiddle + 3 - (NUM_ELEMENTS // NUM_FACES)) % (4 * (NUM_ELEMENTS // NUM_FACES))]:
            theCube.rotate('u')
            solution += 'u'
            leftTriggerFix(theCube, side)
            return True
    
    return False

def resetMiddle(theCube: Cube):
    global solution
    encodedCube = theCube.get()
    
    if encodedCube[FML] != encodedCube[FMM]:
        leftTriggerFix(theCube, FRONT)
    elif encodedCube[FMR] != encodedCube[FMM]:
        rightTriggerFix(theCube, FRONT)
        
    elif encodedCube[RML] != encodedCube[RMM]:
        leftTriggerFix(theCube, RIGHT)
    elif encodedCube[RMR] != encodedCube[RMM]:
        rightTriggerFix(theCube, RIGHT)
        
    elif encodedCube[BML] != encodedCube[BMM]:
        leftTriggerFix(theCube, BACK)
    elif encodedCube[BMR] != encodedCube[BMM]:
        rightTriggerFix(theCube, BACK)
        
    elif encodedCube[LML] != encodedCube[LMM]:
        leftTriggerFix(theCube, LEFT)
    elif encodedCube[LMR] != encodedCube[LMM]:
        rightTriggerFix(theCube, LEFT)
    
