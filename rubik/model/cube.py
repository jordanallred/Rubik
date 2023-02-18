from rubik.model.constants import *

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
        cubeCopy = self.cube
        # face values
        self.cube[0] = cubeCopy[6]
        self.cube[1] = cubeCopy[3]
        self.cube[2] = cubeCopy[0]
        self.cube[3] = cubeCopy[7]
        self.cube[5] = cubeCopy[1]
        self.cube[6] = cubeCopy[8]
        self.cube[7] = cubeCopy[5]
        self.cube[8] = cubeCopy[2]
        
        # edge values
        self.cube[9] = cubeCopy[42]
        self.cube[12] = cubeCopy[43]
        self.cube[15] = cubeCopy[44]
        self.cube[45] = cubeCopy[15]
        self.cube[46] = cubeCopy[12]
        self.cube[47] = cubeCopy[9]
        self.cube[29] = cubeCopy[45]
        self.cube[32] = cubeCopy[46]
        self.cube[35] = cubeCopy[47]
        self.cube[42] = cubeCopy[35]
        self.cube[43] = cubeCopy[32]
        self.cube[44] = cubeCopy[29]
 
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