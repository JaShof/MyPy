import os
import sys

def add_txt_extension_to_files_in_folder(folder_path):
    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        # Check if the file doesn't have an extension
        if '.' not in file:
            # Rename the file to add .txt extension
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, file + '.txt'))

def find_in_file(file_path, search_text, lines_to_search):
    
     # List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    found = False    
    foundin = ""
    for file in files:                
        # Open the file
        with open(file, 'r') as f:
            # Read the first n lines
            content_lines = [f.readline() for _ in range(lines_to_search)]
            content = ''.join(content_lines)
            # Check if the text is in the content
            if search_text in content:
                found = True
                foundin += f.name + "\n" 
                print("*", end="")
            else:
                print(".", end="")
            f.close()            
    print("\n")
    print("Found in: \n" + foundin)
    return found
        
def menu(folder_path): 
    loop = True   
    while loop:
        ## Menu
        print("Target Folder: " + folder_path)
        print("")
        print("Menu")
        print("1. Add .txt extension to files in folder")
        print("2. Find text in file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_txt_extension_to_files_in_folder(folder_path)
            print("Files renamed successfully!") 
        elif choice == "2":           
            search_text = input("Enter the text to search: ")
            lines_to_search = int(input("Enter the number of lines to search: "))
            if find_in_file(folder_path, search_text, lines_to_search):
                print("The text was found in the file!")
            else:
                print("\nThe text wasn't found in the file!")
        elif choice == "3":
            #loop = False
            print("Exiting...")
            exit(0)   
        else:
            print("Invalid choice!")        
    


if __name__ == "__main__":
    if len(sys.argv) == 2:
        folder_path = sys.argv[1]
    else:
        folder_path = input("Enter the path to the folder: ")
    
    #Get the full path    
    folder_path = os.path.abspath(folder_path)

    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("The folder doesn't exist!")
        exit(1)
    else:
        menu(folder_path)
