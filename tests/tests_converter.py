import unittest
from number_to_french import NumberToFrench

class TestNumberToFrench(unittest.TestCase):
    def test_single_number(self):
        converter = NumberToFrench(123)
        self.assertEqual(str(converter), "cent vingt-trois")

    def test_large_number(self):
        converter = NumberToFrench(123456789)
        self.assertEqual(str(converter), "cent vingt-trois million quatre cent cinquante-six mille sept cent quatre-vingt-neuf")

    def test_list_of_numbers(self):
        converter = NumberToFrench()
        result = converter.convert_list_to_french([123, 456, 789])
        expected = ["cent vingt-trois", "quatre cent cinquante-six", "sept cent quatre-vingt-neuf"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
