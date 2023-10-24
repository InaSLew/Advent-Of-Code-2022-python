
with open('input.txt') as f:
    input = f.read()
    elfSnackList = [list(filter(None, entry.split("\n")))
                    for entry in input.split("\n\n")]
    top3TotalCalories = sorted([sum([int(calories) for calories in elfSnack])
                                for elfSnack in elfSnackList], reverse=True)[:3]
    print(sum(top3TotalCalories))

    # 206780
    # 11102016
