def count_vowles(s):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    v_found = []
    c_found = []
    for char in s:
        #if char.isalpha():
            if char in vowels:
                v_count += 1
                v_found.append (char)
            else:
                c_count +=1
                c_found.append (char)

    return v_count, c_count, v_found, c_found


input_string = input("Enter String : ")
vowels, consonants, vowel_list, consonant_list = count_vowles(input_string)
print ("No. of Vowles : ", vowels)
print ("Vowles found : ",",".join(vowel_list))
print ("No. of Constants: ",  consonants)
print ("Consonants found : ",",".join(consonant_list))
