def temperature_converter(temp, unit):
    if unit == 'C':
        return (temp - 32) * 5/9
    elif unit == 'F':
        return (temp * 9/5) + 32
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."