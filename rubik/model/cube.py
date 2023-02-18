from rubik.model.constants import *
from numpy import rot90

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
        
        if len(directions) == 0:
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
        encodedCube = ""
        newFace = ""
        faceList = [[self.cube[0], self.cube[1], self.cube[2]], [self.cube[3], self.cube[4], self.cube[5]], [self.cube[6], self.cube[7], self.cube[8]]]
        faceList = rot90(faceList, 3)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(9, 54):
            match i:
                case 9:
                    encodedCube += self.cube[42]
                case 12:
                    encodedCube += self.cube[43]
                case 15:
                    encodedCube += self.cube[44]
                case 47:
                    encodedCube += self.cube[9]
                case 46:
                    encodedCube += self.cube[12]
                case 45:
                    encodedCube += self.cube[15]
                case 35:
                    encodedCube += self.cube[47]
                case 32:
                    encodedCube += self.cube[46]
                case 29:
                    encodedCube += self.cube[45]
                case 44:
                    encodedCube += self.cube[29]
                case 43:
                    encodedCube += self.cube[32]
                case 42:
                    encodedCube += self.cube[35]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube
        
 
    def _rotateFrontCounterclockwise(self):
        encodedCube = ""
        newFace = ""
        faceList = [[self.cube[0], self.cube[1], self.cube[2]], [self.cube[3], self.cube[4], self.cube[5]], [self.cube[6], self.cube[7], self.cube[8]]]
        faceList = rot90(faceList)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(9, 54):
            match i:
                case 42:
                    encodedCube += self.cube[9]
                case 43:
                    encodedCube += self.cube[12]
                case 44:
                    encodedCube += self.cube[15]
                case 9:
                    encodedCube += self.cube[47]
                case 12:
                    encodedCube += self.cube[46]
                case 15:
                    encodedCube += self.cube[45]
                case 47:
                    encodedCube += self.cube[35]
                case 46:
                    encodedCube += self.cube[32]
                case 45:
                    encodedCube += self.cube[29]
                case 29:
                    encodedCube += self.cube[44]
                case 32:
                    encodedCube += self.cube[43]
                case 35:
                    encodedCube += self.cube[42]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube
    
    def _rotateBackClockwise(self):
        encodedCube = ""
        
        for i in range(18):
            match i:
                case 11:
                    encodedCube += self.cube[53]
                case 14:
                    encodedCube += self.cube[52]
                case 17:
                    encodedCube += self.cube[51]
                case 36:
                    encodedCube += self.cube[11]
                case 37:
                    encodedCube += self.cube[14]
                case 38:
                    encodedCube += self.cube[17]
                case 33:
                    encodedCube += self.cube[36]
                case 30:
                    encodedCube += self.cube[37]
                case 27:
                    encodedCube += self.cube[38]
                case 53:
                    encodedCube += self.cube[33]
                case 52:
                    encodedCube += self.cube[30]
                case 51:
                    encodedCube += self.cube[27]
                case _:
                    encodedCube += self.cube[i]
                    
        newFace = ""
        faceList = [[self.cube[18:21]], [self.cube[21:24]], [self.cube[24:27]]]
        faceList = rot90(faceList, 3)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(27, 54):
            match i:
                case 11:
                    encodedCube += self.cube[53]
                case 14:
                    encodedCube += self.cube[52]
                case 17:
                    encodedCube += self.cube[51]
                case 36:
                    encodedCube += self.cube[11]
                case 37:
                    encodedCube += self.cube[14]
                case 38:
                    encodedCube += self.cube[17]
                case 33:
                    encodedCube += self.cube[36]
                case 30:
                    encodedCube += self.cube[37]
                case 27:
                    encodedCube += self.cube[38]
                case 53:
                    encodedCube += self.cube[33]
                case 52:
                    encodedCube += self.cube[30]
                case 51:
                    encodedCube += self.cube[27]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube
    
    def _rotateBackCounterclockwise(self):
        encodedCube = ""
        
        for i in range(18):
            match i:
                case 53:
                    encodedCube += self.cube[11]
                case 52:
                    encodedCube += self.cube[14]
                case 51:
                    encodedCube += self.cube[17]
                case 11:
                    encodedCube += self.cube[36]
                case 14:
                    encodedCube += self.cube[37]
                case 17:
                    encodedCube += self.cube[38]
                case 36:
                    encodedCube += self.cube[33]
                case 37:
                    encodedCube += self.cube[30]
                case 38:
                    encodedCube += self.cube[27]
                case 33:
                    encodedCube += self.cube[53]
                case 30:
                    encodedCube += self.cube[52]
                case 27:
                    encodedCube += self.cube[51]
                case _:
                    encodedCube += self.cube[i]
                    
        newFace = ""
        faceList = [[self.cube[18:21]], [self.cube[21:24]], [self.cube[24:27]]]
        faceList = rot90(faceList)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(27, 54):
            match i:
                case 53:
                    encodedCube += self.cube[11]
                case 52:
                    encodedCube += self.cube[14]
                case 51:
                    encodedCube += self.cube[17]
                case 11:
                    encodedCube += self.cube[36]
                case 14:
                    encodedCube += self.cube[37]
                case 17:
                    encodedCube += self.cube[38]
                case 36:
                    encodedCube += self.cube[33]
                case 37:
                    encodedCube += self.cube[30]
                case 38:
                    encodedCube += self.cube[27]
                case 33:
                    encodedCube += self.cube[53]
                case 30:
                    encodedCube += self.cube[52]
                case 27:
                    encodedCube += self.cube[51]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube

    def _rotateLeftClockwise(self):
        encodedCube = ""
        
        for i in range(27):
            match i:
                case 0:
                    encodedCube += self.cube[36]
                case 3:
                    encodedCube += self.cube[39]
                case 6:
                    encodedCube += self.cube[42]
                case 45:
                    encodedCube += self.cube[0]
                case 48:
                    encodedCube += self.cube[3]
                case 51:
                    encodedCube += self.cube[6]
                case 26:
                    encodedCube += self.cube[45]
                case 23:
                    encodedCube += self.cube[48]
                case 20:
                    encodedCube += self.cube[51]
                case 36:
                    encodedCube += self.cube[26]
                case 39:
                    encodedCube += self.cube[23]
                case 42:
                    encodedCube += self.cube[20]
                case _:
                    encodedCube += self.cube[i]
                    
        newFace = ""
        faceList = [[self.cube[27:30]], [self.cube[30:33]], [self.cube[33:36]]]
        faceList = rot90(faceList, 3)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(36, 54):
            match i:
                case 0:
                    encodedCube += self.cube[36]
                case 3:
                    encodedCube += self.cube[39]
                case 6:
                    encodedCube += self.cube[42]
                case 45:
                    encodedCube += self.cube[0]
                case 48:
                    encodedCube += self.cube[3]
                case 51:
                    encodedCube += self.cube[6]
                case 26:
                    encodedCube += self.cube[45]
                case 23:
                    encodedCube += self.cube[48]
                case 20:
                    encodedCube += self.cube[51]
                case 36:
                    encodedCube += self.cube[26]
                case 39:
                    encodedCube += self.cube[23]
                case 42:
                    encodedCube += self.cube[20]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube
    
    def _rotateLeftCounterclockwise(self):
        encodedCube = ""
        
        for i in range(27):
            match i:
                case 36:
                    encodedCube += self.cube[0]
                case 39:
                    encodedCube += self.cube[3]
                case 42:
                    encodedCube += self.cube[6]
                case 0:
                    encodedCube += self.cube[45]
                case 3:
                    encodedCube += self.cube[48]
                case 6:
                    encodedCube += self.cube[51]
                case 45:
                    encodedCube += self.cube[26]
                case 48:
                    encodedCube += self.cube[23]
                case 51:
                    encodedCube += self.cube[20]
                case 26:
                    encodedCube += self.cube[36]
                case 23:
                    encodedCube += self.cube[39]
                case 20:
                    encodedCube += self.cube[42]
                case _:
                    encodedCube += self.cube[i]
                    
        newFace = ""
        faceList = [[self.cube[27:30]], [self.cube[30:33]], [self.cube[33:36]]]
        faceList = rot90(faceList)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(36, 54):
            match i:
                case 36:
                    encodedCube += self.cube[0]
                case 39:
                    encodedCube += self.cube[3]
                case 42:
                    encodedCube += self.cube[6]
                case 0:
                    encodedCube += self.cube[45]
                case 3:
                    encodedCube += self.cube[48]
                case 6:
                    encodedCube += self.cube[51]
                case 45:
                    encodedCube += self.cube[26]
                case 48:
                    encodedCube += self.cube[23]
                case 51:
                    encodedCube += self.cube[20]
                case 26:
                    encodedCube += self.cube[36]
                case 23:
                    encodedCube += self.cube[39]
                case 20:
                    encodedCube += self.cube[42]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube
    
    def _rotateRightClockwise(self):
        encodedCube = ""
        
        for i in range(9):
            match i:
                case 44:
                    encodedCube += self.cube[8]
                case 41:
                    encodedCube += self.cube[5]
                case 38:
                    encodedCube += self.cube[2]
                case 18:
                    encodedCube += self.cube[44]
                case 21:
                    encodedCube += self.cube[41]
                case 24:
                    encodedCube += self.cube[53]
                case 53:
                    encodedCube += self.cube[18]
                case 50:
                    encodedCube += self.cube[21]
                case 47:
                    encodedCube += self.cube[24]
                case 8:
                    encodedCube += self.cube[53]
                case 5:
                    encodedCube += self.cube[50]
                case 2:
                    encodedCube += self.cube[47]
                case _:
                    encodedCube += self.cube[i]
                    
        newFace = ""
        faceList = [[self.cube[9:12]], [self.cube[12:15]], [self.cube[15:18]]]
        faceList = rot90(faceList, 3)
        for row in faceList:
            for item in row:
                newFace += item
        
        encodedCube += newFace
        
        for i in range(18, 54):
            match i:
                case 44:
                    encodedCube += self.cube[8]
                case 41:
                    encodedCube += self.cube[5]
                case 38:
                    encodedCube += self.cube[2]
                case 18:
                    encodedCube += self.cube[44]
                case 21:
                    encodedCube += self.cube[41]
                case 24:
                    encodedCube += self.cube[53]
                case 53:
                    encodedCube += self.cube[18]
                case 50:
                    encodedCube += self.cube[21]
                case 47:
                    encodedCube += self.cube[24]
                case 8:
                    encodedCube += self.cube[53]
                case 5:
                    encodedCube += self.cube[50]
                case 2:
                    encodedCube += self.cube[47]
                case _:
                    encodedCube += self.cube[i]
        self.cube = encodedCube
    
    def _rotateRightCounterclockwise(self):
        pass
    
    def _rotateUpClockwise(self):
        pass
    
    def _rotateUpCounterclockwise(self):
        pass