# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
LOWER_CASE_OFFSET = 96
UPPER_CASE_OFFSET = 38

prioScores = 0
with open('input.txt') as f:
    input = f.read()
    rows = input.split('\n')
    itemSets = [set(
        row[:len(row)//2]).intersection(set(row[len(row)//2:])) for row in rows]
    for entry in itemSets:
        if (len(entry) == 0):
            continue
        item = entry.pop()
        itemASCII = ord(item)
        if (item.islower()):
            prioScores += itemASCII - LOWER_CASE_OFFSET
        else:
            prioScores += itemASCII - UPPER_CASE_OFFSET

    print(f'The sum of the priority scores is : {prioScores}')
