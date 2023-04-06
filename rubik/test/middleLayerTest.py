from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.controller.bottomLayer import *
from rubik.controller.middleLayer import *
from rubik.model.constants import *
from rubik.test.tools import create_cube

class BottomLayerTest(TestCase):
    def test101_solve_solveFML(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[FML], encodedCube[FMM])

    def test102_solve_solveFMR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[FMR], encodedCube[FMM])

    def test103_solve_solveRML(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[RML], encodedCube[RMM])

    def test104_solve_solveRMR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[RMR], encodedCube[RMM])

    def test105_solve_solveBML(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[BML], encodedCube[BMM])

    def test106_solve_solveBMR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[BMR], encodedCube[BMM])

    def test107_solve_solveLML(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[LML], encodedCube[LMM])

    def test108_solve_solveLMR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
                
        encodedCube = cube.get()
        self.assertEqual(encodedCube[LMR], encodedCube[LMM])
