import unittest

def classify_triangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If side1**2 + side2**2 = side3**2, then return 'Right'
        
    """
    leg1 = min(a, b, c)
    hyp = max(a, b, c)
    leg2 = a + b + c - leg1 - hyp
    
    if leg1 + leg2 - hyp < 0 or leg1 <= 0:
        return 'NotATriangle'
    if hyp**2 == leg1**2 + leg2**2:
        return 'Right'
    if leg1 == hyp:
        return 'Equilateral'
    if leg1 == leg2 or leg2 == hyp:
        return 'Isoceles'
    else:
        return 'Scalene'

class TestTriangles(unittest.TestCase):

    def test_NotATriangle(self): 
        self.assertEqual(classify_triangle(0,5,8),'NotATriangle', '0 is not a valid length for a triangle')
        self.assertEqual(classify_triangle(4,-2,3),'NotATriangle', '-2 is not a valid length for a triangle')
        self.assertEqual(classify_triangle(10,2,1),'NotATriangle', '10, 2, 1 cannot form a triangle')

    def test_Right(self):
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5,13,12),'Right','5,13,12 is a Right triangle')
        self.assertEqual(classify_triangle(113,112,15),'Right','113,112,15 is a Right triangle')

    def test_Equilateral(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(5,5,5),'Equilateral','5,5,5 should be equilateral')
        self.assertEqual(classify_triangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    def test_Isoceles(self):
        self.assertEqual(classify_triangle(3,3,2),'Isoceles','3,3,2 should be isoceles')
        self.assertEqual(classify_triangle(5,4,5),'Isoceles','5,4,5 should be isoceles')
        self.assertEqual(classify_triangle(8,6,6),'Isoceles','8,6,6 should be isoceles')
    
    def test_Scalene(self): 
        self.assertEqual(classify_triangle(10,25,30),'Scalene','10,25,30 should be scalene')
        self.assertEqual(classify_triangle(2,4,3),'Scalene','2,4,3 should be scalene')
        self.assertEqual(classify_triangle(80,70,60),'Scalene','80,70,60 should be scalene')
        

if __name__ == '__main__':  
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
