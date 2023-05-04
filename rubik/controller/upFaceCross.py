from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveUpCross(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    while not upCrossSolved(encodedCube):
        if isWorstCase(encodedCube):
            pass
        elif isMediumCase(encodedCube):
            while encodedCube[UMM] != encodedCube[UTM]:
                theCube.rotate('U')
                solution += 'U'
                encodedCube = theCube.get()
        elif isBestCase(encodedCube):
            while encodedCube[UMM] != encodedCube[UTM] or encodedCube[UMM] != encodedCube[UML]:
                theCube.rotate('U')
                solution += 'U'
                encodedCube = theCube.get()
                
        theCube.rotate('FURurf')
        solution += 'FURurf'
        encodedCube = theCube.get()
        
    return solution
    
def upCrossSolved(encodedCube) -> bool:
    if encodedCube[UMM] != encodedCube[UTM]:
        return False      
    if encodedCube[UMM] != encodedCube[UML]:
        return False      
    if encodedCube[UMM] != encodedCube[UMR]:
        return False      
    if encodedCube[UMM] != encodedCube[UBM]:
        return False      

    return True

def isWorstCase(encodedCube) -> bool:
    if encodedCube[UMM] == encodedCube[UTM]:
        return False      
    if encodedCube[UMM] == encodedCube[UML]:
        return False      
    if encodedCube[UMM] == encodedCube[UMR]:
        return False      
    if encodedCube[UMM] == encodedCube[UBM]:
        return False      

    return True

def isMediumCase(encodedCube) -> bool:
    if encodedCube[UMM] == encodedCube[UTM] == encodedCube[UBM]:
        return True 
    if encodedCube[UMM] == encodedCube[UML] == encodedCube[UMR]:
        return True 
    
    return False

def isBestCase(encodedCube) -> bool:
    if encodedCube[UMM] == encodedCube[UTM] == encodedCube[UMR]:
        return True 
    if encodedCube[UMM] == encodedCube[UMR] == encodedCube[UBM]:
        return True 
    if encodedCube[UMM] == encodedCube[UBM] == encodedCube[UML]:
        return True 
    if encodedCube[UMM] == encodedCube[UML] == encodedCube[UTM]:
        return True 
    
    return False