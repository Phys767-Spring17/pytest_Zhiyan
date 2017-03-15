#define the function "fizzbuzz()"
def fizzbuzz(number):
    
    r15=number%15
    r5=number%5
    r3=number%3
    
    if r15 == 0:
        return 'fizzbuzz'
    elif r5 == 0:
        return 'buzz'
    elif r3 == 0:
        return 'fizz'
    else:
        return number
