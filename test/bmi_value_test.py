import unittest
from src.bmi_calculator import bmi_calc


class BMICalculatorTest(unittest.TestCase):

    def test_calculation(self):
        # stub
        stub_body_mass1 = 30
        stub_body_height1 = 1.65

        stub_body_mass2 = 60
        stub_body_height2 = 1.50

        stub_body_mass3 = 100
        stub_body_height3 = 1.70

        # assume
        expected1 = 11.019283746556475
        expected2 = 26.666666666666668
        expected3 = 34.602076124567475

        # action
        result1 = bmi_calc(stub_body_mass1, stub_body_height1)
        result2 = bmi_calc(stub_body_mass2, stub_body_height2)
        result3 = bmi_calc(stub_body_mass3, stub_body_height3)

        # expect / assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

    def test_division_By_Zero(self):
        # stub
        stub_body_mass1 = 30
        stub_body_height1 = 0

        # assume
        expected = "Wrong value's: Please insert positive numbers. Weight in kg and Height in meters!"

        # action
        result1 = bmi_calc(stub_body_mass1, stub_body_height1)

        # expect / assert
        self.assertEqual(result1, expected)

    def test_negative_number(self):
        # stub
        stub_body_mass1 = -30
        stub_body_height1 = 1.50

        # assume
        expected1 = "Wrong value's: Please insert positive numbers. Weight in kg and Height in meters!"

        # action
        result1 = bmi_calc(stub_body_mass1, stub_body_height1)

        # expect / assert
        self.assertEqual(result1, expected1)

    def test_only_numbers(self):
        with self.assertRaises(TypeError):
            # stub
            stub_body_mass1 = 'a'
            stub_body_height1 = 1.50

            stub_body_mass2 = 50
            stub_body_height2 = 'a'

            stub_body_mass3 = '#'
            stub_body_height3 = 'a'

            stub_body_mass4 = None
            stub_body_height4 = None

            # assume
            expected = TypeError

            # action
            result1 = bmi_calc(stub_body_mass1, stub_body_height1)
            result2 = bmi_calc(stub_body_mass2, stub_body_height2)
            result3 = bmi_calc(stub_body_mass3, stub_body_height3)
            result4 = bmi_calc(stub_body_mass4, stub_body_height4)

            # axpect / assert
            self.assertRaises(TypeError, result1)
            self.assertRaises(TypeError, result2)
            self.assertRaises(TypeError, result3)
            self.assertRaises(TypeError, result4)


if __name__ == '__main__':
    unittest.main()
