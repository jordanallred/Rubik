from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.controller.bottomLayer import *
from rubik.model.constants import *


class BottomLayerTest(TestCase):
    def test101_solve_createDaisy(self):
        cube = Cube("766Cllx7CACxxCA7Ax77lC6A76AC6C6xllAAAxlCA76xC6lll7xx76")
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DTL], encodedCube[DMM])
        self.assertEqual(encodedCube[DTM], encodedCube[DMM])
        self.assertEqual(encodedCube[DTR], encodedCube[DMM])

        self.assertEqual(encodedCube[DML], encodedCube[DMM])
        self.assertEqual(encodedCube[DMR], encodedCube[DMM])

        self.assertEqual(encodedCube[DBL], encodedCube[DMM])
        self.assertEqual(encodedCube[DBM], encodedCube[DMM])
        self.assertEqual(encodedCube[DBR], encodedCube[DMM])
