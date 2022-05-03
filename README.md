# Strawberry 🍓

Where classicaly bits meet quantum bits.

A simple simulation and combination with Schöning's algorithm and Grover's algorithm. 

# SAT Problems 

A solution to a SAT problem is a string of bits, which makes it easy to map a quantum Circuit. The probkem itself is essentially a bunch of conditions (clauses) that rule out different combinations of bit values.

For example) if we had three bits, one of the clauses might be `zeroth ON, and first bit OFF`. This would rule out combinations like `101` and `001` as valid solutions.

To use such a circuit with Grover's Algorithm, we implement an oracle to change the phase of the output state by 180 degrees if the state is a solution. If it's not a solution, we change it, until it becomes a solution with Schoning's Algorithm.

# Schoning's Algorithm