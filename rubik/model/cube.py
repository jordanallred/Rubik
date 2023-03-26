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
        if len(uniqueColors) != NUM_FACES:
            raise ValueError(f"Number of unique colors must be {NUM_FACES}.")
        
        if not encodedCube.isalnum():
            raise ValueError("Palette values must be alphanumeric.")
            
        if len(encodedCube) != NUM_ELEMENTS:
            raise ValueError("Cube must have exactly 54 palette values.")
        
        if len([encodedCube[FMM], encodedCube[BMM], encodedCube[LMM], encodedCube[RMM], encodedCube[UMM], encodedCube[DMM]]) != len(set([encodedCube[FMM], encodedCube[BMM], encodedCube[LMM], encodedCube[RMM], encodedCube[UMM], encodedCube[DMM]])):
            raise ValueError("Cube must have unique centers.")
        
        self.cube = encodedCube
        
    def rotate(self, directions):
        
        if len(directions) == 0:
            directions = "F"
        
        while len(directions) > 0:
            if not VALID_DIRECTIONS.__contains__(directions[0]):
                print(directions)
                raise ValueError("Input contains invalid rotation direction.")

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
            
            if len(directions) > 1:
                directions = directions[1:]
            else:
                directions = []        
    
    def get(self):
        return self.cube
    
    def _changePalette(self, encodedCube, newPosition, oldPosition):
            return encodedCube[:newPosition] + self.cube[oldPosition] + encodedCube[newPosition + 1:]
    
    def _changePaletteReverse(self, encodedCube, newPosition, oldPosition):
            return encodedCube[:oldPosition] + self.cube[newPosition] + encodedCube[oldPosition + 1:]
    
    def _rotateFront(self, swapFunction):
        encodedCube = self.cube
        
        # top row of front face
        encodedCube = swapFunction(encodedCube, FTL, FBL)
        encodedCube = swapFunction(encodedCube, FTM, FML)
        encodedCube = swapFunction(encodedCube, FTR, FTL)

        # middle row of front face
        encodedCube = swapFunction(encodedCube, FML, FBM)
        encodedCube = swapFunction(encodedCube, FMR, FTM)

        # bottom row of front face
        encodedCube = swapFunction(encodedCube, FBL, FBR)
        encodedCube = swapFunction(encodedCube, FBM, FMR)
        encodedCube = swapFunction(encodedCube, FBR, FTR)

        # bottom row of up face
        encodedCube = swapFunction(encodedCube, UBL, LBR)
        encodedCube = swapFunction(encodedCube, UBM, LMR)
        encodedCube = swapFunction(encodedCube, UBR, LTR)

        # left column of right face
        encodedCube = swapFunction(encodedCube, RTL, UBL)
        encodedCube = swapFunction(encodedCube, RML, UBM)
        encodedCube = swapFunction(encodedCube, RBL, UBR)

        # top row of down face
        encodedCube = swapFunction(encodedCube, DTR, RTL)
        encodedCube = swapFunction(encodedCube, DTM, RML)
        encodedCube = swapFunction(encodedCube, DTL, RBL)
        
        # right column of left face
        encodedCube = swapFunction(encodedCube, LBR, DTR)
        encodedCube = swapFunction(encodedCube, LMR, DTM)
        encodedCube = swapFunction(encodedCube, LTR, DTL)
        
        self.cube = encodedCube

    def _rotateFrontClockwise(self):
        self._rotateFront(self._changePalette)

    def _rotateFrontCounterclockwise(self):
        self._rotateFront(self._changePaletteReverse)
    
    def _rotateBack(self, swapFunction):
        encodedCube = self.cube
        
        # top row of back face
        encodedCube = swapFunction(encodedCube, BTL, BBL)
        encodedCube = swapFunction(encodedCube, BTM, BML)
        encodedCube = swapFunction(encodedCube, BTR, BTL)

        # middle row of back face
        encodedCube = swapFunction(encodedCube, BML, BBM)
        encodedCube = swapFunction(encodedCube, BMR, BTM)

        # bottom row of back face
        encodedCube = swapFunction(encodedCube, BBL, BBR)
        encodedCube = swapFunction(encodedCube, BBM, BMR)
        encodedCube = swapFunction(encodedCube, BBR, BTR)

        # top row of up face
        encodedCube = swapFunction(encodedCube, UTL, RTR)
        encodedCube = swapFunction(encodedCube, UTM, RMR)
        encodedCube = swapFunction(encodedCube, UTR, RBR)

        # left column of left face
        encodedCube = swapFunction(encodedCube, LBL, UTL)
        encodedCube = swapFunction(encodedCube, LML, UTM)
        encodedCube = swapFunction(encodedCube, LTL, UTR)
        
        # bottom row of down face
        encodedCube = swapFunction(encodedCube, DBR, LBL)
        encodedCube = swapFunction(encodedCube, DBM, LML)
        encodedCube = swapFunction(encodedCube, DBL, LTL)        
        
        # right column of right face
        encodedCube = swapFunction(encodedCube, RTR, DBR)
        encodedCube = swapFunction(encodedCube, RMR, DBM)
        encodedCube = swapFunction(encodedCube, RBR, DBL)

        self.cube = encodedCube

    def _rotateBackClockwise(self):
        self._rotateBack(self._changePalette)
    
    def _rotateBackCounterclockwise(self):
        self._rotateBack(self._changePaletteReverse)
    
    def _rotateLeft(self, swapFunction):
        encodedCube = self.cube
        
        # top row of left face
        encodedCube = swapFunction(encodedCube, LTL, LBL)
        encodedCube = swapFunction(encodedCube, LTM, LML)
        encodedCube = swapFunction(encodedCube, LTR, LTL)

        # middle row of left face
        encodedCube = swapFunction(encodedCube, LML, LBM)
        encodedCube = swapFunction(encodedCube, LMR, LTM)

        # bottom row of left face
        encodedCube = swapFunction(encodedCube, LBL, LBR)
        encodedCube = swapFunction(encodedCube, LBM, LMR)
        encodedCube = swapFunction(encodedCube, LBR, LTR)

        # left column of up face
        encodedCube = swapFunction(encodedCube, UTL, BBR)
        encodedCube = swapFunction(encodedCube, UML, BMR)
        encodedCube = swapFunction(encodedCube, UBL, BTR)

        # left column of front face
        encodedCube = swapFunction(encodedCube, FTL, UTL)
        encodedCube = swapFunction(encodedCube, FML, UML)
        encodedCube = swapFunction(encodedCube, FBL, UBL)
        
        # left column of down face
        encodedCube = swapFunction(encodedCube, DTL, FTL)
        encodedCube = swapFunction(encodedCube, DML, FML)
        encodedCube = swapFunction(encodedCube, DBL, FBL)        
        
        # left column of back face
        encodedCube = swapFunction(encodedCube, BBR, DTL)
        encodedCube = swapFunction(encodedCube, BMR, DML)
        encodedCube = swapFunction(encodedCube, BTR, DBL)

        self.cube = encodedCube
    
    def _rotateLeftClockwise(self):
        self._rotateLeft(self._changePalette)
    
    def _rotateLeftCounterclockwise(self):
        self._rotateLeft(self._changePaletteReverse)

    def _rotateRight(self, swapFunction):
        encodedCube = self.cube
        
        # top row of right face
        encodedCube = swapFunction(encodedCube, RTL, RBL)
        encodedCube = swapFunction(encodedCube, RTM, RML)
        encodedCube = swapFunction(encodedCube, RTR, RTL)

        # middle row of right face
        encodedCube = swapFunction(encodedCube, RML, RBM)
        encodedCube = swapFunction(encodedCube, RMR, RTM)

        # bottom row of right face
        encodedCube = swapFunction(encodedCube, RBL, RBR)
        encodedCube = swapFunction(encodedCube, RBM, RMR)
        encodedCube = swapFunction(encodedCube, RBR, RTR)

        # right column of up face
        encodedCube = swapFunction(encodedCube, UTR, FTR)
        encodedCube = swapFunction(encodedCube, UMR, FMR)
        encodedCube = swapFunction(encodedCube, UBR, FBR)

        # right column of back face
        encodedCube = swapFunction(encodedCube, BBL, UTR)
        encodedCube = swapFunction(encodedCube, BML, UMR)
        encodedCube = swapFunction(encodedCube, BTL, UBR)
        
        # right column of down face
        encodedCube = swapFunction(encodedCube, DTR, BBL)
        encodedCube = swapFunction(encodedCube, DMR, BML)
        encodedCube = swapFunction(encodedCube, DBR, BTL)        
        
        # right column of front face
        encodedCube = swapFunction(encodedCube, FTR, DTR)
        encodedCube = swapFunction(encodedCube, FMR, DMR)
        encodedCube = swapFunction(encodedCube, FBR, DBR)

        self.cube = encodedCube
    
    def _rotateRightClockwise(self):
        self._rotateRight(self._changePalette)
    
    def _rotateRightCounterclockwise(self):
        self._rotateRight(self._changePaletteReverse)

    def _rotateUp(self, swapFunction):
        encodedCube = self.cube
        
        # top row of up face
        encodedCube = swapFunction(encodedCube, UTL, UBL)
        encodedCube = swapFunction(encodedCube, UTM, UML)
        encodedCube = swapFunction(encodedCube, UTR, UTL)

        # middle row of up face
        encodedCube = swapFunction(encodedCube, UML, UBM)
        encodedCube = swapFunction(encodedCube, UMR, UTM)

        # bottom row of up face
        encodedCube = swapFunction(encodedCube, UBL, UBR)
        encodedCube = swapFunction(encodedCube, UBM, UMR)
        encodedCube = swapFunction(encodedCube, UBR, UTR)

        # top row of front face
        encodedCube = swapFunction(encodedCube, FTL, RTL)
        encodedCube = swapFunction(encodedCube, FTM, RTM)
        encodedCube = swapFunction(encodedCube, FTR, RTR)

        # top row of left face
        encodedCube = swapFunction(encodedCube, LTL, FTL)
        encodedCube = swapFunction(encodedCube, LTM, FTM)
        encodedCube = swapFunction(encodedCube, LTR, FTR)
        
        # top row of back face
        encodedCube = swapFunction(encodedCube, BTL, LTL)
        encodedCube = swapFunction(encodedCube, BTM, LTM)
        encodedCube = swapFunction(encodedCube, BTR, LTR)        
        
        # top row of right face
        encodedCube = swapFunction(encodedCube, RTL, BTL)
        encodedCube = swapFunction(encodedCube, RTM, BTM)
        encodedCube = swapFunction(encodedCube, RTR, BTR)

        self.cube = encodedCube

    def _rotateUpClockwise(self):
        self._rotateUp(self._changePalette)
    
    def _rotateUpCounterclockwise(self):
        self._rotateUp(self._changePaletteReverse)
        
    def left_trigger(self, face):
        rotations = face.left.letter.lower() + 'u' + face.left.letter.upper()
        self.rotate(rotations)
        return rotations

    def right_trigger(self, face):
        rotations = face.right.letter.upper() + 'U' + face.right.letter.lower()
        self.rotate(rotations)
        return rotations
    
    def print_row(self, left):
        for index in range(left, left + 3):
            print(self.cube[index] + '\t', end='')
        print('\t', end='')

    def visualize(self):
        print('\t\t\t\t', end='')
        self.print_row(36)
        print('\n\t\t\t\t', end='')
        self.print_row(39)
        print('\n\t\t\t\t', end='')
        self.print_row(42)
        print('\n')
                
        self.print_row(27)
        self.print_row(0)
        self.print_row(9)
        self.print_row(18)
        
        print()
        
        self.print_row(30)
        self.print_row(3)
        self.print_row(12)
        self.print_row(21)

        print()
        
        self.print_row(33)
        self.print_row(6)
        self.print_row(15)
        self.print_row(24)
        
        print('\n\n\t\t\t\t', end='')
        self.print_row(45)
        print('\n\t\t\t\t', end='')
        self.print_row(48)
        print('\n\t\t\t\t', end='')
        self.print_row(51)
        print('\n')

        
        