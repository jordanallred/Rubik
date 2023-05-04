from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveUpCross(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    while not middleSolved(encodedCube):
        if isFish(encodedCube):
            while encodedCube[UBL] != encodedCube[UMM]:
                theCube.rotate('U')
                solution += 'U'
                encodedCube = theCube.get()

        theCube.rotate('FURurf')
        solution += 'FURurf'
        encodedCube = theCube.get()
        
    return solution
    
def middleSolved(encodedCube) -> bool:
    if encodedCube[UMM] != encodedCube[UTM]:
        return False      
    if encodedCube[UMM] != encodedCube[UML]:
        return False      
    if encodedCube[UMM] != encodedCube[UMR]:
        return False      
    if encodedCube[UMM] != encodedCube[UBM]:
        return False      

    return True

def isFish(encodedCube) -> bool:
    if encodedCube[UTL] == encodedCube[UMM]:
        return True
    if encodedCube[UTR] == encodedCube[UMM]:
        return True    
    if encodedCube[UBL] == encodedCube[UMM]:
        return True
    if encodedCube[UBR] == encodedCube[UMM]:
        return True
    
    return False