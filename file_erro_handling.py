def modify_content (content):
    return content.upper()

def proccess_file():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as file:
            original_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_name}'.")
        return
    modified_content = modify_content(original_content)
    new_file_name = "modified_" + file_name
    try:
        with open(file_name, 'w') as target_file:
            target_file.write(modified_content)
            print(f"File '{file_name}' has been modified successfully.")
    except IOError:
        print(f"Error: An error occurred while writing to the file '{new_file_name}'.")
        return
    
proccess_file()