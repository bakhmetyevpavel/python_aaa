from one_hot_encoder import fit_transform
import unittest
import time
from datetime import datetime


class Test_fit_transform(unittest.TestCase):
    """
    Class for testing fit_transform func
    """

    @classmethod
    def setUpClass(cls):
        cls.contextfile = open("context_check.txt", "w+")
        cls.contextfile.truncate(0)
        cls.contextfile.write(f"NEW TEST {datetime.now()}:\n")
        cls.contextfile.close()

    def setUp(self):
        self.contextfile = open("context_check.txt", "a+")
        self.start = time.time()

    def tearDown(self):
        self.stop = time.time()
        self.contextfile.write(f"test duration = {self.stop - self.start} sec\n")
        self.contextfile.close()

    def test_list_input(self):
        """
        List[str] input test
        """
        result = fit_transform(["Moscow", "New York", "Moscow", "London"])
        expected = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]

        self.assertEqual(result, expected)

    def test_strings_input(self):
        """
        Strings input test
        """
        result = fit_transform("Moscow", "New York", "Moscow", "London")
        expected = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]

        self.assertEqual(result, expected)

    def test_true_case(self):
        """
        Test for using assertTrue case
        """

        self.assertTrue(
            all(
                [
                    isinstance(item, int)
                    for row in fit_transform("Moscow", "New York", "Moscow", "London")
                    for item in row[1]
                ]
            )
        )

    def test_empty_input(self):
        """
        Empty input test
        """
        with self.assertRaises(TypeError):
            fit_transform()

    def test_not_in_case(self):
        """
        NotIn case test
        """
        result = fit_transform(["Moscow", "New York", "Moscow", "London"])

        self.assertNotIn(("Moscow", [1, 1, 1]), result)
