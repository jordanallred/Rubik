'''
Created on Feb 17, 2023

@author: jra0027
'''
import unittest
from rubik.model.cube import Cube


class Test(unittest.TestCase):


    def test100_validColorQuantity(self):
        self.assertRaises(ValueError, Cube.cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwwx"))
        