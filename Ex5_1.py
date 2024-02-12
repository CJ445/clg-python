def file_operations(file_path):
    # Calculate the number of upper-case letters and lower-case letters
    with open(file_path, 'r') as file:
        content = file.read()
        upper_count = sum(1 for char in content if char.isupper())
        lower_count = sum(1 for char in content if char.islower())
    
    print(f"Number of upper-case letters: {upper_count}")
    print(f"Number of lower-case letters: {lower_count}")
    
    # Search a word in a particular line
    line_number = int(input("Enter the line number to search: "))
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if line_number <= len(lines):
            line = lines[line_number - 1]
            word_to_search = input("Enter the word to search: ")
            if word_to_search in line:
                print(f"Word '{word_to_search}' found in line {line_number}")
            else:
                print(f"Word '{word_to_search}' not found in line {line_number}")
        else:
            print("Invalid line number")
    
    # Search a word in the range of lines
    start_line = int(input("Enter the starting line number: "))
    end_line = int(input("Enter the ending line number: "))
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if start_line <= end_line and end_line <= len(lines):
            words_to_search = input("Enter the words to search (separated by space): ").split()
            for i in range(start_line - 1, end_line):
                line = lines[i]
                for word_to_search in words_to_search:
                    if word_to_search in line:
                        print(f"Word '{word_to_search}' found in line {i + 1}")
        else:
            print("Invalid line numbers")
    
    # Replace a word in the file
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")
    with open(file_path, 'r') as file:
        content = file.read()
        new_content = content.replace(word_to_replace, replacement_word)
    
    with open(file_path, 'w') as file:
        file.write(new_content)
    
    print(f"Word '{word_to_replace}' replaced with '{replacement_word}' in the file")

file_operations("./hello.txt")
