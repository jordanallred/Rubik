import rubik.model.constants
from rubik.model.cube import Cube

solution = ''

def solveUpperLayer(theCube: Cube) -> str:
    global solution
    
    encodedCube = theCube.get()
    
    solution += solveCorners(encodedCube)
    solution += solveLayer(encodedCube)

def solveCorners(encodedCube) -> str:
    pass

def solveLayer(encodedCube) -> str:
    pass
