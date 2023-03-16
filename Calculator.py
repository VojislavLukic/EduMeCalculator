

# function to return sum of 2 integers
def sum_function(intA, intB):
    return intA+intB

# function to divide 2 integers and return value rounded to nearest integer
def divide_function_round(intA, intB):
        try:
            return round(intA/intB)
        except ZeroDivisionError:
            print("Divide Function: Cannot divide by zero")


