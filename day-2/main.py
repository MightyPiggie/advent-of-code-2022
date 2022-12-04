


# A/X = Rock
# B/Y = paper
# C/Z = scissors
combinations_1 = [
    'B X', # 1 
    'C Y', # 2
    'A Z', # 3
    'A X', # 4
    'B Y', # 5
    'C Z', # 6 
    'C X', # 7
    'A Y', # 8
    'B Z'  # 9
]
total_1 = 0
with open('input.txt', 'r') as file:
    data = file.read()
    for i in range(0, 9):
        total_1+= (data.count(combinations_1[i])*(i+1))

print(f"Excersice 1 awnser: {total_1}")

# A = Rock
# B = paper
# C = scissors

# X = Lose
# Y = Draw
# Z = Win
combinations_2 = [
    'B X', # 1 
    'C X', # 2
    'A X', # 3
    'A Y', # 4
    'B Y', # 5
    'C Y', # 6
    'C Z', # 7
    'A Z', # 8
    'B Z'  # 9
]
        
total_2 = 0
with open('input.txt', 'r') as file:
    data = file.read()
    for i in range(0, 9):
        total_2+= (data.count(combinations_2[i])*(i+1))

print(f"Excersice 2 awnser: {total_2}")

