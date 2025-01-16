from unittest import TestCase
import unittest
import Unittest_stuff

SEARCH_NAME = 'Ник'
class TournamentTest(TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        all_results = {}
        cls.all_results = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Unittest_stuff.Runner('Усэйн', 10)
        self.runner2 = Unittest_stuff.Runner('Андрей', 9)
        self.runner3 = Unittest_stuff.Runner(SEARCH_NAME, 3)
    
    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print('{}:'.format(i))
            for a, b in j.items():
                print('{}:{}'.format(a, b))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        tour = Unittest_stuff.Tournament(90, self.runner1, self.runner3)
        result = tour.start()
        TournamentTest.all_results['test1'] = result
        self.assertTrue(result[result.keys()[-1]] == SEARCH_NAME)
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        tour = Unittest_stuff.Tournament(90, self.runner2, self.runner3)
        result = tour.start()
        TournamentTest.all_results['test2'] = result
        self.assertTrue(result[result.keys()[-1]] == SEARCH_NAME)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        tour = Unittest_stuff.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tour.start()
        TournamentTest.all_results['test3'] = result
        self.assertTrue(result[result.keys()[-1]] == SEARCH_NAME)