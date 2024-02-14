# testing lfsr
import unittest
from lfsr import LFSR

# class LFSRTest():
class TestLFSR(unittest.TestCase):

    # save our inputs used in LFSR
    numbers = [
        # ('10011010', 5), # sample
        ('0110100111', 2),
        ('0100110010', 8),
        ('1001011101', 5),
        ('0001001100', 1),
        ('1010011101', 7),
    ]

    # save correct result
    response_numbers = [
        ('1101001111', 1),
        ('1001100100', 0),
        ('0010111010', 0),
        ('0010011000', 0),
        ('0100111011', 1),
    ]
    
    # setup fresh instances before each test methods
    def setUp(self):
        # setup instances
        self.test_obj1 = LFSR(TestLFSR.numbers[0][0], TestLFSR.numbers[0][1])
        self.test_obj2 = LFSR(TestLFSR.numbers[1][0], TestLFSR.numbers[1][1])
        self.test_obj3 = LFSR(TestLFSR.numbers[2][0], TestLFSR.numbers[2][1])
        self.test_obj4 = LFSR(TestLFSR.numbers[3][0], TestLFSR.numbers[3][1])
        self.test_obj5 = LFSR(TestLFSR.numbers[4][0], TestLFSR.numbers[4][1])
        # run step() method to check
        self.test_obj1.step()
        self.test_obj2.step()
        self.test_obj3.step()
        self.test_obj4.step()
        self.test_obj5.step()

    # setup end action after each test methods
    def tearDown(self):
        pass

    # check if step results match
    def test_step(self):
        # print(self.test_obj1.__dict__)

        # each step() function creates 'new_num'
        self.assertEqual(self.test_obj1.new_num, TestLFSR.response_numbers[0][0])
        self.assertEqual(self.test_obj2.new_num, TestLFSR.response_numbers[1][0])
        self.assertEqual(self.test_obj3.new_num, TestLFSR.response_numbers[2][0])
        self.assertEqual(self.test_obj4.new_num, TestLFSR.response_numbers[3][0])
        self.assertEqual(self.test_obj5.new_num, TestLFSR.response_numbers[4][0])
        
    # test the bits(xor) in the lfsr
    def test_bit(self):
        # print(self.test_obj1.__dict__)
        
        # step method runs bit() inside of it, and saves xor result to xor_num
        self.assertEqual(self.test_obj1.xor_num, TestLFSR.response_numbers[0][1])
        self.assertEqual(self.test_obj2.xor_num, TestLFSR.response_numbers[1][1])
        self.assertEqual(self.test_obj3.xor_num, TestLFSR.response_numbers[2][1])
        self.assertEqual(self.test_obj4.xor_num, TestLFSR.response_numbers[3][1])
        self.assertEqual(self.test_obj5.xor_num, TestLFSR.response_numbers[4][1])
        

if __name__ == '__main__':
    # unittest.main() tests the lfsr module when ran
    unittest.main()
