import unittest
from challenge2a import compute_row_checksum

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

if __name__ == "__main__":
    unittest.main()
