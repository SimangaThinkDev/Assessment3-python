import unittest
from assessment import (
    generate_fibonacci_sequence,
    is_palindrome_advanced,
    find_elements_in_matrix_greater_than_value,
    format_names_list,
    sum_diagonals_square_matrix
)

class TestAssessmentModule2Functions(unittest.TestCase):

    def test_generate_fibonacci_sequence(self):
        self.assertEqual(generate_fibonacci_sequence(0), [])
        self.assertEqual(generate_fibonacci_sequence(-5), [])
        self.assertEqual(generate_fibonacci_sequence(1), [0])
        self.assertEqual(generate_fibonacci_sequence(2), [0, 1])
        self.assertEqual(generate_fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_is_palindrome_advanced(self):
        self.assertTrue(is_palindrome_advanced("madam"))
        self.assertTrue(is_palindrome_advanced("Race car!"))
        self.assertTrue(is_palindrome_advanced("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome_advanced("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome_advanced("No 'x' in Nixon"))
        self.assertFalse(is_palindrome_advanced("hello"))
        self.assertFalse(is_palindrome_advanced("Python"))
        self.assertTrue(is_palindrome_advanced("")) # Empty string is often considered a palindrome
        self.assertTrue(is_palindrome_advanced("a")) # Single character

    def test_find_elements_in_matrix_greater_than_value(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix1, 5), [6, 7, 8, 9])
        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix1, 9), [])
        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix1, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9])

        matrix2 = [[10]]
        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix2, 5), [10])
        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix2, 10), [])

        matrix3 = [] # Empty matrix
        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix3, 5), [])

        matrix4 = [[-1, -5], [0, -2]]
        self.assertCountEqual(find_elements_in_matrix_greater_than_value(matrix4, -1), [0])

    def test_format_names_list(self):
        names1 = ["Ada Lovelace", "Charles Babbage", "Grace Hopper"]
        expected1 = [
            {'first_name': 'Ada', 'last_name': 'Lovelace'},
            {'first_name': 'Charles', 'last_name': 'Babbage'},
            {'first_name': 'Grace', 'last_name': 'Hopper'}
        ]
        self.assertEqual(format_names_list(names1), expected1)

        names2 = ["SingleName"] # Single name without space
        self.assertEqual(format_names_list(names2), [{'first_name': 'SingleName', 'last_name': ''}])
        self.assertEqual(format_names_list(["Alan Turing"]), [{'first_name': 'Alan', 'last_name': 'Turing'}])
        self.assertEqual(format_names_list([]), [])


    def test_sum_diagonals_square_matrix(self):
        # Square matrices
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        # Main diagonal: 1+5+9=15. Anti-diagonal: 3+5+7=15. Center 5 counted once. Sum = 1+5+9+3+7 = 25.
        self.assertEqual(sum_diagonals_square_matrix(matrix1), 25)

        matrix2 = [[1, 2],
                   [3, 4]]
        # Main: 1+4=5. Anti: 2+3=5. No overlap. Sum = 1+4+2+3 = 10.
        self.assertEqual(sum_diagonals_square_matrix(matrix2), 10)

        matrix3 = [[10]] # 1x1 matrix
        # Main: 10. Anti: 10. Center 10. Sum = 10.
        self.assertEqual(sum_diagonals_square_matrix(matrix3), 10)

        matrix4 = [[1,  2,  3,  4],
                   [5,  6,  7,  8],
                   [9, 10, 11, 12],
                   [13,14, 15, 16]]
        # Main: 1+6+11+16 = 34. Anti: 4+7+10+13 = 34. No overlap. Sum = 34+34 = 68.
        self.assertEqual(sum_diagonals_square_matrix(matrix4), 68)

        # Non-square or invalid matrices
        self.assertEqual(sum_diagonals_square_matrix([]), 0) # Empty matrix

        non_square1 = [[1, 2, 3], [4, 5, 6]] # Rectangular
        self.assertEqual(sum_diagonals_square_matrix(non_square1), 0)

        non_square2 = [[1, 2], [3, 4, 5]]
        self.assertEqual(sum_diagonals_square_matrix(non_square2), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)