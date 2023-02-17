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
    
    def test103_notNull(self):
        with self.assertRaises(ValueError):
            Cube(None)
