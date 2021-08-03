#!/usr/bin/env python

"""Methods to evaluate progress or value of current pattern on cube.
Some issues may include rotational variation and speed.
If there are X number of possible actions per turn then looking to a depth of K results in
X^K possible end states which increases exponentially
24^1 = 24, 24^2=576, 24^3=13824, 24^4=331776    
"""
