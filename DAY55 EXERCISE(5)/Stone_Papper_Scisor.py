import random

# The matrix represents:
# Rows: Paper (0), Rock (1), Scissor (2)
# Cols: Paper (0), Rock (1), Scissor (2)

Matrics = ["Draw", "Win",  "Lose",       # Paper vs (P, R, S)
           "Lose", "Draw", "Win",        # Rock vs (P, R, S)
           "Win",  "Lose", "Draw"]       # Scissor vs (P, R, S)

names = ["Paper", "Rock", "Scissor"]

choice1 = int(input("Enter your choice\n0 for Paper\n1 for Rock\n2 for Scissor\n"))
choice2 = random.randint(0, 2)

print(f"You chose: {names[choice1]}")
print(f"Computer chose: {names[choice2]}")

# Formula to find the 1D index from 2D coordinates: (row_index * row_width) + col_index
result_index = (choice1 * 3) + choice2
print(f"Result You: {Matrics[result_index]}")