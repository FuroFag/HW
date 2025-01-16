import Unittest_stuff
import Lesson12_1
import Lesson12_2
import unittest

test1 = unittest.TestSuite()

test1.addTest(unittest.TestLoader().loadTestsFromTestCase(Lesson12_1.RunnerTest))
test1.addTest(unittest.TestLoader().loadTestsFromTestCase(Lesson12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test1)
