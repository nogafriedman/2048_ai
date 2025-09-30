# Multi-Agent Search in 2048

This project was developed as part of the Introduction to Artificial Intelligence course.
It implements intelligent agents for the game 2048, focusing on multi-agent search algorithms and the design of effective evaluation functions.

The project explores:
- Implementing and comparing adversarial search algorithms.
- Understanding the role of randomness in decision-making.
- Designing heuristics that improve agent performance in 2048.

<img src="https://github.com/user-attachments/assets/58e96880-441f-4f53-93af-2d7eed436ba2" alt="Image" width="300" />

# Key Files
```multi_agents.py``` – Implementations of ReflexAgent, MinimaxAgent, AlphaBetaAgent, and ExpectimaxAgent.  
```2048.py``` – Main driver for running the 2048 game with different agents.  
```game_state.py``` – Defines the GameState class for 2048.  
```game.py``` – Core game logic, including Agent and Action definitions.  
```util.py``` – Supporting data structures.  
__Graphics and support files__ (not modified):
```graphics_display.py```, ```game_grid.py```, ```game2048_grid.py```, ```displays.py```, ```keyboard_agents.py```.

# How to Run
__Play 2048 manually:__   
python3 2048.py

__Run ReflexAgent:__   
python3 2048.py --agent=ReflexAgent  
python3 2048.py --agent=ReflexAgent --num_of_games=10 --display=SummaryDisplay

__Run MinimaxAgent:__  
python3 2048.py --agent=MinmaxAgent --depth=1 --random_seed=1 --initial_board=test_layout.txt  
python3 2048.py --agent=MinmaxAgent --depth=2

__Run AlphaBetaAgent:__  
python3 2048.py --agent=AlphaBetaAgent --depth=2  
python3 2048.py --agent=AlphaBetaAgent --depth=2 --num_of_games=10 --display=SummaryDisplay

__Run ExpectimaxAgent:__  
python3 2048.py --agent=ExpectimaxAgent --depth=2  
python3 2048.py --agent=ExpectimaxAgent --depth=2 --num_of_games=10 --display=SummaryDisplay

__Run with custom evaluation function:__  
python3 2048.py --agent=AlphaBetaAgent --depth=2 --evaluation_function=better --num_of_games=5

# Evaluation Function Design
The betterEvaluationFunction was designed to capture the characteristics of successful 2048 play using a linear combination of features:
- __Maximum tile value__ – encourages building toward 2048 and beyond.
- __Monotonicity__ – rewards boards with values increasing along rows/columns, which supports stable merging.
- __Smoothness__ – penalizes large differences between adjacent tiles, discouraging fragmented boards.
- __Empty cells__ – rewards open spaces, allowing flexibility and reducing the risk of losing.
- __Board position weighting__ – prioritizes placing larger tiles in corners.

Weights were chosen empirically to balance survival (empty cells, smoothness) and progress toward high tiles (max tile, monotonicity).
With __AlphaBetaAgent__ (depth 2), this heuristic consistently produced scores above 7000 and frequently reached the 1024 tile or higher.

# Results and Observations

- __ReflexAgent__ – Performs poorly; typically stalls at 256, occasionally 512.
- __MinimaxAgent__ – Plays optimally against worst-case responses, but performance degrades due to high branching factor. Depth 2 search is feasible; depth 3 is too slow.
- __AlphaBetaAgent__ – Matches Minimax in strength but runs faster thanks to pruning. Typically reaches 512, sometimes 1024.
- __ExpectimaxAgent__ – Models randomness more effectively; less pessimistic than minimax. In practice, it outperforms AlphaBetaAgent, often achieving 1024 about half the time.
- __BetterEvaluationFunction__ – With Expectimax or AlphaBeta at depth 2, this heuristic significantly improves performance, achieving average scores >7000 and reaching 2048 in many runs.

<img src="https://github.com/user-attachments/assets/504ffdde-a75c-45d2-9f0f-7725c4db7738" alt="Image" width="700" />
[__BetterEvaluationFunction__ results]

__Takeaways:__  
These results highlight the importance of both search strategy and evaluation design. While pruning improves efficiency, realistic modeling of randomness (Expectimax) combined with a strong evaluation function delivers the best overall performance.
