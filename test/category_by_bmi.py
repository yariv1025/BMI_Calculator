import unittest
from src.bmi_calculator import category_by_bmi


class TestCategoryByBMI(unittest.TestCase):
    def test_type_BMI(self):
        stub_char = 'a'
        stub_none = None

        expected = "bmi_value is not numeric."

        result1 = category_by_bmi(stub_char)
        result2 = category_by_bmi(stub_none)

        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)



    def test_Negative_BMI(self):
        stub = -1

        expected = "bmi_value must be positive."

        result = category_by_bmi(stub)

        self.assertEqual(result, expected)

    def test_NotNormal_BMI(self):
        stub1 = 60
        expctednot = "Normal"
        result1 = category_by_bmi(stub1)

        self.assertNotEqual(result1, expctednot)

    def test_Obese_BMI(self):
        stub1 = 31.5
        stub2 = 37
        stub3 = 41
        stub4 = 49.5
        stub5 = 55
        stub6 = 70

        expected1 = "Moderately obese"
        expected2 = "Severely obese"
        expected3 = "Very severely obese"
        expected4 = "Morbidly obese"
        expected5 = "Super obese"
        expected6 = "Hyper obese"

        result1 = category_by_bmi(stub1)
        result2 = category_by_bmi(stub2)
        result3 = category_by_bmi(stub3)
        result4 = category_by_bmi(stub4)
        result5 = category_by_bmi(stub5)
        result6 = category_by_bmi(stub6)

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
        self.assertEqual(result6, expected6)

    def test_Underweight_BMI(self):
        # stub
        stub = 18

        # assume
        expected = "Underweight"

        # action
        result = category_by_bmi(stub)

        # expect / assert
        self.assertEqual(result, expected)

    def test_Normal_BMI(self):
        stub1 = 21.5
        stub2 = 25

        expected1 = "Normal"

        result =  category_by_bmi(stub1)

        self.assertEqual(result, expected1)

if __name__ == '__main__':
    unittest.main()