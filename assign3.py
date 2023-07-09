class Calculator:
    def calculate():
        n1=1
        while n1 == 1:
            print("\n This is menu driven program")
            print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) floor division \n6) exponent\n")
            num=int(input("Enter your choice: "))
            if num == 1:
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Addition is : ",(x+y))
            elif num==2:
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Subtraction is : ",(x-y))
            elif num==3 :
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Multiplication is : ",(x*y))
            elif num==4:
                x=float(input("Enter first value :"))
                y=float(input("Enter second value :"))
                print("Division is : ",(x/y))
            elif num==5 :
                x=float(input("Enter first value :"))
                y=float(input("enter second value :"))
                print("floor division is : ",(x//y))
            elif num==6 :
                x=float(input("Enter first value :"))
                y=float(input("enter second value :"))
                print("exponent:",(x**y))
            else:
                print("Wrong choice")
            n=input("If you want to continue press 1 \n otherwise press any key ")
            if n!="1":
                exit()
            n1=int(n)
            
    
c=Calculator
c.calculate()