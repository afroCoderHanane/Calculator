from art import logo

print(logo)

# Calculator

#addition

def add(x , y):
  return x + y

#substraction 

def  substract(x , y):
  return x - y

#multiplication
def multiply(x , y):
  return x * y

#division

def divide(x , y):
  return x / y

#Operation
operation={
  "/": divide,
  "*": multiply,
  "+": add,
  "-": substract
}
num1 = int(input("Enter your first number\n"))
num2 = int(input("Enter your next number\n"))

for key in operation:
  print(key)
operation_symbol = input("From an operation above pick symbol : ")

calc_function = operation[operation_symbol]
answer = calc_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")