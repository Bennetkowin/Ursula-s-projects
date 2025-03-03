def temperature_converter(temp, unit):
    #function takes in two parameters temp-ya value ya temperature na unit-ya unit kama celsius na fahrenheit
    #Basically the code converts temperature from celsius to fahrenheit and vice versa
    if unit == 'C':
        return (temp - 32) * 5/9
    #If unit is celsius convert to Fahrenheit using ii function apa juu and vice versa kwa iyo function apo down
    elif unit == 'F':
        return (temp * 9/5) + 32
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."
    #If it's neither it returns an error message