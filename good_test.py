import unittest
from datetime import datetime
from good_example import get_time_of_day 

# Example of test written to test testable code good example

class Test(unittest.TestCase):

    # No setup needed

    def test(self):

        time_of_day = get_time_of_day(datetime(2019, 7, 15, 6, 00, 00))
        
        self.assertEqual("Morning", time_of_day)


if __name__ == '__main__':
    unittest.main()
