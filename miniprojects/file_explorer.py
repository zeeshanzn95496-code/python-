print("file explorer started:")

import os 
print("current directory",os.getcwd())

def show_menu():
    print("======:file explorer:======")
    print("1 show current directory")
    print("2 list all files")
    print("3 create a folder")
    print("4 rename a file")
    print("5 search python files")
    print("7 exit")

while True:

    show_menu()

    choice = input("enter your choice(1-6)")

    if choice=="1":
        print("your current directory:",os.getcwd())
    elif choice =="2":
        files = os.listdir()
        print("\n files and folders:")
        for item in files:
            if os.path.isfile(item):
                print("files",item)
    elif choice =="3":
        folder_name= input("enter folder name:")
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print("created folder named:",folder_name)
        else:
            print(f"{folder_name}already exists")
    elif choice =="4":
        old_name = input("enter exixsting file name:")
        if os.path.isfile(old_name):
            new_name = input("enter new name:")
        if not os.path.isfile(new_name):
            os.rename(old_name,new_name)
            print("file renamed successfully")
        else:
            print("file does not exists")  
    elif choice == "5":
        count =0 
        print("\n searching python files\n")

        for root,dirs,files in os.walk("."):
            for file in files:
                if file.endswith(".py"):
                    file_path=os.path.join(root,file)
                    print("found",file_path)                
                    count+=1
            print("\ntotal python files",count)
    elif choice =="6":
        print("exiting file explorer...")
        break
    else:
        print("error ! input must be only in 1,2,3,4,5,6")
        break