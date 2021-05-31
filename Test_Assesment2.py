import unittest
from unittest import result
import Assesment2 

class TestAssesment(unittest.TestCase):

    def setUp(self):
        self.student_count=4
        self.teachers_count=2

    def test_total_count(self):
        result=sum(self.student_count,self.teachers_count)
        self.assertEqual(result,6)

    def test_get_attenance_detail(self):
        result=Assesment2.get_attenance_detail(int)
        self.assertEqual(result,int)

    def test_get_account_details(self):
        result=Assesment2.get_account_details(int)
        self.assertTrue(result,int)

if __name__ == '__main__':
    unittest.main()
