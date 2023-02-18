'''
Created on Jan 20, 2023

@author: jra0027
'''
import unittest
import app


class Test(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'jra0027'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)