debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = list(map(int, f.read().splitlines()))

increases = 0
window_length = 3

for i, val in enumerate(lines[0:(len(lines)-window_length+1)]):
    one = lines[i:(i+window_length)]
    two = lines[(i+1):(i+window_length+1)]

    if sum(two) > sum(one):
        increases += 1


print(increases)
