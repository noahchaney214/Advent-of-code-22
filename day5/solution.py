# f = open("input_test.txt", "r")
f = open("input.txt", "r")


''' Decode crates and separate into stacks for each crane '''
lines = []
for line in f:
    splitLine = line.replace("    ", " * ").split()
    lines.append(splitLine)

i = 0
while not lines[i][0] == '1':
    i += 1

numCranes = len(lines[i])
starting_index = i + 2
i -= 1

stacked_crates = []
while i > -1:
    stacked_crates.append(lines[i])
    i -= 1

cranes = [None] * numCranes

for x in range(numCranes):
    crates = []
    for crate in stacked_crates:
        if x < len(crate):
            crates.append(crate[x])
    cranes[x] = crates

for g in cranes:
    for j in range(g.count('*')):
        g.remove('*')

''' Decoding instructions and reordering crates accordingly '''
for index in range(starting_index, len(lines)):
    dir = lines[index]
    numCratesToMove = int(dir[1])
    craneFrom = cranes[int(dir[3]) - 1]
    craneBuffer = []
    craneTo = cranes[int(dir[5]) - 1]

    for k in range(numCratesToMove):
        craneBuffer.append(craneFrom.pop())

    for k in range(numCratesToMove):
        craneTo.append(craneBuffer.pop())

final_string = ""
for g in cranes:
    final_string += g[len(g)-1][1]

print(final_string)

f.close()