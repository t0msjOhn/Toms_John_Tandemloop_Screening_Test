input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

result = { 1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0}

i = 1
while i <= 9:
    count = 0
    j = 0
    while j < len(input_list):  
        if input_list[j] % i == 0:
            count = count + 1
        j = j + 1
    result[i] = count
    i = i + 1

print(result)
