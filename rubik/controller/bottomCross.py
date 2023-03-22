from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    cubeCopy = Cube(theCube.cube)
    daisySolution = createDaisy(theCube)
    cubeCopy.rotate(daisySolution)
    bottomCrossSolution = createBottomCross(cubeCopy)
    
    return daisySolution + bottomCrossSolution
    
def isDaisy(theCube: Cube):
    bottomCrossColor = theCube.cube[DMM]
    return theCube.cube[UTM] == bottomCrossColor and theCube.cube[UML] == bottomCrossColor and theCube.cube[UMR] == bottomCrossColor and theCube.cube[UBM] == bottomCrossColor

def createDaisy(theCube: Cube):
    cubeCopy = Cube(theCube.cube)
    bottomCrossColor = cubeCopy.cube[DMM]
    solution = ''
    
    while not isDaisy(cubeCopy):
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

def createBottomCross(theCube: Cube):
    cubeCopy = Cube(theCube.cube)
    solution = ''
    
    while cubeCopy.cube[FTM] != cubeCopy.cube[FMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateFrontClockwise()
    cubeCopy._rotateFrontClockwise()
    solution += 'FF'
    
    while cubeCopy.cube[RTM] != cubeCopy.cube[RMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateRightClockwise()
    cubeCopy._rotateRightClockwise()
    solution += 'RR'

    while cubeCopy.cube[BTM] != cubeCopy.cube[BMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateBackClockwise()
    cubeCopy._rotateBackClockwise()
    solution += 'BB'
    
    while cubeCopy.cube[LTM] != cubeCopy.cube[LMM]:
        cubeCopy._rotateUpClockwise()
        solution += 'U'
    cubeCopy._rotateLeftClockwise()
    cubeCopy._rotateLeftClockwise()
    solution += 'LL'

    return solution