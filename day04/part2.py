# Looking for ANY overlap

overlappingPairs = 0

with open('input.txt') as f:
    pairs = [item for item in [row.split(',')
                               for row in f.read().split('\n')]]
    for pair in pairs:
        firstElf = [int(entry) for entry in pair[0].split('-')]
        secondElf = [int(entry) for entry in pair[1].split('-')]
        firstElfCoverage = range(firstElf[0], firstElf[1] + 1)
        secondElfCoverage = range(secondElf[0], secondElf[1] + 1)
        if (len(set(firstElfCoverage).intersection(set(secondElfCoverage))) > 0):
            overlappingPairs += 1


print(f"{overlappingPairs} pairs of elf's shifts need rework.")
