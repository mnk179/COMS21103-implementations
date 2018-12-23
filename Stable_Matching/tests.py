import unittest
from Stable_Matching import *

class TestMatchClass(unittest.TestCase):
    def testCreateMatchObject(self):
        johnDoe = Match("John Doe")
    def testStrAndRepr(self):
        johnDoe = Match("John Doe")
        str(johnDoe)
        repr(johnDoe)

if __name__ == "__main__":
    unittest.main()
