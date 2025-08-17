209010479
315922807
*****
Comments:

For question 7, we chose to implement our evaluation function
using the following heuristics:
- Smoothness of the board: Smoother states get a higher evaluation.
A smooth board is a board where neighboring tiles have similar values.
This strategy encourages boards that are arranged in a more monotonic
way, and with as many options for merges.
- Weighted tiles: The weight of each tile is determined by its position,
where the weight of the tile in the top-left corner is the highest and 
the strategy is to keep the highest tile in the corner. The weight
decreases as we move away from the corner.
This strategy rewards states with high value tiles in the top-left side
of the board, making it easier to merge them in the future when a new
high value tile is finally achieved by merging the lower value tiles
that are around the rest of the board.
- Score: We added the state score to our heuristic value in order to
encourage the algorithm to reach higher scores for the board, and thus
encouraging it to choose moves that lead to merges, that give a lot of 
new points and push it forward in the game.

We gave the Weighted tiles heuristic a weight of 0.5 since it reaches
high values that otherwise overshadow the rest of the scores.
To the smoothness heuristic we gave a weight of 2 to make it's value
more prominent since we believe in its strategy.