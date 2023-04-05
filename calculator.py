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

file_of_equations = open("equations.txt")

for equation in file_of_equations:
    req_calculations = equation
    response_list = req_calculations.split(" ")
    list_of_args = ["+", "-", "*", "/", "sqr", "cube", "pow", "%", "q"]

    if response_list[0] not in list_of_args:
        print("Check your command") 

    if response_list[0] == "q":
        break

    else:
        for number in response_list[1:]:
            try:
                response_list[response_list.index(number)] = float(number)
            except:
                print("Make sure you type a number")

        if len(response_list) < 3 and (response_list[0] == "sqr" or response_list[0] == "cube"):
            if len(response_list) < 2:
                print("Not enough arguments")

            elif response_list[0] == "sqr":
                print(square(*response_list[1:]))

            elif response_list[0] == "cube":
                print(cube(*response_list[1:]))

        elif len(response_list) < 3:
            print("Not enough arguments")
            
        elif response_list[0] == "+":
            print(add(*response_list[1:]))

        elif response_list[0] == "-":
            print(subtract(*response_list[1:]))

        elif response_list[0] == "*":
            print(multiply(*response_list[1:]))    

        elif response_list[0] == "/":
            print(divide(*response_list[1:]))

        elif response_list[0] == "pow":
            print(power(*response_list[1:]))

        elif response_list[0] == "%":
            print(mod(*response_list[1:]))