from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube
from rubik.model.constants import *
import hashlib
import random

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    verifyCube(theCube)
    
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

def verifyCube(theCube: Cube) -> bool:
    colorMatrix = {}
    colors = []
    encodedCube = theCube.get()
    
    for panel in encodedCube:
        if panel not in colors:
            colors.append(panel)
            colorMatrix[panel] = {}
        
    for color1 in colors:
        for color2 in colors:
            if color1 == color2:
                continue
            colorMatrix[color1][color2] = 0
    
    for panel in PANEL_LIST:
        if panel.left is not None:
            colorMatrix[encodedCube[panel.position]][encodedCube[panel.left.position]] += 1
        if panel.right is not None:
            colorMatrix[encodedCube[panel.position]][encodedCube[panel.right.position]] += 1
        if panel.up is not None:
            colorMatrix[encodedCube[panel.position]][encodedCube[panel.up.position]] += 1
        if panel.down is not None:
            colorMatrix[encodedCube[panel.position]][encodedCube[panel.down.position]] += 1
    
    for color1 in colors:
        for color2 in colors:
            if color1 == color2:
                continue
            if colorMatrix[color1][color2] != 0 and colorMatrix[color1][color2] != 3:
                Exception("Unsolvable Cube") 
            