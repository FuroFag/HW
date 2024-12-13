from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
    
class RunnerTest(TestCase):
    def test_walk(self):
        cls_obj = Runner('George Droyd')
        for i in range(10):
            cls_obj.walk()
        self.assertEqual(cls_obj.distance, 50)

    def test_run(self):
        runner = Runner('George Droyd')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    
    def testchallenge(self):
        walker1 = Runner('fent_reactor')
        runner1 = Runner('Hyperborean George Droyd')
        for i in range(10):
            walker1.walk()
            runner1.run()
        self.assertNotEqual(walker1.distance, runner1.distance)
