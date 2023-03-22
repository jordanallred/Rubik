from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.model.constants import *


class BottomCrossTest(TestCase):
    def test101_solve_createDaisy(self):
        cube = Cube("yrbgogybgwwwyywwogoyrorwywbgrbrwowrbybgbgbogrrgrybyogo")
        solution = createDaisy(cube)
        cube.rotate(solution)
        bottomCrossColor = cube.cube[DMM]
                
        self.assertEqual(bottomCrossColor, cube.cube[UTM])
        self.assertEqual(bottomCrossColor, cube.cube[UML])
        self.assertEqual(bottomCrossColor, cube.cube[UMR])
        self.assertEqual(bottomCrossColor, cube.cube[UBM])
    
    def test102_solve_createBottomCross(self):
        cube = Cube("wrrbywgwyyywbowgrgrowrwryybowobrooorggbgbgbgbworygyybo")
        solution = createBottomCross(cube)
        cube.rotate(solution)
        
        # checking centers matching palette underneath
        self.assertEqual(cube.cube[FMM], cube.cube[FBM])
        self.assertEqual(cube.cube[RMM], cube.cube[RBM])
        self.assertEqual(cube.cube[BMM], cube.cube[BBM])
        self.assertEqual(cube.cube[LMM], cube.cube[LBM])

        # checking bottom cross is formed
        self.assertEqual(cube.cube[DMM], cube.cube[DTM])
        self.assertEqual(cube.cube[DMM], cube.cube[DML])
        self.assertEqual(cube.cube[DMM], cube.cube[DMR])
        self.assertEqual(cube.cube[DMM], cube.cube[DBM])
        