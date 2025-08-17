import numpy as np
import abc
import util
from game import Agent, Action

AGENT = 0
OPPONENT = 1
ALPHA = float('-inf')
BETA = float('inf')


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        get_action takes a game_state and returns some Action.X for some X in the set {UP, DOWN, LEFT, RIGHT, STOP}
        """

        # Collect legal moves and successor states
        legal_moves = game_state.get_agent_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(len(scores)) if scores[index] == best_score]
        chosen_index = np.random.choice(best_indices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (GameState.py) and returns a number, where higher numbers are better.

        """

        # Useful information you can extract from a GameState (game_state.py)
        successor_game_state = current_game_state.generate_successor(action=action)
        board = successor_game_state.board
        max_tile = successor_game_state.max_tile
        score = successor_game_state.score

        legal_moves = successor_game_state.get_agent_legal_actions()
        max_score = score
        for move in legal_moves:
            second_successor = successor_game_state.generate_successor(action=move)
            possible_score = second_successor.score + count_equal_neighbors(second_successor.board)
            if possible_score > max_score:
                max_score = possible_score

        return max_score


def count_equal_neighbors(arr):
    equal_neighbors = 0

    for i in range(3):
        for j in range(3):
            if arr[i, j] == arr[i][j + 1] or arr[i, j] == arr[i + 1][j]:
                equal_neighbors += arr[i, j]
        if arr[i, 3] == arr[i + 1][3]:
            equal_neighbors += arr[i, 3]

    for i in range(3):
        if arr[3, i] == arr[3][i + 1]:
            equal_neighbors += arr[3, i]
    return equal_neighbors


def score_evaluation_function(current_game_state):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return current_game_state.score


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinmaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evaluation_function='scoreEvaluationFunction', depth=2):
        self.evaluation_function = util.lookup(evaluation_function, globals())
        self.depth = depth

    @abc.abstractmethod
    def get_action(self, game_state):
        return


class MinmaxAgent(MultiAgentSearchAgent):
    def get_action(self, game_state):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        game_state.get_legal_actions(agent_index):
            Returns a list of legal actions for an agent
            agent_index=0 means our agent, the opponent is agent_index=1

        Action.STOP:
            The stop direction, which is always legal

        game_state.generate_successor(agent_index, action):
            Returns the successor game state after an agent takes an action
        """
        """*** YOUR CODE HERE ***"""
        best_score, best_action = self.minimax(game_state, AGENT, self.depth)
        # print("for depth = " + str(self.depth) + "  the score is: " + str(best_score))
        return best_action

    def minimax(self, game_state, agent_index, depth):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state), None

        if agent_index == AGENT:
            return self.max_value(game_state, depth)

        if agent_index == OPPONENT:
            return self.min_value(game_state, depth)

    def max_value(self, game_state, depth):
        max_score = float('-inf')
        best_action = None

        for action in game_state.get_legal_actions(AGENT):
            successor = game_state.generate_successor(AGENT, action)
            value, _ = self.minimax(successor, OPPONENT, depth)
            if value > max_score:
                max_score = value
                best_action = action
        return max_score, best_action

    def min_value(self, game_state, depth):
        min_score = float('inf')

        for action in game_state.get_legal_actions(OPPONENT):
            successor = game_state.generate_successor(OPPONENT, action)
            value, _ = self.minimax(successor, AGENT, depth - 1)
            if value < min_score:
                min_score = value

        return min_score, None


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def get_action(self, game_state):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        """*** YOUR CODE HERE ***"""
        best_score, best_action = self.alpha_beta_pruning(game_state, AGENT, self.depth, ALPHA, BETA)
        # print("for depth = " + str(self.depth) + "  the score is: " + str(best_score))
        return best_action

    def alpha_beta_pruning(self, game_state, agent_index, depth, alpha, beta):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state), None

        if agent_index == AGENT:
            max_score = float('-inf')
            best_action = None

            for action in game_state.get_legal_actions(AGENT):
                successor = game_state.generate_successor(AGENT, action)
                value, _ = self.alpha_beta_pruning(successor, OPPONENT, depth, alpha, beta)
                if value > max_score:
                    max_score = value
                    best_action = action
                alpha = max(alpha, max_score)
                if beta <= alpha:
                    break  # Beta cut-off

            return max_score, best_action

        else:  # OPPONENT
            min_score = float('inf')

            for action in game_state.get_legal_actions(OPPONENT):
                successor = game_state.generate_successor(OPPONENT, action)
                value, _ = self.alpha_beta_pruning(successor, AGENT, depth - 1, alpha, beta)
                if value < min_score:
                    min_score = value
                beta = min(beta, min_score)
                if beta <= alpha:
                    break  # Alpha cut-off

            return min_score, None


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        max_score, best_action = self.expectimax(game_state, self.depth, AGENT)
        return best_action

    def expectimax(self, game_state, depth, agent_index):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state), None

        if agent_index == AGENT:  # max player
            return self.max_value(game_state, depth)

        if agent_index == OPPONENT:  # chance player
            return self.exp_value(game_state, depth)

    def max_value(self, game_state, depth):
        max_value = float('-inf')
        best_action = None

        for action in game_state.get_legal_actions(AGENT):
            successor = game_state.generate_successor(AGENT, action)
            value, _ = self.expectimax(successor, depth, OPPONENT)
            if value > max_value:
                max_value = value
                best_action = action

        return max_value, best_action

    def exp_value(self, game_state, depth):
        exp_value = 0
        actions = game_state.get_legal_actions(OPPONENT)
        if not actions:
            return self.evaluation_function(game_state), None
        probability = 1 / len(actions)  # uniform distribution

        for action in actions:
            successor = game_state.generate_successor(OPPONENT, action)
            value, _ = self.expectimax(successor, depth - 1, AGENT)
            exp_value += probability * value

        return exp_value, None


# heuristics

def smoothness_heuristic(board):
    """
    Calculate smoothness score for the board, where a smooth board has neighboring tiles with similar values.
    Higher score is better.
    """
    indices = [(3, 3), (3, 2), (3, 1), (3, 0),
               (2, 3), (2, 2), (2, 1), (2, 0),
               (1, 3), (1, 2), (1, 1), (1, 0),
               (0, 3), (0, 2), (0, 1), (0, 0)]

    smoothness_score = 0

    for (i, j) in indices:

        if j < 3:
            # Calculate smoothness for rows
            if board[i, j] != 0 and board[i, j + 1] != 0:
                smoothness_score -= abs(board[i, j] - board[i, j + 1])
            # Calculate smoothness for columns
            if board[j, i] != 0 and board[j + 1, i] != 0:
                smoothness_score -= abs(board[j, i] - board[j + 1, i])

    return smoothness_score


def weight_heuristic(board):
    """
    Compute the weighted score of the current game state. The weight of each tile is determined by its position,
    where the weight of the tile in the top-left corner is the highest and the strategy is to keep the highest tile
    in the corner. The weight decreases as we move away from the corner.
    Higher score is better.
    """
    weight_matrix = np.array([
        [4, 3, 2, 1],
        [3, 2, 1, 0.5],
        [2, 1, 0.5, 0.25],
        [1, 0.5, 0.25, 0.125]
    ])

    weighted_score = 0

    for i in range(4):
        for j in range(4):
            weighted_score += board[i, j] * weight_matrix[i][j]

    return weighted_score


def optimized_combined_heuristic(current_game_state):
    """
    Combines the heuristics for the 2048 game in an optimized way to improve the runtime.
    """
    board = current_game_state.board
    score = current_game_state.score
    max_tile = current_game_state.max_tile

    indices = [(3, 3), (3, 2), (3, 1), (3, 0),
               (2, 3), (2, 2), (2, 1), (2, 0),
               (1, 3), (1, 2), (1, 1), (1, 0),
               (0, 3), (0, 2), (0, 1), (0, 0)]

    weight_matrix = np.array([
        [4, 3, 2, 1],
        [3, 2, 1, 0.5],
        [2, 1, 0.5, 0.25],
        [1, 0.5, 0.25, 0.125]
    ])

    weighted_score = np.sum(board * weight_matrix)
    smoothness_score = 0

    for (i, j) in indices:

        if j < 3:
            # Calculate smoothness for rows
            if board[i, j] != 0 and board[i, j + 1] != 0:
                smoothness_score -= abs(board[i, j] - board[i, j + 1])
            # Calculate smoothness for columns
            if board[j, i] != 0 and board[j + 1, i] != 0:
                smoothness_score -= abs(board[j, i] - board[j + 1, i])

    # return score + 2 * weighted_score + 3 * smoothness_score
    return score + 0.5 * weighted_score + 2 * smoothness_score
    # return score + 2 * weighted_score + max_tile + 3 * smoothness_score


#

def better_evaluation_function(current_game_state):
    """
    A sophisticated evaluation function for the 2048 game that uses a linear combination of several heuristics:
    - Score (current game score)
    - Weighted score (tile values are weighted by their position, where the top left corner has the highest weight)
    - Smoothness (states with neighboring tiles with similar values are rewarded)
    """
    return optimized_combined_heuristic(current_game_state)


# Abbreviation
better = better_evaluation_function
