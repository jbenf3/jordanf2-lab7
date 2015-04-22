# Physics 91SI
# Spring 2015
# Lab 7

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets x position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))

class Molecule:
    
    def __init__(self, pos1, pos2, m1, m2, k, L_0):
        self.p1 = Particle(pos1, m1)
        self.p2 = Particle(pos2, m2)
        self.m1 = m1
        self.m2 = m2
        self.k = k
        self.L_0 = L_0

    def get_displ(self):
        return self.p2.pos - self.p1.pos

    def get_force(self):
        return -self.k*(self.L_0 - self.get_displ())


mol = Molecule(5,3,4,1,0.4, 1)
print mol.get_force()
