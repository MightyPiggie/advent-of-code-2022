with open('input.txt', 'r') as file:
    data = file.readlines()
    total_1 = 0
    for i in range(0,len(data)):
        tmp_data = data[i].strip()
        string1 = tmp_data[:len(tmp_data)//2]
        string2 = tmp_data[len(tmp_data)//2:]
        for j in range(0, len(string1)):
            if string2.count(string1[j]) >= 1:
                char_value = ord(string1[j])
                if(char_value >96 and char_value < 123):
                    total_1 += (char_value - 96)
                    break
                if(char_value >64 and char_value < 91):
                    total_1 += (char_value - 38 )
                    break

with open('input.txt', 'r') as file:
    data = file.readlines()
    total_2 = 0
    for i in range(0,len(data), 3):
        for j in range(0, len(data[i])):
            if data[i+1].count(data[i][j]) >= 1 and data[i+2].count(data[i][j]) >= 1:
                char_value = ord(data[i][j])
                if(char_value >96 and char_value < 123):
                    total_2 += (char_value - 96)
                    break
                if(char_value >64 and char_value < 91):
                    total_2 += (char_value - 38 )
                    break


print("Awnser excersice 1: ", total_1)
print("Awnser excersice 2: ", total_2)
    
