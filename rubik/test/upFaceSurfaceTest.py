from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.controller.bottomLayer import *
from rubik.controller.middleLayer import *
from rubik.controller.upFaceCross import *
from rubik.controller.upFaceSurface import *
from rubik.model.constants import *
from rubik.test.tools import create_cube

class UpFaceSurfaceTest(TestCase):
    def test101_solve_solveUTL(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UTL])

    def test102_solve_solveUTR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UTR])
        
    def test103_solve_solveUBL(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)

        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UBL])
        
    def test104_solve_solveUBR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UBR])
