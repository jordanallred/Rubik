from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    rotations += solveBottomLayer(theCube)      #iteration 3
    rotations += solveMiddleLayer(theCube)      #iteration 4
    rotations += solveUpCross(theCube)          #iteration 5
    rotations += solveUpSurface(theCube)        #iteration 5
    rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    result['status'] = 'ok'  
    
    itemToTokenize = encodedCube + rotations + 'allrejr'
    sha256hash = hashlib.sha256()
    sha256hash.update(itemToTokenize.encode())
    fullToken = sha256hash.hexdigest()
    
    index = random.randrange(len(fullToken) - 8)
    result['integrity'] = fullToken[index: index + 8]   #iteration 3
                     
    return result