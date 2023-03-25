from unittest import TestCase
from rubik.model.cube import Cube
from rubik.controller.bottomCross import *
from rubik.controller.bottomLayer import *
from rubik.model.constants import *
from rubik.test.tools import create_cube

class BottomLayerTest(TestCase):
    def test101_solve_solveDTL(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DTL], encodedCube[DMM])


    def test102_solve_solveDTM(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DTM], encodedCube[DMM])


    def test103_solve_solveDTR(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DTR], encodedCube[DMM])


    def test104_solve_solveDML(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()

        self.assertEqual(encodedCube[DML], encodedCube[DMM])


    def test105_solve_solveDMR(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DMR], encodedCube[DMM])


    def test106_solve_solveDBL(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DBL], encodedCube[DMM])


    def test107_solve_solveDBM(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DBM], encodedCube[DMM])


    def test108_solve_solveDBR(self):
        cube = create_cube()
        solution = solveBottomCross(cube)
        cube.rotate(solution)
        
        solution = solveBottomLayer(cube)
        cube.rotate(solution)
        
        encodedCube = cube.get()
        
        self.assertEqual(encodedCube[DBR], encodedCube[DMM])
