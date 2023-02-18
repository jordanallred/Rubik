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
        self.assertEquals(test.get(), "bbbbbbbbbrrwrrwrrwoooooooooyggyggyggrrryyyyyywwwwwwggg")

    def test109_rotateBackCounterclockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("b")
        self.assertEquals(test.get(), "bbbbbbbbbrryrryrryooooooooowggwggwgggggyyyyyywwwwwwrrr")

    def test110_rotateLeftClockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("L")
        self.assertEquals(test.get(), "ybbybbybbrrrrrrrrroowoowoowgggggggggoyyoyyoyybwwbwwbww")
    
    def test111_rotateLeftCounterclockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("l")
        self.assertEquals(test.get(), "wbbwbbwbbrrrrrrrrrooyooyooygggggggggbyybyybyyowwowwoww")

    def test112_rotateRightClockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("R")
        self.assertEquals(test.get(), "bbwbbwbbwrrrrrrrrryooyooyoogggggggggyybyybyybwwowwowwo")
    
    def test113_rotateRightCounterclockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("r")
        self.assertEquals(test.get(), "bbybbybbyrrrrrrrrrwoowoowoogggggggggyyoyyoyyowwbwwbwwb")

    def test114_rotateUpClockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("U")
        self.assertEquals(test.get(), "rrrbbbbbbooorrrrrrgggoooooobbbggggggyyyyyyyyywwwwwwwww")

    def test115_rotateUpCounterclockwise(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("u")
        self.assertEquals(test.get(), "gggbbbbbbbbbrrrrrrrrroooooooooggggggyyyyyyyyywwwwwwwww")

    def test116_rotateDefault(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("F")
        rotate1 = test.get()
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("")
        rotate2 = test.get()
        self.assertEqual(rotate1, rotate2)
    
    def test117_rotateFront(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("FfFfFf")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        
    def test118_rotateBack(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("BbBbBb")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")

    def test119_rotateLeft(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("LlLlLl")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")

    def test120_rotateRight(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("RrRrRr")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
    
    def test121_rotateUp(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("UUUuuu")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        
    def test122_rotateAll(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("BLFFRUurfflb")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
    
