
def divide_function(intA, intB):
    try:
        return round(intA/intB)
    except ZeroDivisionError:
        raise ZeroDivisionError
