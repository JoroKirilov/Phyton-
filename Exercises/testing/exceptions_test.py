import unittest


class Worker:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def rest(self):
        self.energy += 1

    def work(self):
        if self.energy < 1:
            raise Exception("NOT ENOUGH ENERGY")



class TestWorkerClass(unittest.TestCase):
    def test_if_worker_not_energy_raise_exception(self):
        worker1 = Worker("John", 0)
        with self.assertRaises(Exception) as ex:   # when know that we have exception, find if the exception raise
            worker1.work()
        self.assertEqual("NOT ENOUGH ENERGY", str(ex.exception)) # and check exception msg