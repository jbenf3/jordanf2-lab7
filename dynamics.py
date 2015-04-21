#!/usr/bin/python

# Physics 91SI
# molecule 2015
# Lab 7

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle
import molecule

# TODO: Implement this function
def init_molecule():
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them"""

    pass


# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions of the particles attached to mol"""
    # The time iteration is performed by the following steps:
    #   1) Update velocity half step
    #   2) Update position/displacements
    #   3) Update forces w/ spring formula
    #   4) Update accelerations
    #   5) Update velocity
    # Implement these below
    pass


#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(1, 5), ylim=(1, 5)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig = plt.figure()
    line, = plt.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')

    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim,n,
            fargs=(dt, mol,line), interval=50, blit=True)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)