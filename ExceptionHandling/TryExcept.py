from ExceptionHandling import InputTooSmallError
from ExceptionHandling import InputTooLargeError

alphabet = 'm'

while True:
    try:
        apb = input("Enter an alphabet: ")
        if apb < alphabet:
            raise InputTooSmallError
        elif apb > alphabet:
            raise InputTooLargeError
        break
    except InputTooSmallError:
        print("The entered alphabet is too small, try again!")
        print('')
    except InputTooLargeError:
        print("The entered alphabet is too large, try again!")
        print('')