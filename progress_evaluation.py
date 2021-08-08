#!/usr/bin/env python

"""Methods to evaluate progress or value of current pattern on cube.
Some issues may include rotational variation and speed.
If there are X number of possible actions per turn then looking to a depth of K results in
X^K possible end states which increases exponentially
24^1 = 24, 24^2=576, 24^3=13824, 24^4=331776 

Explore method for rapidly checking graph structure to be similar.
Eventual profiling to work. Solve slightly shuffled cubes first.

Solved cube = 
Y Y Y A A A G G G R R R
Y Y Y A A A G G G R R R
O O O B B B W W W P P P
O O O B B B W W W P P P

Graph representation
"""


def evaluate_progress(pattern):
    pass
