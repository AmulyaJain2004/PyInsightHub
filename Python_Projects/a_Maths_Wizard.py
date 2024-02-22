def Add(num1, num2):
    '''
    
    '''
    result = num1 + num2
    return result

def Subtract(num1, num2):
    '''
    
    '''
    result = num1 - num2
    return result

def Abs_diff (num1, num2):
    '''
    
    '''
    result = num1 - num2 if num1 > num2 else num2 - num1
    return result

def Multiply(num1, num2):
    '''
    
    '''
    result = num1 * num2
    return result

def Int_Divide (num1, num2):
    '''
    
    '''
    if num2 == 0:
        print ("Division by 0 is not allowed")
    else :
        result = num1 // num2
    return result

def Float_Divide (num1, num2):
    '''
    
    '''
    if num2 == 0:
        print ("Division by 0 is not allowed")
    else :
        result = num1 / num2
    return result

def Exponent(num1, num2):
    '''
    
    '''
    result = num1 ** num2
    return result

ops_dict = {"Add": "+", "Subtract": "-", "Abs_diff":"|", "Multiply":"*", "Float_Divide":"/", "IntDivide":"//", "Exponent":"**"}

def main():
    
    expression = input("Enter the expression")
    
    choice = 1
    while(choice):
        print("Enter + to Add 2 numbers")
        print("Enter - to Subtract 2 numbers")
        print("Enter | to perform Absolute Difference of 2 numbers")
        print("Enter * to Multiply 2 numbers")
        print("Enter // to Integer Divide 2 numbers")
        print("Enter / to Precise Divide 2 numbers")
        print("Enter ** to Raise Power of number")
        
        op =input("Enter the choice: ")

        if op in ops_dict.values():
            for i in ops_dict.values():
                if op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Add(num1, num2)
                    print(f"Addition of {num1} and {num2} is {res}")
                    
                elif op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Subtract(num1, num2)
                    print(f"Subtract of {num1} and {num2} is {res}")
                    
                elif op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Abs_diff(num1, num2)
                    print(f"Absolute difference of {num1} and {num2} is {res}")
                    
                elif op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Multiply(num1, num2)
                    print(f"Multiplication of {num1} and {num2} is {res}")
                    
                elif op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Int_Divide(num1, num2)
                    print(f"Integer division of {num1} and {num2} is {res}")
                    
                elif op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Float_Divide(num1, num2)
                    print(f"Float Division of {num1} and {num2} is {res}")
                    
                elif op == i:
                    num1 = float(input("Enter number 1: "))
                    num2 = float(input("Enter number 2: "))
                    
                    res=Exponent(num1, num2)
                    print(f"Exponent of {num1} and {num2} is {res}")
                
        else: 
            print("Enter valid operation")
            
        choice=int(input("Do you want to continue ? Type 1 for \"yes\", Type 2 for \"no\": "))
        
    print("Terminating the Program")    
    return 0

if __name__ == "__main__":
    main()
