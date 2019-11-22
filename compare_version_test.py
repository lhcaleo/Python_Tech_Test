import unittest
import compare_version

class compare_version_test():

	def test_non_string_input(self):
		with self.assertRaises(TypeError):
			compare_version('1.2', 1.2)

	def test_non_digit_input(self):
		with self.assertRaises(ValueError):
			compare_version('1.2.3', '1.2.#')

	def test_same_len_less(self):
		self.assertEqual(compare_version('1.2.3', '1.2.4'), -1)
	def test_same_len_equal(self):
		self.assertEqual(compare_version('1.2.3', '1.2.3'), 0)
	def test_same_len_greater(self):
		self.assertEqual(compare_version('1.2.4', '1.2.3'), 1)

	def test_diff_len_less(self):
		self.assertEqual(compare_version('1.2.3.4', '1.2.4'), -1)
	def test_diff_len_equal(self):
		self.assertEqual(compare_version('1.2.3.0', '1.2.3'), 0)
	def test_diff_len_greater(self):
		self.assertEqual(compare_version('1.2.4', '1.2.3.4'), 1)		

	def test_same_len_less_wish_space(self):
		self.assertEqual(compare_version('1.2.3.4 ', '1.2.4.4 '), -1)
	def test_same_len_equal_with_space(self):
		self.assertEqual(compare_version('1.2.3.4 ', '1.2.3.4 '), 0)
	def test_same_len_greater_with_space(self):
		self.assertEqual(compare_version('1.2.4.4 ', '1.2.3.4 '), 1)
	
	def test_diff_len_less_wish_space(self):
		self.assertEqual(compare_version(' 1.2.3.4 ', '1.2.4.4 '), -1)
	def test_diff_len_equal_with_space(self):
		self.assertEqual(compare_version(' 1.2.3.4 ', '1.2.3.4 '), 0)
	def test_diff_len_greater_with_space(self):
		self.assertEqual(compare_version(' 1.2.4.4 ', '1.2.3.4 '), 1)


if __name__ == '__main__':
    unittest.main()

