import unittest
from challenge2 import compute_row_checksum, compute_row_evendivision

spreadheet = [[5,1,9,5],[7,5,3,0],[2,4,6,8]]


class CalculateRowCheckSum(unittest.TestCase):

    def test_checksum_row(self):
        row1 = [5,1,9,5]
        row1_checksum = compute_row_checksum(row1)
        self.assertEqual(row1_checksum, 8, "checksum of row 1")
        row2 = [0,1,3,4]
        row2_checksum = compute_row_checksum(row2)
        self.assertEqual(row2_checksum, 4, "checksum of row 2")
        row3 = [4,5,6,7]
        row3_checksum = compute_row_checksum(row3)
        self.assertEqual(row3_checksum, 3, "checksum of row 3")

    def test_evendivision_row(self):
        row1 = [5,9,2,8]
        row1_evendivision = compute_row_evendivision(row1)
        self.assertEqual(row1_evendivision, 4, "first test case")
        row2 = [9,4,7,3]
        row2_evendivision = compute_row_evendivision(row2)
        self.assertEqual(row2_evendivision, 3, "second test case")
        row3 = [3,8,6,5]
        row3_evendivision = compute_row_evendivision(row3)
        self.assertEqual(row3_evendivision, 2, "third test case")


if __name__ == "__main__":
    unittest.main()
