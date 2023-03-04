from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
    def test100_sampleRotate(self):
        startCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = startCube
        parms['dir'] = 'F'
        
        result = rotate(parms)
        
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww', result.get('cube'))

    def test101_defaultRotate(self):
        startCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        
        parms['cube'] = startCube
        parms['dir'] = 'F'
        result1 = rotate(parms)
        
        parms['cube'] = startCube
        parms['dir'] = ''
        result2 = rotate(parms)
        
        self.assertEqual(result1.get('cube'), result2.get('cube'))
                    
    def test103_paramDir(self):
        startCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        
        parms['cube'] = startCube
        parms['direction'] = 'F'
        
        with self.assertRaises(ValueError):
            rotate(parms)
            
    def test104_paramCube(self):
        startCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        
        parms['wrong'] = startCube
        parms['dir'] = 'F'
        
        with self.assertRaises(ValueError):
            rotate(parms)