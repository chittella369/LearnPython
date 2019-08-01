import Translator

def factorial(number):
    result = 1
    while number > 1:
        result = result * number
        number = number-1
    return result


num = input("enter a number : ")
value = factorial(int(num))
print("factorial : "+str(value))

