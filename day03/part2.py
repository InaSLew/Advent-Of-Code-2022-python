LOWER_CASE_OFFSET = 96
UPPER_CASE_OFFSET = 38

prioScores = 0
with open('input.txt') as f:
    input = f.read()
    rows = input.split('\n')
    while (len(rows) != 0):
        group1 = rows.pop()
        group2 = rows.pop()
        group3 = rows.pop()
        badge = set(group1).intersection(
            set(group2)).intersection(set(group3)).pop()
        badgePrio = ord(badge)
        if (badge.islower()):
            prioScores += badgePrio - LOWER_CASE_OFFSET
        else:
            prioScores += badgePrio - UPPER_CASE_OFFSET

print(f'The sum of the priority scores is : {prioScores}')
