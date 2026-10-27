import numpy as np

class RightTriangle:

    # lengths of the two legs
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    # hypotenuse
    def hyp(self):
        return np.sqrt(self.l1**2 + self.l2**2)

    # angle 1 in degrees
    def angle1(self):
        angle = np.arctan2(self.l2, self.l1)
        return np.degrees(angle)

    # angle 2 in degrees
    def angle2(self):
        angle = np.arctan2(self.l1, self.l2)
        return np.degrees(angle)

t = RightTriangle(1, np.sqrt(3))

print('Hypotenuse:', t.hyp())
print('Ang 1:', t.angle1())
print('Ang 2:', t.angle2())

#test...equal leg
t2 = RightTriangle(1, 1)

print('Hypotenuse:', t2.hyp())
print('Ang 1:', t2.angle1())
print('Ang 2:', t2.angle2())
