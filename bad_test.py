import unittest
import bad_example

# Bad example of test to test poorly writtern testable code

class Test(unittest.TestCase):

    # Setup: change system time to 6AM

    def test(self):

        time_of_day = bad_example.get_time_of_day()

        self.assertEqual("Morning", time_of_day)

    # Teardown: roll system time back to normal


if __name__ == '__main__':
    unittest.main()


# This is a bad test set up to test non-testable code because in order for this test to pass the test,
# we would need to change the system time in setup, and then roll back to normal in teardown
# Because I don't want to change the time of my system - this current test will fail.
# This would be expensive and may fail for other reasons (such as permissions), tests should run fast
# Not actually a unittest because while it acts like it's testing a simple function, it requires the environment to change