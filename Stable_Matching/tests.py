import unittest
from Stable_Matching import *

class TestMatchClass(unittest.TestCase):

    def testCreateMatchObject(self):
        johnDoe = Match("John Doe")

    def testStrAndRepr(self):
        janeDoe = Match("Jane Doe")
        str(janeDoe)
        repr(janeDoe)

    def testSetPreferences(self):
        johnDoe = Match("John Doe")
        janeDoe = Match("Jane Doe")
        adamSmith = Match("Adam Smith")
        adamSmith.preferences = [janeDoe, johnDoe]
        # Check if preferences set
        self.assertEqual(adamSmith.preferences, [janeDoe, johnDoe])

    def testSetPreferencesInvalid(self):
        adamSmith = Match("Adam Smith")
        with self.assertRaises(TypeError):
            adamSmith.preferences = ["John Doe", "Jane Doe"]


if __name__ == "__main__":
    unittest.main()
