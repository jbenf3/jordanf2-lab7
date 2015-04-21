# Physics 91SI
# Spring 2015
# Lab 7

import numpy as np

class Particle:
    """This is a particle class. You will use this to simulate a spring system"""
    def __init__(self,Position,M):
        """ Initialize the particle with its 2D position (should be a 2x1 numpy array) and mass """
        self.pos = Position   # Sets x position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,1))
        self.acc = np.zeros((2,1))
