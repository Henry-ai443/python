def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32 

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def convert_temperature():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature(C , F , K): ")
    target_unit = input("Enter the target unit to convert to (C, F, K): ")

    if unit == "c":
        if target_unit == "f":
            converted_temperature = celsius_to_fahrenheit(temp)
            print(f"{temp}C is equal to {converted_temperature}F")
        elif target_unit == "k":
            converted_temperature = celsius_to_kelvin(temp)
            print(f"{temp}C is equal to {converted_temperature}K")
        else:
            print("Invalid target unit")
    elif unit == "f":
        if target_unit == "c":
            converted_temperature = fahrenheit_to_celsius(temp)
            print(f"{temp}F is equal to {converted_temperature}C")
        elif target_unit == "k":
            temp_in_celsius = fahrenheit_to_celsius(temp)
            converted_temperature = celsius_to_kelvin(temp_in_celsius)
            print(f"{temp}F is equal to {converted_temperature}K")
        else:
            print("Invalid target unit")
    elif unit == "k":
        if target_unit == "c":
            converted_temperature = kelvin_to_celsius(temp)
            print(f"{temp}K is equal to {converted_temperature}C")
        elif target_unit == "f":
            temp_in_celsius = kelvin_to_celsius(temp)
            converted_temperature = celsius_to_fahrenheit(temp_in_celsius)
            print(f"{temp}K is equal to {converted_temperature}F")
        else:
            print("Invalid target unit!")
    else:
        print("Invalid input for the unit!")