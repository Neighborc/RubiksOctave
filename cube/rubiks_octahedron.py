#!/usr/bin/env python

"""Class object for building the Rubiks truncated octahedron
Methods

Some inspiration: https://github.com/pglass/cube
Some Animation: https://jakevdp.github.io/blog/2012/11/26/3d-interactive-rubiks-cube-in-python/
Solving via learning: https://github.com/CVxTz/rubiks_cube

Solving this as a portfolio project and to complete as a challenge given to me by my professor. 

"""

class TruncatedOctahedron:

    def __init__(self, pattern):
        """
        Initialize with pattern of colors on octoid       
        
        
        """

        self.pattern = pattern


    def rotate(direction="L"):
        """
        Main action of octoid 
        Each face can be rotated three ways
        With 8 faces, that comes to 24 possible actions

        """
        
        pass