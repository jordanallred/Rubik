from rubik.model.constants import *
from rubik.model.cube import Cube

solution = ''

def solveUpCross(theCube: Cube) -> str:
    global solution
    encodedCube = theCube.get()
    
    while not middleSolved(encodedCube):
        pass
    
    return solution
    
def middleSolved(encodedCube) -> bool:        
    return True