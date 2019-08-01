import random

meters_in_kilometer = 1000
feet_in_mile = 5280


def rollDice(num):
    return random.randint(1,num)


def get_file_extension(filename):
    return filename[filename.index(".")+1 :]

'''
ext = get_file_extension("employees.txt")
print("extension : "+ext)
'''
