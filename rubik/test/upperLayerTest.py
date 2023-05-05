from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.controller.bottomLayer import *
from rubik.controller.middleLayer import *
from rubik.controller.upFaceCross import *
from rubik.controller.upFaceSurface import *
from rubik.controller.upperLayer import *
from rubik.model.constants import *
from rubik.test.tools import create_cube

class UpFaceSurfaceTest(TestCase):
    def test101_solve_solveFTL(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[FMM], encodedCube[FTL])

    def test102_solve_solveFTM(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[FMM], encodedCube[FTM])
        
    def test103_solve_solveFTR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[FMM], encodedCube[FTR])

    def test104_solve_solveRTL(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[RMM], encodedCube[RTL])

    def test105_solve_solveRTM(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[RMM], encodedCube[RTM])
        
    def test106_solve_solveRTR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[RMM], encodedCube[RTR])
    
    def test107_solve_solveBTL(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[BMM], encodedCube[BTL])

    def test108_solve_solveBTM(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[BMM], encodedCube[BTM])
        
    def test109_solve_solveBTR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[BMM], encodedCube[BTR])
    
    def test110_solve_solveLTL(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[LMM], encodedCube[LTL])

    def test111_solve_solveLTM(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[LMM], encodedCube[LTM])
        
    def test112_solve_solveBTR(self):
        cube = create_cube()
        solveBottomCross(cube)    
        solveBottomLayer(cube)
        solveMiddleLayer(cube)
        solveUpCross(cube)
        solveUpSurface(cube)
        solveUpperLayer(cube)
        
        encodedCube = cube.get()
        self.assertEqual(encodedCube[LMM], encodedCube[LTR])
    
