from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    daisySolution = createDaisy(theCube)
    bottomCrossSolution = createBottomCross(theCube)
    
    return daisySolution + bottomCrossSolution
    
def isDaisy(theCube: Cube):
    encodedCube = theCube.get()
    bottomCrossColor = encodedCube[DMM]
    return encodedCube[UTM] == bottomCrossColor and encodedCube[UML] == bottomCrossColor and encodedCube[UMR] == bottomCrossColor and encodedCube[UBM] == bottomCrossColor

def create_middles(theCube: Cube, bottomCrossColor, solution):
    encodedCube = theCube.get()
    
    if encodedCube[FTM] == bottomCrossColor or encodedCube[FBM] == bottomCrossColor:
        theCube._rotateFrontClockwise()
        solution += 'F'
        encodedCube = theCube.get()
        
    if encodedCube[BTM] == bottomCrossColor or encodedCube[BBM] == bottomCrossColor:
        theCube._rotateBackClockwise()
        solution += 'B'
        encodedCube = theCube.get()

    if encodedCube[LTM] == bottomCrossColor or encodedCube[LBM] == bottomCrossColor:
        theCube._rotateLeftClockwise()
        solution += 'L'
        encodedCube = theCube.get()

    if encodedCube[RTM] == bottomCrossColor or encodedCube[RBM] == bottomCrossColor:
        theCube._rotateRightClockwise()
        solution += 'R'
        encodedCube = theCube.get()
        
    return solution

def check_middles(theCube, bottomCrossColor, solution):
    encodedCube = theCube.get()
    
    if encodedCube[UTM] != bottomCrossColor:
        if encodedCube[RMR] == bottomCrossColor or encodedCube[DBM] == bottomCrossColor or encodedCube[LML] == bottomCrossColor:
            while encodedCube[UTM] != bottomCrossColor:
                theCube._rotateBackClockwise()
                solution += 'B'
                encodedCube = theCube.get()
    
    if encodedCube[UMR] != bottomCrossColor:
        if encodedCube[BML] == bottomCrossColor or encodedCube[DMR] == bottomCrossColor or encodedCube[FMR] == bottomCrossColor:
            while encodedCube[UMR] != bottomCrossColor:
                theCube._rotateRightClockwise()
                solution += 'R'
                encodedCube = theCube.get()
        
    if encodedCube[UBM] != bottomCrossColor:
        if encodedCube[RML] == bottomCrossColor or encodedCube[DTM] == bottomCrossColor or encodedCube[LMR] == bottomCrossColor:
            while encodedCube[UBM] != bottomCrossColor:
                theCube._rotateFrontClockwise()
                solution += 'F'
                encodedCube = theCube.get()
                
    if encodedCube[UML] != bottomCrossColor:
        if encodedCube[BMR] == bottomCrossColor or encodedCube[DML] == bottomCrossColor or encodedCube[FML] == bottomCrossColor:
            while encodedCube[UML] != bottomCrossColor:
                theCube._rotateLeftClockwise()
                solution += 'L'
                encodedCube = theCube.get()
    
    theCube._rotateUpClockwise()
    solution += 'U'
    
    return solution
    


def createDaisy(theCube: Cube):
    encodedCube = theCube.get()
    bottomCrossColor = encodedCube[DMM]
    solution = ''
    
    while not isDaisy(theCube):
        solution = create_middles(theCube, bottomCrossColor, solution)
        solution = check_middles(theCube, bottomCrossColor, solution)
        
    return solution

def createBottomCross(theCube: Cube):
    encodedCube = theCube.get()    
    solution = ''
    
    while encodedCube[FTM] != encodedCube[FMM] or encodedCube[UBM] != encodedCube[DMM]:
        theCube._rotateUpClockwise()
        solution += 'U'
        encodedCube = theCube.get()
    theCube._rotateFrontClockwise()
    theCube._rotateFrontClockwise()
    solution += 'FF'
    encodedCube = theCube.get()    
    
    
    while encodedCube[RTM] != encodedCube[RMM] or encodedCube[UMR] != encodedCube[DMM]:
        theCube._rotateUpClockwise()
        solution += 'U'
        encodedCube = theCube.get()
    theCube._rotateRightClockwise()
    theCube._rotateRightClockwise()
    solution += 'RR'
    encodedCube = theCube.get()    


    while encodedCube[BTM] != encodedCube[BMM] or encodedCube[UTM] != encodedCube[DMM]:
        theCube._rotateUpClockwise()
        solution += 'U'
        encodedCube = theCube.get()
    theCube._rotateBackClockwise()
    theCube._rotateBackClockwise()
    solution += 'BB'
    encodedCube = theCube.get()    

    
    while encodedCube[LTM] != encodedCube[LMM] or encodedCube[UML] != encodedCube[DMM]:
        theCube._rotateUpClockwise()
        solution += 'U'
        encodedCube = theCube.get()
    theCube._rotateLeftClockwise()
    theCube._rotateLeftClockwise()
    solution += 'LL'
    encodedCube = theCube.get()    

    return solution