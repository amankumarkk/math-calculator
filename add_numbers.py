def get_sum():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2

if __name__ == "__main__":
    sum_result = get_sum()
    print(f"The sum is {sum_result}")
