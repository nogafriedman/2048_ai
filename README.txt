Introduction to Artificial Intelligence - Project 2: Multi-Agent Search in 2048

This project, part of the Introduction to Artificial Intelligence course, focuses on designing intelligent agents for the game 2048. The assignment explores multi-agent search techniques, including minimax, alpha-beta pruning, and expectimax, as well as the design of effective evaluation functions.
The primary goals of this project are:
Implementing and comparing adversarial search algorithms
Understanding the impact of randomness in decision-making
Designing evaluation functions to improve agent performance

Key files:
multi_agents.py – Implementations of ReflexAgent, MinimaxAgent, AlphaBetaAgent, and ExpectimaxAgent.
2048.py – Main driver for running the 2048 game with different agents.
game_state.py – Defines the GameState class for 2048.
game.py – Core game logic, including Agent and Action definitions.
util.py – Supporting data structures.
Graphics and support files (not modified):
graphics_display.py, game_grid.py, game2048_grid.py, displays.py, keyboard_agents.py.

How to run:
Play 2048 manually:
python3 2048.py

Run ReflexAgent:
python3 2048.py --agent=ReflexAgent
python3 2048.py --agent=ReflexAgent --num_of_games=10 --display=SummaryDisplay

Run MinimaxAgent:
python3 2048.py --agent=MinmaxAgent --depth=1 --random_seed=1 --initial_board=test_layout.txt
python3 2048.py --agent=MinmaxAgent --depth=2

Run AlphaBetaAgent:
python3 2048.py --agent=AlphaBetaAgent --depth=2
python3 2048.py --agent=AlphaBetaAgent --depth=2 --num_of_games=10 --display=SummaryDisplay

Run ExpectimaxAgent:
python3 2048.py --agent=ExpectimaxAgent --depth=2
python3 2048.py --agent=ExpectimaxAgent --depth=2 --num_of_games=10 --display=SummaryDisplay

Run with custom evaluation function:
python3 2048.py --agent=AlphaBetaAgent --depth=2 --evaluation_function=better --num_of_games=5

Evaluation Function Design:
The betterEvaluationFunction was designed to capture key properties of successful 2048 play using a linear combination of features:
Maximum tile value – encourages building toward 2048 and higher.
Monotonicity – rewards boards where values consistently increase along rows/columns, which supports stable merging.
Smoothness – penalizes large differences between adjacent tiles, discouraging fragmented boards.
Empty cells – rewards open spaces, since they allow flexibility and reduce the risk of losing.
Board position weighting – prioritizes placing larger tiles in stable corners.
Weights were chosen empirically to balance survival (empty cells, smoothness) and progress toward high tiles (max tile, monotonicity).
When tested with AlphaBetaAgent at depth 2, this evaluation function consistently produced scores above 7000 and often reached tiles 1024 or higher.

Results & Observations:
ReflexAgent: Performs poorly; usually achieves 256, occasionally 512.
MinimaxAgent: Plays optimally against worst-case board responses, but performance degrades due to high branching factor. Depth 2 search is feasible; depth 3 is too slow.
AlphaBetaAgent: Produces the same minimax values as MinimaxAgent but runs faster due to pruning. Typically reaches 512, sometimes 1024 with more depth.
ExpectimaxAgent: Models randomness more effectively; less pessimistic than minimax. In practice, it outperforms AlphaBetaAgent, often achieving 1024 about half the time.
Better Evaluation Function: With Expectimax or AlphaBeta at depth 2, this heuristic significantly boosts performance, achieving average scores over 7000 and reaching 2048 in many runs.
These results highlight the importance of both search strategy and evaluation design. While pruning improves efficiency, realistic modeling of randomness (Expectimax) combined with a strong evaluation function delivers the best overall performance.
