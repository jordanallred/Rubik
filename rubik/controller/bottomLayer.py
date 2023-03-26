from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveBottomLayer(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    while not bottomSolved(theCube):
        encodedCube = move_color_happy(encodedCube, theCube, FTL, LTR, theCube.right_trigger)
        encodedCube = move_color_happy(encodedCube, theCube, FTR, RTL, theCube.left_trigger)
        
        encodedCube = move_color_happy(encodedCube, theCube, RTL, FTR, theCube.right_trigger)
        encodedCube = move_color_happy(encodedCube, theCube, RTR, BTL, theCube.left_trigger)
    
        encodedCube = move_color_happy(encodedCube, theCube, BTL, RTR, theCube.right_trigger)
        encodedCube = move_color_happy(encodedCube, theCube, BTR, LTL, theCube.left_trigger)
    
        encodedCube = move_color_happy(encodedCube, theCube, LTL, BTR, theCube.right_trigger)
        encodedCube = move_color_happy(encodedCube, theCube, LTR, FTL, theCube.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, theCube, FRONT, FBL, theCube.left_trigger, UBR, theCube.right_trigger)
        encodedCube = move_color_sad(encodedCube, theCube, FRONT, FBR, theCube.right_trigger, UBL, theCube.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, theCube, RIGHT, RBL, theCube.left_trigger, UTR, theCube.right_trigger)
        encodedCube = move_color_sad(encodedCube, theCube, RIGHT, RBR, theCube.right_trigger, UBR, theCube.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, theCube, BACK, BBL, theCube.left_trigger, UTL, theCube.right_trigger)
        encodedCube = move_color_sad(encodedCube, theCube, BACK, BBR, theCube.right_trigger, UTR, theCube.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, theCube, LEFT, LBL, theCube.left_trigger, UBL, theCube.right_trigger)
        encodedCube = move_color_sad(encodedCube, theCube, LEFT, LBR, theCube.right_trigger, UTL, theCube.left_trigger)
         
    return solution
    
def bottomSolved(theCube: Cube) -> bool:
    encodedCube = theCube.get()
        
    if encodedCube[DTL] !=  encodedCube[DMM]:
        return False
    if encodedCube[DTM] !=  encodedCube[DMM]:
        return False
    if encodedCube[DTR] !=  encodedCube[DMM]:
        return False
    
    if encodedCube[DML] !=  encodedCube[DMM]:
        return False
    if encodedCube[DMR] !=  encodedCube[DMM]:
        return False
    
    if encodedCube[DBL] !=  encodedCube[DMM]:
        return False
    if encodedCube[DBM] !=  encodedCube[DMM]:
        return False
    if encodedCube[DBR] !=  encodedCube[DMM]:
        return False
        
    return True

def move_color_happy(encodedCube, theCube, target_color, face_color, trigger):
    global solution    
    if encodedCube[target_color] == encodedCube[DMM]:
        while encodedCube[face_color] != encodedCube[face_color + (4 - face_color % (NUM_ELEMENTS // NUM_FACES))]:
            theCube.rotate('u')
            encodedCube = theCube.get()
            solution += 'u'
            face_color = (face_color + (NUM_ELEMENTS // NUM_FACES)) % ((NUM_ELEMENTS // NUM_FACES) * 4)
            
        if FTL == face_color or FTR == face_color:
            face = FRONT
        elif RTL == face_color or RTR == face_color:
            face = RIGHT
        elif BTL == face_color or BTR == face_color:
            face = BACK
        elif LTL == face_color or LTR == face_color:
            face = LEFT
            
        solution += trigger(face)
            
    return theCube.get()

def move_color_sad(encodedCube, theCube, face, moveUp, trigger1, doubleTrigger, trigger2):
    global solution    
    if encodedCube[moveUp] == encodedCube[DMM]:
        solution += trigger1(face)
        encodedCube = theCube.get()
        
    if encodedCube[doubleTrigger] == encodedCube[DMM]:
        solution += trigger2(face)
        solution += trigger2(face)
    return theCube.get()

    