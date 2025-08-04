def read_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            ##print(f"File '{filename}' exists and content read successfully.")
        return content
    except FileNotFoundError:
        ##print(f"ERROR: File '{filename}' not found.")
        return None
    except IOError as e:
        ##print(f"ERROR reading from file '{filename}': {e}")
        return None
if __name__ == "__main__":
    ##print("\n--- Reading content from 'Hrk_file.txt' ---")
    read_hrk_content = read_content(filename="Hrk_file.txt")
    if read_hrk_content:
        ##print("\nContent of 'Hrk_file.txt':")
        print(read_hrk_content)


def read_content (filename):
    try:
        with open (filename , 'r') as file :
            content = file.read()
    except IOError:
        print("Error occured while reading Content in '{filename}'")

if __name__ == '__main__':
    read_content = read_content(filename = 'Hrk_file.txt')
    if read_content:
        print(read_content)
