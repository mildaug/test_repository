import unittest
from bank import Bank

class TestBank(unittest.TestCase):
    def test_calculator(self):
        bank = Bank(10000, 5, 3)
        monthly_payment, total_payment = bank.calculator()
        self.assertAlmostEqual(monthly_payment, 299.71, places=2)
        self.assertAlmostEqual(total_payment, 10789.56, places=2)

if __name__ == '__main__':
    unittest.main()






