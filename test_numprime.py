Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import unittest
>>> from andela_bootcamp import numprime
    class mytestcases(unittest.TestCase):
        def test1(self):
            sol = numprime(17)
            self.assertln(sol,5)
         def test2(self)
             sol = numprime(17)
             self.assertNotEqual(sol,18)
         def test2(self)
             sol = numprime(18)
             self.assertTrue(sol,True)
         def test2(self)
             sol = numprime(**args)
             self.assertRaises(exception)
         def test2(self)
            sol = numprime(17)
            self.assertIs(sol,17)
