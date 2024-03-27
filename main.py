from pathlib import Path
import json

def read_location():
    with open('settings.json', 'r') as file:
        settings = json.load(file) 
        return settings['location']


location = read_location()

def typecheck(path_to_file):

    file_path = Path(path_to_file)
    file_type = file_path.suffix

    print(file_type)
    if '.' in file_type and not file_type == ".txt":
        t_or_f = 2
        
    elif file_type == ".txt":
        t_or_f = 1

    return t_or_f



def num1():
    
    folder_name = input("What Is This Password For: ")
    com_path_one = Path(location) / (folder_name)
    if com_path_one.exists():
        pass
    else: 
        create_file(Path(location) / (folder_name))
        print("created")

    account = input("What Nickname Would You Give This Acc: ")
    com_path_to = Path(com_path_one) / (account)

    t_or_f = typecheck(com_path_to)
    
    if  t_or_f == 1:
        com_path_to = str(com_path_to)  + ".txt"       
    elif t_or_f == 2:
        print("Cant Save Your Passwords In That File Type \nOR \nCant End With '.' In The Last 3 Letters")
        exit()  
    else:
        print("some error just fix me")
    
    fread = open(com_path_to, "w")
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")
    fread.write(Username + "\n" + Password)

    fread.close()  


def num2():
    files_dir = list_files(location)

    for file_name in files_dir:
        print(file_name) 
    
    open_file = input("Witch File Would You Like To Open: ")
    the_path = Path(location) / (open_file)
    
    if the_path.is_dir():
        pass
    else:
        print( "'"+open_file +"'"  + " Doesnt Exist")

    file_type = the_path.suffix
    if file_type == '.txt':
        the_path = Path(location) / (open_file)
        pass
    else:
        files_dir = list_files(Path(location) / (open_file))

        for file_name in files_dir:
            print(file_name) 

        open_again = input("Witch File Would You Like To Open: ")
        the_path = Path(location) / (open_again)
        print(the_path)


    #check type
    t_or_f = typecheck(the_path)
    if t_or_f == 1:
        the_path = str(the_path)  + ".txt"
    elif t_or_f == 2:
        print("file is not .txt")
        exit()

    try:
        with open(the_path, "r") as file:
            file_contents = file.read()
            print(file_contents)
            exit()
    except Exception as e:
        print(f"Error: {e}")
    

def num3():
    print("changed")

def opt(option):
    if option == 1:
        num1()
    elif option == 2:
        num2()
    elif option == 3:
        num3()
    else:
        print("Only Use Numbers 1 - 3")


def create_file(folder):
    try:
        Path(folder).mkdir()

    except FileExistsError:
        pass
    except Exception as e:
        print(f"Failed to create directory: {e}")
        exit()


def list_files(directory):
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


print("1 Save: \n2 Read: \n3 Change:")
option = 0
while not option == 1 or option == 2 or option == 3:    
    try:
        option = int(input("|=> ", ))
        opt(option)
    except ValueError:
        print("Cant Use Words")

