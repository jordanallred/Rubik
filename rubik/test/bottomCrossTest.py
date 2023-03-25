from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.model.constants import *
from rubik.test.tools import create_cube


class BottomCrossTest(TestCase):
    def test101_solve_createDaisy(self):
        cube = create_cube()
        solution = createDaisy(cube)
        cube.rotate(solution)
        encodedCube = cube.get()
                
        self.assertEqual(encodedCube[DMM], encodedCube[UTM])
        self.assertEqual(encodedCube[DMM], encodedCube[UML])
        self.assertEqual(encodedCube[DMM], encodedCube[UMR])
        self.assertEqual(encodedCube[DMM], encodedCube[UBM])
    
    def test102_solve_createBottomCross(self):
        cube = create_cube()
        solution = createDaisy(cube)
        cube.rotate(solution)
        
        solution = createBottomCross(cube)
        cube.rotate(solution)
        encodedCube = cube.get()
                
        # checking centers matching palette underneath
        self.assertEqual(encodedCube[FMM], encodedCube[FBM])
        self.assertEqual(encodedCube[RMM], encodedCube[RBM])
        self.assertEqual(encodedCube[BMM], encodedCube[BBM])
        self.assertEqual(encodedCube[LMM], encodedCube[LBM])

        # checking bottom cross is formed
        self.assertEqual(encodedCube[DMM], encodedCube[DTM])
        self.assertEqual(encodedCube[DMM], encodedCube[DML])
        self.assertEqual(encodedCube[DMM], encodedCube[DMR])
        self.assertEqual(encodedCube[DMM], encodedCube[DBM])
        