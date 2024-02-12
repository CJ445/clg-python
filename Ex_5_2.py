def write_to_file():
    file_path = input("Enter the file path: ")
    
    with open(file_path, 'w') as file:
        while True:
            line = input()
            if line == "end of the line":
                break
            file.write(line + "\n")
    
    print("Input written to file successfully!")

write_to_file()
