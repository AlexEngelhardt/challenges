debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()

increases = 0
depth = int(lines[0])

for new_depth in lines[1:]:
    if int(new_depth) > depth:
        increases += 1
    depth = int(new_depth)

print(increases)
