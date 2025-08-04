import re


def clean_str (input_str):
    #output = ""
    output = re.sub(r'[^a-zA-Z]', '', input_str)
    #for char in input_str:
        #if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
	   #output += char
    return output

input_str = "Harish1234Kumar!!@#K252M"
result = clean_str (input_str)
print(result)