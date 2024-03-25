from pathlib import Path

location = "C:/Users/Dekel/Documents/Visual Studio project/python project/Passwords"

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

    d_type = typecheck(com_path_to)
    
    if  d_type == True:
        com_path_to = str(com_path_to)  + ".txt"       
    elif d_type == False:
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

    #check type
    d_type = typecheck(the_path)
    if d_type == True:
        the_path = str(the_path)  + ".txt"
    elif d_type == False:
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

def typecheck(path_to_file):
    t_or_f = True
    file_path = Path(path_to_file)
    file_type = file_path.suffix
    print(file_type)
    if '.' in file_type and not file_type == ".txt":

        t_or_f = False
        
    elif file_type == ".txt":
        t_or_f = True

    return t_or_f

  

print("1 Save: \n2 Read: \n3 Change:")
option = 0
while not option == 1 or option == 2 or option == 3:    
    try:
        option = int(input("|=> ", ))
        opt(option)
    except ValueError:
        print("Cant Use Words")

        
        

