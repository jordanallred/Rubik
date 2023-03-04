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
            Cube("rbbbbbbbbrrrrbrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
    
    def test105_validDirections(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        with self.assertRaises(ValueError):
            test.rotate('Dd')
        test.rotate('')
        test.rotate('FfRrBbLlUu')
    
    def test106_rotateFrontClockwise(self):
        test = Cube("LQlfffyfZfZlyylLyfyLQfZlLZQfQZZQQlZlLyflLLyLQZLQQllZyy")
        test.rotate("F")
        self.assertEquals(test.get(), "yfLffQZflyZlLylQyfyLQfZlLZQfQZZQLlZQLyflLLlQZLyfQllZyy")
        
    def test107_rotateFrontCounterclockwise(self):
        test = Cube("222222ssDDMsDjwwjswDwjwwwjjjsjMsj2sMMwMDD2Mss2wjMMMDDD")
        test.rotate("f")
        self.assertEquals(test.get(), "22D22s22sjMswjw2jswDwjwwwjjjssMss2sMMwMDD2DDwjjMMMMDDD")
    
    def test108_rotateBackClockwise(self):
        test = Cube("9o9o4ofooxRffoxR9fox9RRxxRoRfo4x999xxf44994R4R4f4fxRf4")
        test.rotate("B")
        self.assertEquals(test.get(), "9o9o4ofooxR4fofR9RxRoRRxox94fofx9x9xfxf4994R4R4f4fxR49")

    def test109_rotateBackCounterclockwise(self):
        test = Cube("3oLLLLokLk3o99Y99LkLLo33Y339L9YoYYo3kk3okkk3oY9YkYY99o")
        test.rotate("b")
        self.assertEquals(test.get(), "3oLLLLokLk3k99k993L33L33koY9L99oYoo3YY9okkk3oY9YkYYLYo")

    def test110_rotateLeftClockwise(self):
        test = Cube("xx666b666PoToTPT6bPbTooTooTb6oPxxPxxoT6PPTPPxbbbbbToxx")
        test.rotate("L")
        self.assertEquals(test.get(), "ox6P6bP66PoToTPT6bPboooboobPPbxx6xxoTT6TPTTPxxbb6bT6xx")
    
    def test111_rotateLeftCounterclockwise(self):
        test = Cube("swaBBsaBswwXXwBX8BaXwsX88awXX8sswXwB8as888BXBsa8aaBasw")
        test.rotate("l")
        self.assertEquals(test.get(), "swaaBsaBswwXXwBX8BaXBsX88a88wBXswXsXsasB88aXBwa88aBwsw")

    def test112_rotateRightClockwise(self):
        test = Cube("mmVUgtKggtVUKVVmVVVUUtKgKKtgmUUmVmmtmmggtgKKgVtttUKKUU")
        test.rotate("R")
        self.assertEquals(test.get(), "mmtUgKKgUmKtVVVVVUgUUgKggKtgmUUmVmmtmmVgttKKgVtKtUtKUV")
    
    def test113_rotateRightCounterclockwise(self):
        test = Cube("3Rw7w3373R7703w03w0hhR700w7RwRwhR00R70hhRh7hhw3w70R33h")
        test.rotate("r")
        self.assertEquals(test.get(), "3Rh7wh37h7ww733R00hhhR70ww7RwRwhR00R700hRR7h0w3w703333")

    def test114_rotateUpClockwise(self):
        test = Cube("S8zbGQSz8SQzz8bbQ8QSSSSGGGGbQ8bQ8bz8Q8GSzGzGQb8GSbbQzz")
        test.rotate("U")
        self.assertEquals(test.get(), "SQzbGQSz8QSSz8bbQ8bQ8SSGGGGS8zbQ8bz8zSQGz8QGGb8GSbbQzz")

    def test115_rotateUpCounterclockwise(self):
        test = Cube("nvnMoooPMvnMnnWoMMWWWMWvPPnMWPMMPovvPvvPPWWnWnnvovoPoo")
        test.rotate("u")
        self.assertEquals(test.get(), "MWPMoooPMnvnnnWoMMvnMMWvPPnWWWMMPovvvWWvPnPPWnnvovoPoo")

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
        test.rotate("LLLlll")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")

    def test120_rotateRight(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("RRRrrr")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
    
    def test121_rotateUp(self):
        test = Cube("bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        test.rotate("UUUuuu")
        self.assertEquals(test.get(), "bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww")
        