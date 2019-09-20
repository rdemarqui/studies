tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

# Discovering the column width
for item in range(len(tableData)):
    colWidths[item] = len(max(tableData[item], key=len))

# Printing the result
for column in range(len(tableData[0])):
    for line in range(len(tableData)):
        print(tableData[line][column].rjust(colWidths[line]), end = ' ')
        
    print()
        
        