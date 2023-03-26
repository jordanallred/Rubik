from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveBottomLayer(theCube: Cube) -> str:
    global solution
    cubeCopy = theCube
    encodedCube = cubeCopy.get()
    
    while not bottomSolved(cubeCopy):
        encodedCube = move_color_happy(encodedCube, cubeCopy, FTL, LTR, cubeCopy.right_trigger)
        encodedCube = move_color_happy(encodedCube, cubeCopy, FTR, RTL, cubeCopy.left_trigger)
        
        encodedCube = move_color_happy(encodedCube, cubeCopy, RTL, FTR, cubeCopy.right_trigger)
        encodedCube = move_color_happy(encodedCube, cubeCopy, RTR, BTL, cubeCopy.left_trigger)
    
        encodedCube = move_color_happy(encodedCube, cubeCopy, BTL, RTR, cubeCopy.right_trigger)
        encodedCube = move_color_happy(encodedCube, cubeCopy, BTR, LTL, cubeCopy.left_trigger)
    
        encodedCube = move_color_happy(encodedCube, cubeCopy, LTL, BTR, cubeCopy.right_trigger)
        encodedCube = move_color_happy(encodedCube, cubeCopy, LTR, FTL, cubeCopy.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, cubeCopy, FRONT, FBL, cubeCopy.left_trigger, UBR, cubeCopy.right_trigger)
        encodedCube = move_color_sad(encodedCube, cubeCopy, FRONT, FBR, cubeCopy.right_trigger, UBL, cubeCopy.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, cubeCopy, RIGHT, RBL, cubeCopy.left_trigger, UTR, cubeCopy.right_trigger)
        encodedCube = move_color_sad(encodedCube, cubeCopy, RIGHT, RBR, cubeCopy.right_trigger, UBR, cubeCopy.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, cubeCopy, BACK, BBL, cubeCopy.left_trigger, UTL, cubeCopy.right_trigger)
        encodedCube = move_color_sad(encodedCube, cubeCopy, BACK, BBR, cubeCopy.right_trigger, UTR, cubeCopy.left_trigger)
    
        encodedCube = move_color_sad(encodedCube, cubeCopy, LEFT, LBL, cubeCopy.left_trigger, UBL, cubeCopy.right_trigger)
        encodedCube = move_color_sad(encodedCube, cubeCopy, LEFT, LBR, cubeCopy.right_trigger, UTL, cubeCopy.left_trigger)
         
    return solution
    
def bottomSolved(theCube: Cube) -> bool:
    encodedCube = theCube.get()
    
    theCube.visualize()
    
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

def move_color_happy(encodedCube, cubeCopy, target_color, face_color, trigger):
    global solution    
    if encodedCube[target_color] == encodedCube[DMM]:
        while encodedCube[face_color] != encodedCube[face_color + (4 - face_color % (NUM_ELEMENTS // NUM_FACES))]:
            cubeCopy.rotate('u')
            encodedCube = cubeCopy.get()
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
            
    return cubeCopy.get()

def move_color_sad(encodedCube, cubeCopy, face, moveUp, trigger1, doubleTrigger, trigger2):
    global solution    
    if encodedCube[moveUp] == encodedCube[DMM]:
        solution += trigger1(face)
        encodedCube = cubeCopy.get()
        
    if encodedCube[doubleTrigger] == encodedCube[DMM]:
        solution += trigger2(face)
        solution += trigger2(face)
    return cubeCopy.get()

    