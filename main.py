from pathlib import Path


def num1():
    filetype = input("What Is This Password For: ")
    acctype = input("What Nickname Would You Give This Acc: ")
    create_file(filetype)
    file_path = file_exist()

    fread = open(str(Path(filetype) / (acctype + ".txt")), "w")
    Username = input("Enter Username: ")
    Password = input("Enter Password: ")
    fread.write(Username + "\n" + Password)

    fread.close()  


def num2():
    file_path = file_exist()
    try:
        with open(file_path, "r") as file:
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


def listfiles(directory):
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


def file_exist():
    location = "C:/Users/Dekel/Documents/Visual Studio project/python project/passtest"
    files_dir = listfiles(location)

    for file_name in files_dir:
        print(file_name) 

    open_file = input("Witch File Would You Like To Open: ")
    the_path = location + "/" + open_file

    if len(open_file) >= 3:
        last3 = open_file[-4:]



    if '.' in last3 and not last3 == ".txt":
        print("i only take .txt files sorry")
        exit()
    elif not last3 == '.txt':
        the_path += ".txt"
        
    return the_path
 
        
  

print("1 Save: \n2 Read: \n3 Change:")
option = 0
while not option == 1 or option == 2 or option == 3:    
    try:
        option = int(input("|=> ", ))
        opt(option)
    except ValueError:
        print("Cant Use Words")

        
