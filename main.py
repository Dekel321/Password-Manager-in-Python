from pathlib import Path
import json

def read_location():
    with open('settings.json', 'r') as file:
        settings = json.load(file) 
        return settings['location']

location = read_location()


def create_password():
    
    folder_name = input("What Is This Password For: ")
    combined_one = Path(location) / (folder_name)
    if combined_one.exists():
        pass
    else: 
        create_file(Path(location) / (folder_name))
        print("created")

    account_file = input("What Nickname Would You Give This Acc: ")
    combined_to = Path(combined_one) / (account_file)

    t_or_f = is_txt_file(combined_to)

    if t_or_f == 1:
        pass

    elif t_or_f == 2: 
        combined_to = str(combined_to)  + ".txt"
    elif t_or_f == 3:
        print("File Type Error")
        exit()
    elif t_or_f == 4:
        print("error in code 001")

    
    file_read = open(combined_to, "w")
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")
    file_read.write(Username + "\n" + Password)

    file_read.close()  


def read_password():
    main_path = file_manage()
    t_or_f = is_txt_file(main_path)
    if t_or_f == 1:
        pass

    elif t_or_f == 2: 
        main_path = str(main_path) +".txt"
    elif t_or_f == 3:
        print("File Type Error")
        exit()
    elif t_or_f == 4:
        print("error in code 001")

    try:
        read_file = open(main_path, "r")
        file_contents = read_file.read()
        print(file_contents)
        read_file.close()
    except FileNotFoundError as e:
        print(f"Error: File '{main_path}' not found. \n {e}")
    except Exception as e:
        print(f"Error: {e}")
    

def change_password():
    print("1 Change Username: \n2 Change Password: ")
    change_option = 0
    while not change_option == 1 or 2:
        try:
            change_option = int(input("|=> ", ))
            if change_option == 1:
                change_user()
            elif change_option == 2:
                change_pass()
            else:
                print("Only Use Numbers 1 - 2")    
        except ValueError:
            print("Cant Use Words")


def list_and_open(value, write_value):
    main_path = file_manage()

    t_or_f = is_txt_file(main_path)
    if t_or_f == 1:
        pass
    elif t_or_f == 2: 
        main_path = str(main_path) +".txt"
    elif t_or_f == 3:
        print("File Type Error")
        exit()
    elif t_or_f == 4:
        print("error in code 001")

    try:
        with open(main_path, "r") as file:
            lines = file.readlines()

        if len(lines) >= 2:
            lines[int(value)] = write_value
        else:
            pass
                
        with open(main_path, "w") as file:

            file.writelines(lines)

    except FileNotFoundError as e:
        print(f"Error: File '{main_path}' not found. \n {e}")
    except Exception as e:
        print(f"Error: {e}")

def change_user():
    value = 0
    write_value = input("Pick New Username: ")
    list_and_open(value, write_value)
    

def change_pass():
    value = 1
    write_value = input("Pick New Password: ")
    list_and_open(value, write_value)

def opt(option):
    if option == 1:
        create_password()
    elif option == 2:
        read_password()
    elif option == 3:
        change_password()
    else:
        print("Only Use Numbers 1 - 3")

def create_file(make_file_in):
    try:
        Path(make_file_in).mkdir()

    except FileExistsError:
        pass
    except Exception as e:
        print(f"Failed to create directory: {e}")
        exit()


def list_files_in_directory(directory):
    file_list = []  
    try:
        files = Path(directory).glob("*")
        for file in files:
            file_list.append(file.name)  
    except FileNotFoundError:
        print("Directory not found")
    except Exception as e:
        print(f"Error: {e}")
    
    return file_list

def file_manage():
    file_directory = list_files_in_directory(location)

    for file_name in file_directory:
        print(file_name) 
    
    open_file = input("Witch File Would You Like To Open: ")
    main_path = Path(location) / (open_file)
    
    if main_path.is_dir():
        pass
    else:
        print( "'"+open_file +"'"  + " Doesnt Exist")


    if main_path.suffix == '.txt':
        main_path = Path(location) / (open_file)
        pass
    elif main_path.suffix == '':
        file_directory = list_files_in_directory(Path(location) / (open_file))

        for file_name in file_directory:
            print(file_name)

        open_file_2nd = input("Witch File Would You Like To Open: ")
        main_path = Path(location) / (open_file) / (open_file_2nd)
        return main_path
    
def is_txt_file(path_to_file):
    t_or_f = 4
    file_path = Path(path_to_file)
    value = file_path.suffix
    if value == ".txt":
        t_or_f = 1

    elif value == '':
        print(file_path.suffix)
        t_or_f = 2
      
    elif len(value) > 0:
        print(file_path.suffix)
        t_or_f = 3
    else:
        print("error in code 1")

    return t_or_f

print("1 Save: \n2 Read: \n3 Change:")
option = 0
while not option == 1 or 2 or 3:    
    try:
        option = int(input("|=> ", ))
        opt(option)
    except ValueError:
        print("Cant Use Words")
