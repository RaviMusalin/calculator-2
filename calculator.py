"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


# Replace this with your code
# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)
while True:
    req_calculations = input("Enter your equation: ")
    response_list = req_calculations.split(" ")
    if response_list[0] == "q":
        break
    else:
        for number in response_list[1:]:
            response_list[response_list.index(number)] = float(number)
            
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