f = open("input.txt", "r")
line = f.read()
print(line)
queue = []
num_letters = 0
total_letters = 0
for letter in line:
    unique = True
    queue.append(letter)
    num_letters += 1
    total_letters += 1
    if num_letters == 14:
        print(queue)
        copy_of_queue = queue.copy()
        for lets in queue:
            copy_of_queue.pop(0)
            for let2s in copy_of_queue:
                if lets == let2s:
                    unique = False
        queue.pop(0)
        num_letters -= 1
        if unique:
            print(total_letters)
            break
f.close()