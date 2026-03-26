import unittest
import pycalc.pycalc as calculator

class PyCalcUnitTests(unittest.TestCase):
  def test_add(self):
    left = [50,50,50,50,50,-50,-50,-50,-50,-50,0,0,0]
    right = [50,-10,-60,-50,0,60,40,50,-50,0,50,-50,0]
    expected = [100,40,-10,0,50,10,-10,0,-100,-50,50,-50,0]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.add(l, r)
        self.assertEqual(got, e)

  def test_subtract(self):
    left = [50,50,50,50,50,-50,-50,-50,-50,-50,0,0,0]
    right = [20,60,50,-50,0,60,40,-60,-50,0,50,-50,0]
    expected = [30,-10,0,100,50,-110,-10,10,0,-50,-50,50,0]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.subtract(l, r)
        self.assertEqual(got, e)
  
  def test_multiply(self):
    left = [10,10,10,-10,-10,-10,0,0,0]
    right = [5,-5,0,5,-5,0,40,-50,0]
    expected = [50,-50,0,-50,50,0,0,0,0]
    for i in range(len(left)):
      l = left[i]
      r = right[i]
      e = expected[i]
      with self.subTest(l=l, r=r, e=e):
        got = calculator.multiply(l, r)
        self.assertEqual(got, e)
  


if __name__ == '__main__':
  unittest.main()
