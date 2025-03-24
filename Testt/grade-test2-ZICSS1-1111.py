'''
1. Download your programs from Moodle.
1. Put this grading program in a folder with your programs.
2. Run this grading program.
3. Read your test results from results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f("2 3 +"),5)
        self.assertEqual(p1.f("1 2 + 3 4 + - 1 +"),-3)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(30,90),178)
        self.assertEqual(p2.f(1,5),12)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f(12),"*/*/*/*/*/*/*/*/*/*/*/*")
        self.assertEqual(p3.f(0),"")

    def test_p4(self):
        import p4
        sub_grades = {"prg":[4,4,5,5], "hist":[4,4,5], "econ":[5,4,5,5], "alg":[5,4]}
        self.assertEqual(p4.f(sub_grades),"econ")

    def test_p5(self):
        import p5
        cart = {"juice":4, "bread":2, "milk":3}
        prices = {"juice":2.99, "bread":2.19, "butter":3.09, "milk":1.29}
        self.assertEqual(p5.f(cart, prices, 21),True)
        self.assertEqual(p5.f(cart, prices, 20),False)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("za153"),True)
        self.assertEqual(p6.f("zA9999"),True)
        self.assertEqual(p6.f("G12345"),False)
        self.assertEqual(p6.f("AbC2"),False)

    def test_p7(self):
        import p7
        points1 = [[2,-2],[3,3],[4,-4]]
        points2 = [[-4,-4],[-5,5],[-6,6],[7,7]]
        self.assertEqual(p7.f(points1),4)
        self.assertEqual(p7.f(points2),2)

    def test_p8(self):
        import p8
        self.assertEqual(p8.f("2A9K"),"AK92")
        self.assertEqual(p8.f("4Q3J8"),"QJ843")

    def test_p9(self):
        import p9
        self.assertEqual(p9.f([1,1,2,2,3,3,3,3,4,4,4,5,5]),4)
        self.assertEqual(p9.f([22,22,33,33,33,33,33,33,44,44,44,44,44]),44)

    def test_p10(self):
        import p10
        computer = {"Owl","Camper","Chaser","Walker","Hunter","Breeze"}
        smartphone = {"Owl","Camper","Storm","Sleeper","Eater"}
        self.assertEqual(p10.f(computer,smartphone),9)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
