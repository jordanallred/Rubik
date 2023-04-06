from unittest import TestCase
from rubik.view.solve import solve
from rubik.model.cube import Cube
from rubik.model.constants import *
from rubik.test.tools import create_cube

class SolveTest(TestCase):        

    def test100_solve_solveNominal(self):
        parms = {}
        encodedCube = create_cube().get()
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)

        cube = Cube(encodedCube)
        cube.rotate(result.get('solution'))