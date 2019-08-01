def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

    return result


base_num = input("Enter the base number : ")
pow_num = input("Enter the power number : ")

value = raise_to_power(int(base_num), int(pow_num))

print(value)
