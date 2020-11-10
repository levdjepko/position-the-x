# 3x3 board
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


column = int(position[1]) - 1
row = int(position[0])
if (row == 1):
  row1[column] = 'x'
elif (row == 2):
  row2[column] = 'x'
elif (row == 3):
  row3[column] = 'x'  

print(f"{row1}\n{row2}\n{row3}")
