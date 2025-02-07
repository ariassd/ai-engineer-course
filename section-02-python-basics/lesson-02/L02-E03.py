list = [3, 6, 1, 9, 3, 5, 9, 8, 7, 1]
higher = 0
for i_num in list:
    if i_num > higher:
        higher = i_num

print(f"the highest number is {higher}")
