from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    theCube.visualize()
    print('\n')    
    
    cubeCopy = theCube
    encodedCube = cubeCopy.get()
    solution = ''
    
    while not bottomSolved(cubeCopy):
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, FTL, LTR, theCube.right_trigger, solution)
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, FTR, RTL, theCube.left_trigger, solution)
        
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, RTL, FTR, theCube.right_trigger, solution)
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, RTR, BTL, theCube.left_trigger, solution)
    
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, BTL, RTR, theCube.right_trigger, solution)
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, BTR, LTL, theCube.left_trigger, solution)
    
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, LTL, BTR, theCube.right_trigger, solution)
        encodedCube, solution = move_color_happy(encodedCube, cubeCopy, LTR, FTL, theCube.left_trigger, solution)
    
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, FRONT, FBL, theCube.left_trigger, UBR, theCube.right_trigger, solution)
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, FRONT, FBR, theCube.right_trigger, UBL, theCube.left_trigger, solution)
    
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, RIGHT, RBL, theCube.left_trigger, UTR, theCube.right_trigger, solution)
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, RIGHT, RBR, theCube.right_trigger, UBR, theCube.left_trigger, solution)
    
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, BACK, BBL, theCube.left_trigger, UTL, theCube.right_trigger, solution)
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, BACK, BBR, theCube.right_trigger, UTR, theCube.left_trigger, solution)
    
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, LEFT, LBL, theCube.left_trigger, UBL, theCube.right_trigger, solution)
        encodedCube, solution = move_color_sad(encodedCube, cubeCopy, LEFT, LBR, theCube.right_trigger, UTL, theCube.left_trigger, solution)
        
    return solution
    
def bottomSolved(theCube: Cube) -> bool:
    encodedCube = theCube.get()

    theCube.visualize()
    print('\n')
    
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

def move_color_happy(encodedCube, cubeCopy, target_color, face_color, trigger, solution):
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
        else:
            cubeCopy.visualize()
            print('\n')
            print(face_color)
            
        solution += trigger(face)
            
    return cubeCopy.get(), solution

def move_color_sad(encodedCube, cubeCopy, face, moveUp, trigger1, doubleTrigger, trigger2, solution):
    if encodedCube[moveUp] == encodedCube[DMM]:
        solution += trigger1(face)
        encodedCube = cubeCopy.get()
        
    
    if encodedCube[doubleTrigger] == encodedCube[DMM]:
        solution += trigger2(face)
        solution += trigger2(face)
    return cubeCopy.get(), solution

    