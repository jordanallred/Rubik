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
        
    
    def get(self):
        return self.cube
        