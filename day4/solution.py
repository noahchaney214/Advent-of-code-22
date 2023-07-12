#f = open("input_test.txt", "r")
f = open("input.txt", "r")

numContain = 0


def decode(code):
    numrange = []
    num_range = code.split("-")
    for x in range(int(num_range[0]),int(num_range[1])+1):
        numrange.append(int(x))
    print(numrange)
    return numrange


for line in f:
    pairs = line.split(",")
    numOverlap = 0

    one = decode(pairs[0])
    two = decode(pairs[1])

    for num in one:
        for num2 in two:
            if num == num2:
                numOverlap += 1

    if numOverlap > 0:
        numContain += 1

print(numContain)
