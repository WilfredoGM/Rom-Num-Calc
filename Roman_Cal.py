# Egan Schmidt Weiss on Tue 2 Nov 15:50-16:02
# Some of the variable names are written in Spanish my native language
# This Print is to make visually more comfortable
print()

# This Function Turns a Roman Number to a Intenger


def rom_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90}
    i = 0
    num = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in rom_val:
            num += rom_val[s[i:i+2]]
            i += 2
        else:
            num += rom_val[s[i]]
            i += 1
    return num

# This Function sees if the Roman Number enter is a Valid Roman Number


def check_if_rom_num(numeral):
    valid_rom_num = ["C", "L", "X", "V", "I"]
    for letters in numeral:
        if letters not in valid_rom_num:
            print(f"Sorry {numeral} is not a valid roman numeral")
            print()
            break
        elif letters in valid_rom_num:
            return True

# This Function add two numbers


def sumar(x, y):
    return x + y

# This Function subtracts two numbers


def restar(x, y):
    if y >= x:
        print("Can't Print Negative Values")
        return 0
    else:
        return x - y

# This Function multiplies two numbers


def multiplicacion(x, y):
    return x * y

# This Function divides two numbers


def division(x, y):
    return int(x / y)

# This Function Turns a Intenger to a Roman Number


def int_to_rom_num(num):
    val = [100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# This Function deside which calculation make


def equation(f):
    if f == "+":
        suma = sumar(number1, number2)
        if suma <= 380:
            return suma
        else:
            print(f"{suma} is out of Range")
            suma = 0
            return suma
    elif f == "-":
        resta = restar(number1, number2)
        if resta <= 380:
            return resta
        else:
            print(f"{resta} is out of Range")
            resta = 0
            return resta
    elif f == "*":
        multiplicar = multiplicacion(number1, number2)
        if multiplicar <= 380:
            return multiplicar
        else:
            print(f"{multiplicar} is out of Range")
            multiplicar = 0
            return multiplicar
    elif f == "/":
        dividir = division(number1, number2)
        if dividir <= 380:
            return dividir
        else:
            print(f"{dividir} is out of Range")
            dividir = 0
            return dividir


# Lists and Variable to valid while loops
equations = ["+", "-", "*", "/"]
continuar = "y"
valid_letter = ["C", "L", "X", "V", "I"]

# Calculator API
while continuar == "y":
    print("Valid Roman Numbers", end=" ")
    print(' '.join(valid_letter))
    num1 = input("Enter First Roman Number: ").upper()
    while check_if_rom_num(num1) and num1.isalpha:
        number1 = rom_to_int(num1)
        num2 = input("Enter Second Roman Number: ").upper()
        if check_if_rom_num(num2) and num2.isalpha:
            number2 = rom_to_int(num2)
            func_symbol = input("What you want to do +, -, *, /: ")
            if func_symbol in equations:
                print(int_to_rom_num(equation(func_symbol)))
                num1 = ""
                num2 = ""
                print()
                continuar = input(
                    "Want to make another Equation (y/n): ").lower()
                print()
            else:
                print(f"{func_symbol} is not a Valid Function")
                print()
                func_symbol = input("What you want to do +, -, *, /: ")
                if func_symbol in equations:
                    print(int_to_rom_num(equation(func_symbol)))
                    num1 = ""
                    num2 = ""
                    print()
                    continuar = input(
                        "Want to make another Equation (y/n): ").lower()
                    print()

print()
print("Goodbye 👋")
