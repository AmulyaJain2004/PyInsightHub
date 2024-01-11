principal = float(input("Enter the value of principal: "))
rate = float(input("Enter the value of rate: "))
time = float(input("Enter the value of time period: "))

simple_interest = (principal*rate*time)/100.0
print("Value of Simple Interest: ",simple_interest)
print("Value of Amount: ",simple_interest + principal)
