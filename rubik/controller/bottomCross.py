from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    cubeCopy = Cube(theCube.get())
    daisySolution = createDaisy(theCube)
    cubeCopy.rotate(daisySolution)
    bottomCrossSolution = createBottomCross(cubeCopy)
    
    return daisySolution + bottomCrossSolution
    
def isDaisy(theCube: Cube):
    encodedCube = theCube.get()
    bottomCrossColor = encodedCube[DMM]
    return encodedCube[UTM] == bottomCrossColor and encodedCube[UML] == bottomCrossColor and encodedCube[UMR] == bottomCrossColor and encodedCube[UBM] == bottomCrossColor

def create_middles(cubeCopy: Cube, bottomCrossColor, solution):
    if cubeCopy.cube[FTM] == bottomCrossColor or cubeCopy.cube[FBM] == bottomCrossColor:
        cubeCopy._rotateFrontClockwise()
        solution += 'F'
        
    if cubeCopy.cube[BTM] == bottomCrossColor or cubeCopy.cube[BBM] == bottomCrossColor:
        cubeCopy._rotateBackClockwise()
        solution += 'B'

    if cubeCopy.cube[LTM] == bottomCrossColor or cubeCopy.cube[LBM] == bottomCrossColor:
        cubeCopy._rotateLeftClockwise()
        solution += 'L'

    if cubeCopy.cube[RTM] == bottomCrossColor or cubeCopy.cube[RBM] == bottomCrossColor:
        cubeCopy._rotateRightClockwise()
        solution += 'R'
        
    return solution

def check_middles(cubeCopy, bottomCrossColor, solution):
    if cubeCopy.cube[UTM] != bottomCrossColor:
        if cubeCopy.cube[RMR] == bottomCrossColor or cubeCopy.cube[DBM] == bottomCrossColor or cubeCopy.cube[LML] == bottomCrossColor:
            while cubeCopy.cube[UTM] != bottomCrossColor:
                cubeCopy._rotateBackClockwise()
                solution += 'B'
    
    if cubeCopy.cube[UMR] != bottomCrossColor:
        if cubeCopy.cube[BML] == bottomCrossColor or cubeCopy.cube[DMR] == bottomCrossColor or cubeCopy.cube[FMR] == bottomCrossColor:
            while cubeCopy.cube[UMR] != bottomCrossColor:
                cubeCopy._rotateRightClockwise()
                solution += 'R'
        
    if cubeCopy.cube[UBM] != bottomCrossColor:
        if cubeCopy.cube[RML] == bottomCrossColor or cubeCopy.cube[DTM] == bottomCrossColor or cubeCopy.cube[LMR] == bottomCrossColor:
            while cubeCopy.cube[UBM] != bottomCrossColor:
                cubeCopy._rotateFrontClockwise()
                solution += 'F'
                
    if cubeCopy.cube[UML] != bottomCrossColor:
        if cubeCopy.cube[BMR] == bottomCrossColor or cubeCopy.cube[DML] == bottomCrossColor or cubeCopy.cube[FML] == bottomCrossColor:
            while cubeCopy.cube[UML] != bottomCrossColor:
                cubeCopy._rotateLeftClockwise()
                solution += 'L'
    
    cubeCopy._rotateUpClockwise()
    solution += 'U'
    
    return solution
    


def createDaisy(theCube: Cube):
    cubeCopy = Cube(theCube.cube)
    bottomCrossColor = cubeCopy.cube[DMM]
    solution = ''
    
    while not isDaisy(cubeCopy):
        solution = create_middles(cubeCopy, bottomCrossColor, solution)
        solution = check_middles(cubeCopy, bottomCrossColor, solution)
    return solution

def createBottomCross(theCube: Cube):
    cubeCopy = Cube(theCube.cube)
    solution = ''
    
    while cubeCopy.cube[FTM] != cubeCopy.cube[FMM] or cubeCopy.cube[UBM] != cubeCopy.cube[DMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateFrontClockwise()
    cubeCopy._rotateFrontClockwise()
    solution += 'FF'
    
    
    while cubeCopy.cube[RTM] != cubeCopy.cube[RMM] or cubeCopy.cube[UMR] != cubeCopy.cube[DMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateRightClockwise()
    cubeCopy._rotateRightClockwise()
    solution += 'RR'


    while cubeCopy.cube[BTM] != cubeCopy.cube[BMM] or cubeCopy.cube[UTM] != cubeCopy.cube[DMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateBackClockwise()
    cubeCopy._rotateBackClockwise()
    solution += 'BB'

    
    while cubeCopy.cube[LTM] != cubeCopy.cube[LMM] or cubeCopy.cube[UML] != cubeCopy.cube[DMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateLeftClockwise()
    cubeCopy._rotateLeftClockwise()
    solution += 'LL'

    return solution