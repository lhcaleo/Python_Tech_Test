import unittest
from check_overlap import check

class test_check_overlap(unittest.TestCase):

	def test_point_as_input(self):
		self.assertFalse(check(1, 1, 2, 3))
	def test_non_int_input(self):
		with self.assertRaises(TypeError):
			check(1.1, 3, 2, 4)

	# Positive
	def test_x1_less_x2_x3_less_x4_overlap_pos(self):
		self.assertTrue(check(1, 3, 2, 4))
	def test_x1_less_x2_x3_less_x4_no_overlap_pos(self):
		self.assertFalse(check(1, 2, 3, 4))	

	def test_x1_greater_x2_x3_less_x4_overlap_pos(self):
		self.assertTrue(check(3, 1, 2, 4))
	def test_x1_greater_x2_x3_less_x4_no_overlap_pos(self):
		self.assertFalse(check(2, 1, 3, 4))

	def test_x1_less_x2_x3_greater_x4_overlap_pos(self):
		self.assertTrue(check(1, 3, 4, 2))
	def test_x1_less_x2_x3_greater_x4_no_overlap_pos(self):
		self.assertFalse(check(1, 2, 4, 3))	

	def test_x1_greater_x2_x3_greater_x4_overlap_pos(self):
		self.assertTrue(check(3, 1, 4, 2))
	def test_x1_greater_x2_x3_greater_x4_no_overlap_pos(self):
		self.assertFalse(check(2, 1, 4, 3))	

	# Negative
	def test_x1_less_x2_x3_less_x4_overlap_neg(self):
		self.assertTrue(check(-3, -1, -4, -2))
	def test_x1_less_x2_x3_less_x4_no_overlap_neg(self):
		self.assertFalse(check(-2, -1, -4, -3))	

	def test_x1_greater_x2_x3_less_x4_overlap_neg(self):
		self.assertTrue(check(-1, -3, -4, -2))
	def test_x1_greater_x2_x3_less_x4_no_overlap_neg(self):
		self.assertFalse(check(-1, -2, -4, -3))

	def test_x1_less_x2_x3_greater_x4_overlap_neg(self):
		self.assertTrue(check(-3, -1, -2, -4))
	def test_x1_less_x2_x3_greater_x4_no_overlap_neg(self):
		self.assertFalse(check(-2, -1, -3, -4))	

	def test_x1_greater_x2_x3_greater_x4_overlap_neg(self):
		self.assertTrue(check(-1, -3, -2, -4))
	def test_x1_greater_x2_x3_greater_x4_no_overlap_neg(self):
		self.assertFalse(check(-1, -2, -3, -44))	




if __name__ == '__main__':
    unittest.main(verbosity=2)