from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.controller.bottomLayer import *
from rubik.controller.middleLayer import *
from rubik.controller.upFaceCross import *
from rubik.model.constants import *
from rubik.test.tools import create_cube

class UpFaceCrossTest(TestCase):
    def test101_solve_solveUTM(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UTM])

    def test102_solve_solveUML(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UML])
        
    def test103_solve_solveUMR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UMR])
        
    def test104_solve_solveUBM(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[UMM], encodedCube[UBM])
