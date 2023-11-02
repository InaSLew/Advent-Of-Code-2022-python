# Seperate the stack plot and (re)arrange procedure
# Turn the stack plot into actually workable stacks
# Mutate stacks according to the (re)arrange procedure


with open('input.txt') as f:
    raw = f.read().split('\n\n')
    stackPlot = [item.replace('    ', ' []').split(' ')
                 for item in raw[0].split('\n')][:-1]
    arrangeProc = [[int(x) for x in list(filter(lambda x: x.isdigit(), item.split()))]
                   for item in raw[1].split('\n')]

    # crates to move / origin stack / target stack

    # construct workable stacks
    supplyStacks = [[], [], [], [], [], [], [], [], []]
    for row in stackPlot:
        # cellIdx indicates which stack cell/crate belongs to
        for cellIdx, cell in enumerate(row):
            cell = cell.strip('[]')
            if cell != '':
                supplyStacks[cellIdx].append(cell)

    supplyStacks = [list(reversed(stack)) for stack in supplyStacks]
    for cratesToMove, originStackNumber, targetStackNumber in arrangeProc:
        cratesHolder = []
        while (len(cratesHolder) != cratesToMove):
            temp = supplyStacks[originStackNumber - 1].pop()
            cratesHolder.append(temp)

        cratesHolder = list(reversed(cratesHolder))
        for crate in cratesHolder:
            supplyStacks[targetStackNumber - 1].append(crate)

    print(
        f"The top row of the stacks is {''.join([stack[-1] for stack in supplyStacks])}")
