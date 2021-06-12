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


def calc():
  
  num1 = float(input("Enter your first number\n"))
  should_continue = True
  while should_continue:
    for key in operation:
      print(key)
    operation_symbol = input("From an operation above pick symbol : ")

    num2 = float(input("Enter your next number\n"))
    calc_function = operation[operation_symbol]
    answer = calc_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    offset = input(f"press'yes' if you want to continue with {answer} or press 'no' restart with a new number" ).lower()
    if(offset == "yes"):
      num1 = answer
    else:
      calc()

calc()