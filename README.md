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
- __BetterEvaluationFunction__ – At depth 2, this heuristic greatly boosts AlphaBeta’s performance, with average scores significantly above 7000 and frequent 2048 tiles. Expectimax also benefits, though the improvement is less pronounced.

<img src="https://github.com/user-attachments/assets/2306547f-ebe3-4954-b03a-a51a5a05efd3" alt="AlphaBeta Results" width="700" />

(AlphaBetaAgent depth=2 with BetterEvaluationFunction, n=5 summary)  

<img src="https://github.com/user-attachments/assets/a805d295-66aa-42df-9d77-33ca9e19d9c0" alt="Expectimax Results" width="700" />  

(ExpectimaxAgent depth=2 with BetterEvaluationFunction, n=5 summary)  


__Takeaways:__  
With betterEvaluationFunction at depth 2, AlphaBeta achieves about 80% win rate, often reaching 2048 and averaging well over 7000 points. Expectimax, by contrast, failed to win any of the runs, typically stalling at 1024. This shows that the synergy between pruning and a strong heuristic can outweigh probabilistic modeling at shallow depths, making AlphaBeta the stronger choice in practice.

<img src="https://github.com/user-attachments/assets/df399bd6-1e09-4faf-8c27-88279d76a151" alt="Results details" width="400" />
