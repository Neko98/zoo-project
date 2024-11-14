import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_neg(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), None)

    def test_baby(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_child(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elderly(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()