"""Simply increasing the numbers in part 1 doesn't work.
Let's first refactor part 1 to be fast, then adapt the numbers to part 2"""

test_input = True
debug = True
part = 1

if test_input:
    order = list(map(int, list('389125467')))
else:
    order = list(map(int, list('398254716')))

if part == 2:
    order += range(10, 1_000_001)

current_label = order[0]


def step(order, current_label):
    # Modify 'order' in-place


    return current_label


n_moves = 10 if debug else 100

for move in range(1, n_moves+1):
    order, current_label = step(order, current_label)

if part == 1:
    print("".join(order))  # the final order
elif part == 2:
    i = order.index(1)
    print(order[(i+1) % len(order)] * order[(i+2) % len(order)])
