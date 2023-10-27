PLAYER_WIN_BONUS = 6
DRAW_BONUS = 3
OUTCOME_BONUS = {
    'X': 0,  # Lost
    'Y': DRAW_BONUS,  # Draw
    'Z': PLAYER_WIN_BONUS  # Player wins
}
# index + 1 to get each shape's worth of points: 1 for Rock, 2 for Paper, and 3 for Scissor
SHAPES = ['A', 'B', 'C']
STRAT_LOOKUP = {
    'A': {  # if opponent uses A (rock)
        'X': 'C',  # To lose, use C (scissors)
        'Y': 'A',  # To tie, use A (rock)
        'Z': 'B'  # To win, use B (paper)
    },
    'B': {  # if opponent uses B (paper)
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    },
    'C': {  # if opponent uses C (scissors)
        'X': 'B',
        'Y': 'C',
        'Z': 'A'
    }
}

playerScores = 0

with open('input.txt') as f:
    input = f.read()
    rows = [''.join(pair.split(' ')) for pair in input.split("\n")]
    for row in rows:
        opponentShape = row[0]
        goalOutcome = row[1]
        playerShape = STRAT_LOOKUP.get(opponentShape).get(goalOutcome)
        playerScores += (SHAPES.index(playerShape) + 1) + \
            OUTCOME_BONUS.get(goalOutcome)


print(
    f"Player woulda won {playerScores} points if they follow the strategy guide.")
