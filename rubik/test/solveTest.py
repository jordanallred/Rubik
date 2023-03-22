from unittest import TestCase
from rubik.view.solve import solve
from rubik.model.cube import Cube
from rubik.model.constants import *


class SolveTest(TestCase):        

    def test100_solve_solveNominal(self):
        parms = {}
        encodedCube = "H6c56c556DDc6cBHHc6DHcBD66HD6BcHcDHc6BD55H5DBBB5BD5BH5"
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)

        cube = Cube(encodedCube)
        cube.rotate(result.get('solution'))
        
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
        
        
    def test100_solve_solveNominal(self):
        parms = {}
        encodedCube = "ggeSLaeaLLLaReeSgRRReSRReegSeLeaaaLgRSSLgSaLSLgaaSRRgg"
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)

        cube = Cube(encodedCube)
        cube.rotate(result.get('solution'))
        
        print(cube.get())

