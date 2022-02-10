# Tic Tac Toe

Problem solving Agent: Minimax algorithm



### MinimaxAgent

The number of possible different games is:
* 362,880 games (9!)- playing all the moves, until board is full
* 255,168 games - stop the tree exploration when one player has won
* 26,830 games - taking symmetry into account


function min and max called: 549,946 times = nodes
terminal leaves: 255,168 = games



### Symmetry reduction

Reduction of the search space 
When 2 states are symetric?
isomorphic ?


rotation, reflection, and/or flip
symmetry group of a square.


http://logic.stanford.edu/ggp/readings/symmetry.pdf 
We propose to use a transposition table to detect those symmetric states before expanding a node. That means before we evaluate or expand a state in the game tree we check whether this state or any state that is symmetric to this one has an entry in the transposition table. If so, we just use the value stored in the transposition table without expanding the state. It is clear, that the algorithm does not use any additional memory compared to normal search. On the contrary, the transposition table may get smaller because symmetric states are not stored. However, the time for node expansion is increased by the time that it takes to compute the symmetric states and check whether some symmetric state is in the transposition table.
Therefore, it is essential to be able to compute hash values of states and symmetric states very efficiently. We use zobrist hashing [Zobrist, 1970] where each ground fluent is mapped to a randomly generated hash value and the hash value of a state is the bit-wise exclusive disjunction of the hash values of its fluents. 

https://en.wikipedia.org/wiki/Zobrist_hashing

Group theory is the mathematical study of symmetry
https://www2.math.upenn.edu/~mlazar/math170/notes07.pdf



