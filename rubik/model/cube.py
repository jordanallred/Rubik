from rubik.model.constants import *
from numpy import rot90, ndarray

class Cube:
    '''
    Rubik's cube
    '''

    def __init__(self, encodedCube):
        if type(encodedCube) is not str:
            raise ValueError("Cube must not be of type String")
        uniqueColors = []
        for color in encodedCube:
            if color not in uniqueColors:
                uniqueColors.append(color)
        if len(uniqueColors) != 6:
            raise ValueError("Number of unique colors must be six.")
        
        if not encodedCube.isalnum():
            raise ValueError("Palette values must be alphanumeric.")
            
        if len(encodedCube) != 54:
            raise ValueError("Cube must have exactly 54 palette values.")
        
        if encodedCube[4] == encodedCube[13] or encodedCube[4] == encodedCube[22] or encodedCube[4] == encodedCube[31] or encodedCube[4] == encodedCube[40] or encodedCube[4] == encodedCube[49] \
        or encodedCube[13] == encodedCube[22] or encodedCube[13] == encodedCube[31] or encodedCube[13] == encodedCube[40] or encodedCube[13] == encodedCube[49] \
        or encodedCube[22] == encodedCube[31] or encodedCube[22] == encodedCube[40] or encodedCube[22] == encodedCube[49] \
        or encodedCube[31] == encodedCube[40] or encodedCube[22] == encodedCube[49] \
        or encodedCube[40] == encodedCube[49]:
            raise ValueError("Cube must have unique centers.")
        
        self.cube = encodedCube
        
    def rotate(self, directions):
        validDirections = {'F', 'f', 'B', 'b', 'L', 'l', 'R', 'r', 'U', 'u'}
        if len(set(directions).difference(validDirections)) > 0:
            raise ValueError("Input contains invalid rotation direction.")
        
        if len(directions):
            directions = "F"
        
        while len(directions) > 0:
            if directions[0] == 'F':
                self._rotateFrontClockwise()
            elif directions[0] == 'f':
                self._rotateFrontCounterclockwise()
            elif directions[0] == 'B':
                self._rotateBackClockwise()
            elif directions[0] == 'b':
                self._rotateBackCounterclockwise()
            elif directions[0] == 'L':
                self._rotateLeftClockwise()
            elif directions[0] == 'l':
                self._rotateLeftCounterclockwise()
            elif directions[0] == 'R':
                self._rotateRightClockwise()
            elif directions[0] == 'r':
                self._rotateRightCounterclockwise()
            elif directions[0] == 'U':
                self._rotateUpClockwise()
            elif directions[0] == 'u':
                self._rotateUpCounterclockwise()
            
            directions = directions[1:] if len(directions) > 1 else []
        
    
    def get(self):
        return self.cube
    
    def _rotateFrontClockwise(self):
        encodedCube = self.cube
        cubeArray = ndarray((3, 3, 3), data=encodedCube)
        print(cubeArray)
 
    def _rotateFrontCounterclockwise(self):
        pass
    
    def _rotateBackClockwise(self):
        pass
    
    def _rotateBackCounterclockwise(self):
        pass

    def _rotateLeftClockwise(self):
        pass
    
    def _rotateLeftCounterclockwise(self):
        pass
    
    def _rotateRightClockwise(self):
        pass
    
    def _rotateRightCounterclockwise(self):
        pass
    
    def _rotateUpClockwise(self):
        pass
    
    def _rotateUpCounterclockwise(self):
        pass