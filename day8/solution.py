f = open("input_test.txt", "r")

# make array of rows looking from left
rows = []
for line in f:
    row = []
    for num in line:
        if num != "\n":
            row.append(num)
    rows.append(row)

# copying rows but from the right
rows_r = []
for row in rows:
    ctr = len(row)-1
    new_row = []
    for x in range(len(row)):
        new_row.append(row[ctr])
        ctr -= 1
    rows_r.append(new_row)


# make array of columns looking from top
cols = []
for y in range(len(rows)):
    for x in range(len(rows[y])):
        cols.append(rows[x][y])

counter = 0
tempCols = []
col = []
for num in cols:
    col.append(num)
    counter += 1
    if counter == len(rows):
        tempCols.append(col)
        col = []
        counter = 0
cols = tempCols

# make cols arr from bottom
cols_b = []
for c in cols:
    new_col = []
    ctr = len(c)-1
    for x in range(len(c)):
        new_col.append(c[ctr])
        ctr -= 1
    cols_b.append(new_col)

views = [rows, rows_r, cols, cols_b]
total = (len(rows) * 2) + ((len(rows)-2) * 2)
# look at inner grid and determine how many visible trees

for view in views:
    temp = -1
    numTrees = 0
    for treeline in view:
        for tree in treeline:
            if temp < int(tree):
                numTrees += 1
                temp = int(tree)

    print(numTrees)


f.close()