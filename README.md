# Strawberry 🍓

Where classicaly bits meet quantum bits.

A simple simulation and combination with Schöning's algorithm and Grover's algorithm. 

# SAT Problems 

A solution to a SAT problem is a string of bits, which makes it easy to map a quantum Circuit. The probkem itself is essentially a bunch of conditions (clauses) that rule out different combinations of bit values.

For example) if we had three bits, one of the clauses might be `zeroth ON, and first bit OFF`. This would rule out combinations like `101` and `001` as valid solutions.

To use such a circuit with Grover's Algorithm, we implement an oracle to change the phase of the output state by 180 degrees if the state is a solution. If it's not a solution, we change it, until it becomes a solution with Schoning's Algorithm.

# Schoning's Algorithm

Similar to random guessing, Schoning's Algorithm chooses an input at random and checks if it works. But unlike random guessing, it doesn't throw the string away. Instead it pick up an unsatisfied clause and toggles a bit in the string to satisfy that clause.

*Note*: In Strawberry, the Schoning's algorithm will run regardless if the program finds an unsatisfied SAT clause.

Since our parameters are based on `true` and `false`, the bit toggling part essentially becomes us trying to replace either `0` or `1` as we are only dependent on a 50/50 chance of either two bits being `true` or `false` dependent on the program. This becomes our initial guess, and if that becomes close enough, it could be the correct solution, which gets sent to Grover's. 

The runtime for 3-SAT problems is `1.3334^n`, where `n` is the number of strings, which is faster than Grover's