# Looking for COMPLETELY overlapped

completeOverlap = 0

with open('input.txt') as f:
    pairs = [item for item in [row.split(',')
                               for row in f.read().split('\n')]]
    for pair in pairs:
        elf1 = [int(entry) for entry in pair[0].split('-')]
        elf2 = [int(entry) for entry in pair[1].split('-')]
        elf1Coverage = range(elf1[0], elf1[1] + 1)
        elf2Coverage = range(elf2[0], elf2[1] + 1)
        biggerCoverage = elf1Coverage if len(elf1Coverage) >= len(
            elf2Coverage) else elf2Coverage
        smallerCoverage = elf1Coverage if len(elf1Coverage) < len(
            elf2Coverage) else elf2Coverage

        if ((biggerCoverage[0] <= smallerCoverage[0]) and (biggerCoverage[-1] >= smallerCoverage[-1])):
            completeOverlap += 1


print(f"{completeOverlap} pairs of elf's shifts need rework.")
