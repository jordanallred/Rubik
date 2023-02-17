from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test100_rotateDefault(self):
        startCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = startCube
        parms['dir'] = 'F'
        
        result = rotate(parms)
        
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(startCube, result.get('cube'))
