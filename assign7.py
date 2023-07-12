def Func(file="Shub.txt"):
    try:
        with open(file, "+a") as f:
            roll_number = "46"
            name = "Shubham"
            class_name = "Tpoly"
            entries = [roll_number, name, class_name]
            f.writelines("\n".join(entries))  

        with open(file, "+r") as f:
            display = f.readlines()
            print("Entered File Content:")
            for line in display:
                print(line.strip()) 

    except FileNotFoundError:
        print(f"File '{file}' not found!")


Func()  
