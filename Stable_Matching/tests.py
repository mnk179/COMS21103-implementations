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

class TestStableMatching(unittest.TestCase):

    def testEmployersPreference(self):
        # Initialise employers
        veolia = Match("Veolia")
        weibo = Match("Weibo")
        xerox = Match("Xerox")
        yahoo = Match("Yahoo")
        zurich = Match("Zurich")

        employers = [veolia, weibo, xerox, yahoo, zurich]

        # Initialise students
        abby = Match("Abby")
        ben = Match("Ben")
        callum = Match("Callum")
        davida = Match("Davida")
        erika = Match("Erika")

        students = [abby, ben, callum, davida, erika]

        # Set employers' preference lists
        veolia.preferences = [ben, abby, davida, erika, callum]
        weibo.preferences = [davida, ben, abby, callum, erika]
        xerox.preferences = [ben, erika, callum, davida, abby]
        yahoo.preferences = [abby, davida, callum, ben, erika]
        zurich.preferences = [ben, davida, abby, erika, callum]

        # Set students' preference lists
        abby.preferences = [zurich, veolia, weibo, yahoo, xerox]
        ben.preferences = [xerox, weibo, yahoo, veolia, zurich]
        callum.preferences = [weibo, xerox, yahoo, zurich, veolia]
        davida.preferences = [veolia, zurich, yahoo, xerox, weibo]
        erika.preferences = [yahoo, weibo, zurich, xerox, veolia]

        stableMatching(employers, students)

        employersResult = [emp.pair for emp in employers]
        employersTestAgainst = [abby, callum, ben, erika, davida]

        self.assertEqual(employersResult, employersTestAgainst)

        studentsResult = [stu.pair for stu in students]
        studentsTestAgainst = [veolia, xerox, weibo, zurich, yahoo]

        self.assertEqual(studentsResult, studentsTestAgainst)

    def testProposorsAcceptors(self):
        # https://en.wikipedia.org/wiki/Stable_marriage_problem#/media/File:Gale-Shapley.gif

        # Initialise proposors
        p = [Match(1), Match(2), Match(3), Match(4)]

        # Initialise acceptors
        a = [Match(1), Match(2), Match(3), Match(4)]

        # Set proposors' preferences
        p[0].preferences = [a[1], a[0], a[2], a[3]]
        p[1].preferences = [a[3], a[0], a[1], a[2]]
        p[2].preferences = [a[0], a[2], a[1], a[3]]
        p[3].preferences = [a[1], a[2], a[0], a[3]]

        # Set acceptors' preferences
        a[0].preferences = [p[0], p[2], p[1], p[3]]
        a[1].preferences = [p[2], p[3], p[0], p[1]]
        a[2].preferences = [p[3], p[1], p[2], p[0]]
        a[3].preferences = [p[2], p[1], p[0], p[3]]

        stableMatching(p, a)

        proposorsResult = [el.pair for el in p]
        proposorsTestAgainst = [a[0], a[3], a[2], a[1]]

        self.assertEqual(proposorsResult, proposorsTestAgainst)

        acceptorsResult = [el.pair for el in a]
        acceptorsTestAgainst = [p[0], p[3], p[2], p[1]]

        self.assertEqual(acceptorsResult, acceptorsTestAgainst)

if __name__ == "__main__":
    unittest.main()
