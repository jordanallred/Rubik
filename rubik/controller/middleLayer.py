from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

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
        
        if stuck:
            theCube.right_trigger(FRONT)
            counter += 1
        else:
            counter = 0
            
        if counter == 4:
            solution += theCube.right_trigger(FRONT)
            theCube.rotate('u')
            solution += 'u'
            theCube.left_trigger(RIGHT)

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
            solution += theCube.right_trigger(side)
            theCube.rotate('u')
            solution += 'u'
            theCube.left_trigger(side.right)
            encodedCube = theCube.get()
            return True
        if encodedCube[topBottomMiddle] == encodedCube[(frontTopMiddle + 3 + (NUM_ELEMENTS // NUM_FACES)) % (4 * (NUM_ELEMENTS // NUM_FACES))]:
            theCube.rotate('u')
            solution += 'u'
            solution += theCube.left_trigger(side)
            theCube.rotate('U')
            solution += 'U'
            theCube.right_trigger(side.left)
            encodedCube = theCube.get()
            return True
        return False