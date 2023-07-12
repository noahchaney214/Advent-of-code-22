# aoc_template.py

import pathlib
import sys
from elf import Elf

f = open("input.txt", "r")

elfs = []
newElf = Elf()

for x in f:
    if not x.strip():
        elfs.append(newElf)
        newElf = Elf()
    else:
        newElf.addCalories(int(x))

topThree = []
for x in range(3):
    maxCal = 0
    temp = 0
    for cals in elfs:
        if cals.totalCalories > maxCal:
            maxCal = cals.totalCalories
            temp = cals

    topThree.append(maxCal)
    elfs.remove(temp)

topThreeCalories = topThree[0] + topThree[1] + topThree[2]
print(topThreeCalories)

f.close()