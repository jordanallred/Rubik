from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.model.constants import *
from rubik.test.tools import create_cube


class BottomCrossTest(TestCase):
    def test101_solve_createDaisy01(self):
        cube = create_cube()
        solution = createDaisy(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[UTM])

    def test102_solve_createDaisy02(self):
        cube = create_cube()
        solution = createDaisy(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[UML])

    def test103_solve_createDaisy03(self):
        cube = create_cube()
        solution = createDaisy(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[UMR])

    def test104_solve_createDaisy04(self):
        cube = create_cube()
        solution = createDaisy(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[UBM])
    
    def test105_solve_bottomCross01(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[FMM], encodedCube[FBM])

    def test106_solve_bottomCross02(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[RMM], encodedCube[RBM])

    def test107_solve_bottomCross03(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[BMM], encodedCube[BBM])

    def test108_solve_bottomCross04(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[LMM], encodedCube[LBM])

    def test109_solve_bottomCross05(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[DTM])
        
    def test110_solve_bottomCross06(self):
        cube = create_cube()
        solution = createDaisy(cube)
                
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[DML])

    def test111_solve_bottomCross07(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[DMR])

    def test112_solve_bottomCross08(self):
        cube = create_cube()
        solution = createDaisy(cube)
        
        solution = createBottomCross(cube)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[DBM])
        