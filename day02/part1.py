# Opponent: A for Rock, B for Paper, and C for Scissors.
# Player: X for Rock, Y for Paper, and Z for Scissors.
# Points of shape: 1 for Rock, 2 for Paper, and 3 for Scissors

# winning combinations, worth 6 points: 'AY', 'BZ', 'CX'
# draw combination, worth 3 points: 'AX', 'BY', 'CZ'
# losing combinations earn no points.

# sudo code
# find winning combinations and add the win-bonus to score
# find the draw combinations and add the draw-bonus to score
# add points earned through all player-symbols

PLAYER_SHAPES = ['X', 'Y', 'Z']
PLAYER_WIN_COMBOS = ['AY', 'BZ', 'CX']
PLAYER_WIN_BONUS = 6
DRAW_COMBOS = ['AX', 'BY', 'CZ']
DRAW_BONUS = 3

playerScores = 0

with open('input.txt') as f:
    input = f.read()
    rows = [''.join(pair.split(' ')) for pair in input.split("\n")]
    for row in rows:
        if row in PLAYER_WIN_COMBOS:
            playerScores += PLAYER_WIN_BONUS
        elif row in DRAW_COMBOS:
            playerScores += DRAW_BONUS
        shapeScore = PLAYER_SHAPES.index(row[1]) + 1
        playerScores += shapeScore

print(
    f"Player woulda won {playerScores} points if they follow the strategy guide.")
