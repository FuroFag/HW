import unittest
from unittest import TestCase
import logging

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            cls_obj = Runner('George Droyd')
            for i in range(10):
                cls_obj.walk()
            self.assertEqual(cls_obj.distance, 50)
            logging.info(f'Succes')
        except:
            logging.error(f'Speed must be bigger than 0')
            return 0

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('George Droyd')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testchallenge(self):
        walker1 = Runner('fent_reactor')
        runner1 = Runner('Hyperborean George Droyd')
        for i in range(10):
            walker1.walk()
            runner1.run()
        self.assertNotEqual(walker1.distance, runner1.distance)
