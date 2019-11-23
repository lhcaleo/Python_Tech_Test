import unittest
from compare_version import compare

class Test_compare_version(unittest.TestCase):

	def test_non_string_input(self):
		with self.assertRaises(TypeError):
			compare('1.2', 1.2)
	def test_non_digit_input(self):
		with self.assertRaises(ValueError):
			compare('1.2.3', '1.2.#')

	def test_same_len_less(self):
		self.assertEqual(compare('1.2.3', '1.2.4'), -1)
	def test_same_len_equal(self):
		self.assertEqual(compare('1.2.3', '1.2.3'), 0)
	def test_same_len_greater(self):
		self.assertEqual(compare('1.2.4', '1.2.3'), 1)

	def test_diff_len_less(self):
		self.assertEqual(compare('1.2.3.4', '1.2.4'), -1)
	def test_diff_len_equal(self):
		self.assertEqual(compare('1.2.3.0', '1.2.3'), 0)
	def test_diff_len_greater(self):
		self.assertEqual(compare('1.2.4', '1.2.3.4'), 1)		

	def test_same_len_less_wish_space(self):
		self.assertEqual(compare('1.2.3.4 ', '1.2.4.4 '), -1)
	def test_same_len_equal_with_space(self):
		self.assertEqual(compare('1.2.3.4 ', '1.2.3.4 '), 0)
	def test_same_len_greater_with_space(self):
		self.assertEqual(compare('1.2.4.4 ', '1.2.3.4 '), 1)
	
	def test_diff_len_less_wish_space(self):
		self.assertEqual(compare(' 1.2.3.4 ', '1.2.4.4 '), -1)
	def test_diff_len_equal_with_space(self):
		self.assertEqual(compare(' 1.2.3.4 ', '1.2.3.4 '), 0)
	def test_diff_len_greater_with_space(self):
		self.assertEqual(compare(' 1.2.4.4 ', '1.2.3.4 '), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

