# File Handling with FileNotFoundError

# Instructions:

# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

def read_file():
    try:
        
        file_name = input("Enter the name of the file to read: ")
        
        # Attempt to open and read the file
        with open(file_name, 'r') as file:
            data = file.read()
        
        
        print("\nFile Contents:")
        print(data)
    
    except FileNotFoundError:
    
        print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")


read_file()
