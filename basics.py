#flatten nested list

#nested_list = [1, 2, 3, [4, 5], 3, [7, 9], 10, 11]
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list

input_list = [1, 2, 3, [4, 5], 3, [7, 9], 10, 11]
output_list = flatten(input_list)
print(flatten(input_list))
print(sorted(flatten(input_list)))
print(set(sorted(flatten(input_list))))