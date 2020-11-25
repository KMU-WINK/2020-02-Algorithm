start_location = str(input())
edge_row = ['1', '8']
side_row = ['2', '7']
middle_row = ['3', '4', '5', '6']
edge_col = ['a', 'h']
side_col = ['b', 'g']
middle_col = ['c', 'd', 'e', 'f']

case = 0
if start_location[0] in edge_col and start_location[1] in edge_row:
    case = 2
elif (start_location[0] in side_col and start_location[1] in edge_row) or (start_location[0] in edge_col and start_location[1] in side_row):
    case = 3
elif (start_location[0] in edge_col and start_location[1] in middle_row) or (start_location[0] in middle_col and start_location[1] in edge_row) or (start_location[0] in side_col and start_location[1] in side_row):
    case = 4
elif (start_location[0] in side_col and start_location[1] in middle_row) or (start_location[0] in middle_col and start_location[1] in side_row):
    case = 5
else:
    case = 8

print(case)