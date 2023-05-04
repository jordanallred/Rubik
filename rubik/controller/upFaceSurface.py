from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveUpSurface(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    while not upSurfaceSolved(encodedCube):
        if isFish(encodedCube):
            while encodedCube[UBL] != encodedCube[UMM]:
                theCube.rotate('U')
                solution += 'U'
                encodedCube = theCube.get()
        else:
            while encodedCube[LTR] != encodedCube[UMM]:
                theCube.rotate('U')
                solution += 'U'
                encodedCube = theCube.get()
                
        theCube.rotate('RUrURuur')
        solution += 'RUrURuur'
        encodedCube = theCube.get()
        theCube.visualize()
        pass
    return solution
    
def upSurfaceSolved(encodedCube) -> bool:
    if encodedCube[UMM] != encodedCube[UTL]:
        return False      
    if encodedCube[UMM] != encodedCube[UTR]:
        return False      
    if encodedCube[UMM] != encodedCube[UBL]:
        return False      
    if encodedCube[UMM] != encodedCube[UBR]:
        return False      

    return True

def isFish(encodedCube) -> bool:
    corners = 0
    if encodedCube[UMM] == encodedCube[UTL]:
        corners += 1      
    if encodedCube[UMM] == encodedCube[UTR]:
        corners += 1      
    if encodedCube[UMM] == encodedCube[UBL]:
        corners += 1      
    if encodedCube[UMM] == encodedCube[UBR]:
        corners += 1      

    return corners == 1
