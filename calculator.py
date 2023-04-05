"""CLI application for a prefix-notation calculator.

+ : add two numbers
- : subtract two numbers
* : multiplie two numbers
/ : divide two numbers
sqr : square a number
cube : cube a number
pow : takes one number and brings it to the power of another number
% : calculate remainder of two numbers
q : quit
"""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)

while True:
    req_calculations = input("Enter your equation: ")
    response_list = req_calculations.split(" ")
    if response_list[0] == "q":
        break
    else:
        for number in response_list[1:]:
            try:
                response_list[response_list.index(number)] = float(number)
            except:
                print("Make sure you type a number")
        if response_list[0] == "+":
            print(add(*response_list[1:]))

        elif response_list[0] == "-":
            print(subtract(*response_list[1:]))

        elif response_list[0] == "*":
            print(multiply(*response_list[1:]))    

        elif response_list[0] == "/":
            print(divide(*response_list[1:]))
            
        elif response_list[0] == "sqr":
            print(square(*response_list[1:]))

        elif response_list[0] == "cube":
            print(cube(*response_list[1:]))

        elif response_list[0] == "pow":
            print(power(*response_list[1:]))

        elif response_list[0] == "%":
            print(mod(*response_list[1:]))

        else:
            print("Check your command")