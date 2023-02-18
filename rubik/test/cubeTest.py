'''
Created on Feb 17, 2023

@author: jra0027
'''
import unittest
from rubik.model.cube import Cube

class Test(unittest.TestCase):
    def test100_validColorQuantity(self):
        with self.assertRaises(ValueError):
            Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwx")
    
    def test101_validAlpha(self):
        with self.assertRaises(ValueError):
            Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyy:::::::::")
            
    def test102_validLength(self):
        with self.assertRaises(ValueError):
            Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwww")
    
    def test103_validDataType(self):
        with self.assertRaises(ValueError):
            Cube(None)
        with self.assertRaises(ValueError):
            Cube(0.2)
        with self.assertRaises(ValueError):
            Cube(1)
        with self.assertRaises(ValueError):
            Cube([])
        with self.assertRaises(ValueError):
            Cube({})
    
    def test104_uniqueCenters(self):
        with self.assertRaises(ValueError):
            Cube("bbbbbbbbbrrrrbrrrroooobooooggggbggggyyyybyyyywwwwbwwww")
    
    def test105_validDirections(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        with self.assertRaises(ValueError):
            test.rotate('Dd')
        test.rotate('')
        test.rotate('FfRrBbLlUu')
    
    def test106_rotateFrontClockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("F")
        self.assertEquals(test.get(), "bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww")
        
    def test107_rotateFrontCounterclockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("f")
        self.assertEquals(test.get(), "bbbbbbbbbwrrwrrwrroooooooooggyggyggyyyyyyyrrrgggwwwwww")
    
    def test108_rotateBackClockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("B")
        self.assertEquals(test.get(), "bbbbbbbbbrrwrrwrrwooooooooooggyggyggrrryyyyyywwwwwwggg")

    def test109_rotateBackCounterclockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("Bb")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")

    def test110_rotateLeftClockwise(self):
        pass
    
    def test111_rotateLeftCounterclockwise(self):
        pass
    
    def test112_rotateRightClockwise(self):
        pass
    
    def test113_rotateRightCounterclockwise(self):
        pass
    
    def test114_rotateUpClockwise(self):
        pass
    
    def test115_rotateUpCounterclockwise(self):
        pass    
    
    def test116_rotateDefault(self):
        pass
    
    def test117_rotateFront(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("FfFfFf")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
