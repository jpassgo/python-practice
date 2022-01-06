# 
# 640. Solve the Equation
# 
# Solve a given equation and return the value of 'x' in the form of a string "x=#value". 
# The equation contains only '+', '-' operation, the variable 'x' and its coefficient. 
# You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are 
# infinite solutions for the equation.
# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.
# 
# https://leetcode.com/problems/solve-the-equation/
# 




def solveEquation( equation: str) -> str:
    sides_of_equation = equation.split('=')
    left_side = 0
    right_side = 0
    left_side_x_count = 0
    right_side_x_count = 0
    
    previous_value = 0        
    current_operation = ''
    for i in range(0,1):            
        for c in sides_of_equation[i]:
            current_value = 0
            skip = False
            
            if c == '+' or c == '-':
                current_operation = c
                skip = True
            elif c != 'x':                    
                current_value = int(c)
            else:
                if i == 0:
                    left_side_x_count += 1
                    skip = True
                else:
                    right_side_x_count += 1
                    skip = True
                
            if not skip and current_operation == '+':
                previous_value += int(c)
            elif not skip and current_operation == '-':
                previous_value -= int(c)
                
        if i == 0:
            left_side = previous_value
            i += 1
        else:
            right_side = previous_value
                
        print(right_side)
        print(left_side)
                

solveEquation("x+5-3+x=6+x-2")
        