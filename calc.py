class user:
    import random
while True:
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multipy(x,y):
        return x*y
    def divide(x,y):
        return x/y
    print("\n\n ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ")
    print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗") 
    print("██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝") 
    print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
    print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
    print("╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
    print("\033[0;37m\nOperators\n[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")
    name = input("\nEnter Your Name: ")
    oper = input("Enter Operator: ") 
    if oper != '1' and oper != '2' and oper != '3' and oper != '4':
        print("Invalid Operator!!")
        invop = input("\nWant To Enter Operator Again?\ny for yes, n for no: ")
        if invop == 'y':
           continue
        if invop == 'n':
           break
        if invop != 'y' and invop != 'n':
            print("Invalid Response!!\nPlease Type (y and n) only")
        yn = input("\nWant To Enter Operator Again?\ny for yes, n for no: ")
        if yn == 'y':
            continue
        if yn == 'n':
            break      
    firnum = int(input("Enter First Number: "))
    secnum = int(input("Enter Second Number: "))

    if oper == '1':
        print("\nOperator: [ Addition ]\nAnswer: ","[",add(firnum,secnum),"]")
    elif oper == '2':
        print("\nOperator: [ Subtraction ]\nAnswer: ","[",subtract(firnum,secnum),"]")
    elif oper == '3':
        print("\nOperator: [ Multiplication ]\nAnswer: ","[",multipy(firnum,secnum),"]")
    elif oper == '4':
        print("\nOperator: [ Division ]\nAnswer: ","[",divide(firnum,secnum),"]")
        
    wan = str(input("\nWant To Solve Again?\ny for yes, n for no: "))
    if wan == 'n':
        print("\nThanks",name,"For Using This\nCreated By: John Michael Manlangit")
        break
    

        
                    

    

            
    




    



