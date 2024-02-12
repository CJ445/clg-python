def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
    
    return longest_word

file_path = input("Enter the file path: ")
longest_word = find_longest_word(file_path)
print(f"The longest word in the file is: {longest_word}")
