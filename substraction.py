#function for substraction
def substract(a,b):
    if b > a:
        raise ValueError('Result cannot be negative')
    return(a-b)
