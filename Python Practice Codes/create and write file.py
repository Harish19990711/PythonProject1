def create_file(filename, content):
    try:
        with open(filename, 'w') as filename:
            filename.write(content)
    except IOError:
     print(f"Error writing to file '{filename}' : {e} ")

if __name__ == "__main__" :
   test_file = "Hrk_file.txt"
   inital_content = ' Hello harish you got job offer.\n'
   print("---Writing to file ----")
   create_file(test_file , inital_content)
   print(inital_content)

