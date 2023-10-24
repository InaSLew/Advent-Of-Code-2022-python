
with open('input.txt') as f:
    input = f.read()
    elfSnackList = [list(filter(None, entry.split("\n")))
                    for entry in input.split("\n\n")]
    result = max([sum([int(calories) for calories in elfSnack])
                 for elfSnack in elfSnackList])
    print(result)
