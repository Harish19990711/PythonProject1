string = 'Harish Kumar K M'
print (string[::-1])



def reverse_string_loop(input_str):
    rev_string = ""  # Initialize rev_string as an empty string
    for char in input_str: # Use 'char' for clarity instead of 'arr1'
        rev_string = char + rev_string # Prepend each character
    return rev_string # Return after the loop has finished

print(reverse_string_loop('Harish Kumar K M'))

def rev_str(input):
    reverse = ""
    for char in input:
	    reverse = char + reverse
    return reverse
print(rev_str("REVERSE"))

