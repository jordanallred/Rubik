from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveUpperLayer(theCube: Cube) -> str:
    global solution
    
    encodedCube = theCube.get()
    solveCorners(theCube)
    solveLayer(theCube)

def solveCorners(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    while not solvedCorners(encodedCube):
        corners = None
        face = FRONT
        if encodedCube[FTL] == encodedCube[FTR]:
            corners = FTL
            face = FRONT        
        elif encodedCube[RTL] == encodedCube[RTR]:
            corners = RTL
            face = RIGHT
        elif encodedCube[BTL] == encodedCube[BTR]:
            corners = BTL
            face = BACK
        elif encodedCube[LTL] == encodedCube[LTR]:
            corners = LTL
            face = LEFT
        
        if corners is not None:
            while encodedCube[corners] != encodedCube[corners + 4]:
                theCube.rotate('u')
                solution += 'u'
                corners = corners + (NUM_ELEMENTS // NUM_FACES) % ((NUM_ELEMENTS // NUM_FACES) * 4)
                face = face.right
                encodedCube = theCube.get()
        
        face = face.right
        faceRight = face.right.letter
        faceLeft = face.left.letter
        
        rotation = faceLeft.lower() + 'U' + faceRight.upper() + 'u' + faceLeft.upper() + 'U' + faceRight.lower() + \
                   faceRight.upper() + 'U' + faceRight.lower() + 'U' + faceRight.upper() + 'uu' + faceRight.lower()
            
        theCube.rotate(rotation)
        solution += rotation
        encodedCube = theCube.get()
        
    while encodedCube[FTL] != encodedCube[FMM]:
        theCube.rotate('u')
        solution += 'u'
        encodedCube = theCube.get()
        
def solveLayer(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()

    while not cubeSolved(encodedCube):
        solvedFace = FRONT
        
        if faceSolved(encodedCube, FTL):
            solvedFace = FRONT
        elif faceSolved(encodedCube, RTL):
            solvedFace = RIGHT
        elif faceSolved(encodedCube, BTL):
            solvedFace = BACK
        elif faceSolved(encodedCube, LTL):
            solvedFace = LEFT
            
        frontFace = solvedFace.right.right
        frontLetter = frontFace.letter
        frontLeft = frontFace.left.letter
        frontRight = frontFace.right.letter
        rotation = frontLetter.upper() + frontLetter.upper() + 'U' + frontRight.lower() + frontLeft.upper() + \
                   frontLetter.upper() + frontLetter.upper() + frontLeft.lower() + frontRight.upper() + 'U' + \
                   frontLetter.upper() + frontLetter.upper()
        theCube.rotate(rotation)
        solution += rotation
        encodedCube = theCube.get()
    
def solvedCorners(encodedCube) -> bool:
    if encodedCube[FTL] != encodedCube[FTR]:
        return False
    if encodedCube[RTL] != encodedCube[RTR]:
        return False
    if encodedCube[BTL] != encodedCube[BTR]:
        return False
    if encodedCube[LTL] != encodedCube[LTR]:
        return False
    return True

def faceSolved(encodedCube, topLeft) -> bool:
    middle = topLeft + 4
    for index in range(topLeft, topLeft + 9):
        if encodedCube[index] != encodedCube[middle]:
            return False 
    return True

def cubeSolved(encodedCube) -> bool:
    if not faceSolved(encodedCube, FTL):
        return False
    if not faceSolved(encodedCube, RTL):
        return False
    if not faceSolved(encodedCube, BTL):
        return False
    if not faceSolved(encodedCube, LTL):
        return False
    if not faceSolved(encodedCube, UTL):
        return False
    if not faceSolved(encodedCube, DTL):
        return False
    
    return True
