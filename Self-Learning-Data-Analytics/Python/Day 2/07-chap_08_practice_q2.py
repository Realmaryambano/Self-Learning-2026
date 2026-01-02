# 2. Write a python program using function to convert Celsius to Fahrenheit.
celsius = float(input("Enter value of celsius: "))
def c_to_f(celsius):
    return (celsius * 9/5) + 32

print(f"The temperature after converting from Celsius to Fahrenheit is: {c_to_f(celsius):.2f}°F")
