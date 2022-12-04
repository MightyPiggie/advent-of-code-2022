with open('input.txt', 'r') as file:
    data = file.readlines()
    total_1 = 0
    for i in range(0,len(data)):
        pair = data[i].strip().split(',')
        elv1 = pair[0].split('-')
        elv2 = pair[1].split('-')
        elv1_start = int(elv1[0])
        elv1_end = int(elv1[1])
        elv2_start = int(elv2[0])
        elv2_end = int(elv2[1])

        if elv1_start <= elv2_start and elv1_end >= elv2_end:
            total_1 += 1
        elif elv1_start >= elv2_start and elv1_end <= elv2_end:
            total_1 += 1

with open('input.txt', 'r') as file:
    data = file.readlines()
    total_2 = 0
    for i in range(0,len(data)):
        pair = data[i].strip().split(',')
        elv1 = pair[0].split('-')
        elv2 = pair[1].split('-')
        elv1_start = int(elv1[0])
        elv1_end = int(elv1[1])
        elv2_start = int(elv2[0])
        elv2_end = int(elv2[1])

        if elv2_start <= elv1_start and elv1_start <= elv2_end:
            total_2 += 1

        elif elv1_start <= elv2_start and elv2_start <= elv1_end:
            total_2 += 1



print("Awnser excersice 1: ", total_1)
print("Awnser excersice 2: ", total_2)
