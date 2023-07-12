f = open("input_test.txt", "r")
# f = open("input.txt", "r")

total_priority = 0


# this takes a letter, converts it into its ascii integer value
# then based on the rules of the challenge calculates its priority
def priority(letter):
    ascii_value = ord(letter)
    # capital letters
    if 64 < ascii_value < 91:
        priority_value = 27
        for x in range(65, 91):
            if x == ascii_value:
                return priority_value
            priority_value += 1

    # lower case letters
    elif 96 < ascii_value < 123:
        priority_value = 1
        for x in range(97, 123):
            if x == ascii_value:
                return priority_value
            priority_value += 1


def get_magic_letter(first, second, third):
    for letter in first:
        if letter in second and letter in third:
            return letter


iterator = 1
threeLines = []
for line in f:
    threeLines.append(str(line))
    iterator += 1
    if iterator > 3:
        total_priority += priority(get_magic_letter(threeLines[0], threeLines[1], threeLines[2]))
        for x in range(3):
            threeLines.pop()
        iterator = 1

print('Total Priority:', total_priority)
