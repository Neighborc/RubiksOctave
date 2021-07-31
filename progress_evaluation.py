#!/usr/bin/env python

"""Methods to evaluate progress or value of current pattern on cube.
Some issues may include rotational variation and speed.
If there are X number of possible actions per turn then looking to a depth of K results in
X^K possible end states which increases exponentially
11^1 = 11, 11^2= 121, 11^3=1331, 11^4=14641
    
"""
