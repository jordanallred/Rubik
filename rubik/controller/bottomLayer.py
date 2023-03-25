from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    cubeCopy = theCube
    encodedCube = cubeCopy.get()
    
    encodedCube = move_color_happy(encodedCube, cubeCopy, FTL, LTR, LMM, LEFT, Cube.right_trigger)
    encodedCube = move_color_happy(encodedCube, cubeCopy, FTR, RTL, RMM, RIGHT, Cube.left_trigger)
    
    encodedCube = move_color_happy(encodedCube, cubeCopy, RTL, FTR, FMM, FRONT, Cube.right_trigger)
    encodedCube = move_color_happy(encodedCube, cubeCopy, RTR, BTL, BMM, BACK, Cube.left_trigger)

    encodedCube = move_color_happy(encodedCube, cubeCopy, BTL, RTR, RMM, RIGHT, Cube.right_trigger)
    encodedCube = move_color_happy(encodedCube, cubeCopy, BTR, LTL, LMM, LEFT, Cube.left_trigger)

    encodedCube = move_color_happy(encodedCube, cubeCopy, LTL, BTR, BMM, BACK, Cube.right_trigger)
    encodedCube = move_color_happy(encodedCube, cubeCopy, LTR, FTL, FMM, FRONT, Cube.left_trigger)

    encodedCube = move_color_sad(encodedCube, cubeCopy, FRONT, FBL, Cube.left_trigger, UBR, Cube.right_trigger)
    encodedCube = move_color_sad(encodedCube, cubeCopy, FRONT, FBR, Cube.right_trigger, UBL, Cube.left_trigger)

    encodedCube = move_color_sad(encodedCube, cubeCopy, RIGHT, RBL, Cube.left_trigger, UTR, Cube.right_trigger)
    encodedCube = move_color_sad(encodedCube, cubeCopy, RIGHT, RBR, Cube.right_trigger, UBR, Cube.left_trigger)

    encodedCube = move_color_sad(encodedCube, cubeCopy, BACK, BBL, Cube.left_trigger, UTL, Cube.right_trigger)
    encodedCube = move_color_sad(encodedCube, cubeCopy, BACK, BBR, Cube.right_trigger, UTR, Cube.left_trigger)

    encodedCube = move_color_sad(encodedCube, cubeCopy, LEFT, LBL, Cube.left_trigger, UBL, Cube.right_trigger)
    encodedCube = move_color_sad(encodedCube, cubeCopy, LEFT, LBR, Cube.right_trigger, UTL, Cube.left_trigger)

    return cubeCopy.get()
    
def bottomSolved(theCube: Cube) -> bool:
    encodedCube = theCube.get()
    
    if encodedCube[BTL] !=  encodedCube[BMM]:
        return False
    if encodedCube[BTM] !=  encodedCube[BMM]:
        return False
    if encodedCube[BTR] !=  encodedCube[BMM]:
        return False
    
    if encodedCube[BML] !=  encodedCube[BMM]:
        return False
    if encodedCube[BMR] !=  encodedCube[BMM]:
        return False
    
    if encodedCube[BBL] !=  encodedCube[BMM]:
        return False
    if encodedCube[BBM] !=  encodedCube[BMM]:
        return False
    if encodedCube[BBR] !=  encodedCube[BMM]:
        return False
    
    return True

def move_color_happy(encodedCube, cubeCopy, target_color, face_color, middle_color, face, trigger):
    if encodedCube[target_color] == encodedCube[BMM]:
        if encodedCube[face_color] == encodedCube[middle_color]:
            cubeCopy.trigger(face)
        else:
            cubeCopy.rotate('U')
            
    return cubeCopy.get()

def move_color_sad(encodedCube, cubeCopy, face, moveUp, trigger1, doubleTrigger, trigger2):
    if encodedCube[moveUp] == encodedCube[BMM]:
        cubeCopy.trigger1(face)
        encodedCube = cubeCopy.get()
    
    if encodedCube[doubleTrigger] == encodedCube[BMM]:
        cubeCopy.trigger2(face)
        cubeCopy.trigger1(face)
        
    return cubeCopy.get()

    