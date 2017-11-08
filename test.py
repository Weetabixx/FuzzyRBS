import unittest
from FuzzySet import FuzzyDimension
from FuzzySet import FuzzySet
from Inference import Rule

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_fuzzysets(self):
        dimension = FuzzyDimension("driving")
        dimension.add_membership("bad", (0, 30, 0, 20))
        notbadmembership = dimension.membership("bad", 60)
        self.assertEqual(notbadmembership, 0)
        badmembership = dimension.membership("bad", 10)
        self.assertEqual(badmembership, 1)
        kindabadmembership = dimension.membership("bad", 40)
        self.assertEqual(kindabadmembership, 0.5)
    def test_rules(self):
        rule = Rule("Rule 4 If the driving is bad then the tip will be small")
        concequence = rule.fire({"driving": {"bad": 1}})
        self.assertEqual(concequence, ("tip", "small", 1))
        concequence = rule.fire({"driving": {"bad": 0.2}})
        self.assertEqual(concequence, ("tip", "small", 0.2))
    def test_defuzzify(self):
        dimension = FuzzyDimension("driving")
        dimension.add_membership("good", (80, 100, 20, 0))
        mom = dimension.meanofmax("good")
        self.assertEqual(mom, 90)


if __name__ == '__main__':
    unittest.main()
