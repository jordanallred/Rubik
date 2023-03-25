from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    cubeCopy = theCube
    encodedCube = cubeCopy.get()
    
    if encodedCube[FTL] == encodedCube[BMM]:
        if encodedCube[LTR] == encodedCube[LMM]:
            cubeCopy.
    
    return ''
    
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