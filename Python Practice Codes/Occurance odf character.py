def occ_str(input):
    count_char = {}

    for char in input:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    return count_char


input = "occurance"
result = occ_str(input)

for char, count in result.items():
    print(f" '{char}':{count}", end=",")