import sys, os

hexLookup = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
binaryLookup = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}


def main_menu():
    os.system('cls')
    print("Main menu")
    print("1. Convert hex string to binary")
    print("2. Convert binary string to hex")
    print("3. Quit")
    print("")

    choice = input(">")
    exec_menu(choice)

    return

def exec_menu(choice):
    os.system('cls')
    choice = choice.lower()
    if choice == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid choice.\n")
            menu_actions['main_menu']()

def convertToBinary(x):
    convertedString = ''
    try:
        for letter in x:
            convertedString += hexLookup.get(letter)
        print(convertedString)
        input("")
        menu_actions['main_menu']()
    except TypeError:
        print("Invalid hexademical code.")
        input("")
        menu_actions['main_menu']()

def convertToHex(x):
    convertedString = ''
    convertedPortion = ''
    i = 0
    length = len(x)
    try:
        while(i < length):
            convertedPortion = x[i:(i+4)]
            convertedString += binaryLookup.get(convertedPortion)
            i += 4
        print(convertedString)
        input("")
        menu_actions['main_menu']()
    except TypeError:
        print("Invalid binary code.")
        input("")
        menu_actions['main_menu']()

            

    print("")

def programQuit():
    sys.exit()

def ctbMenu():
    hexInput = input("Enter the hexadecimal string to convert: ")
    convertToBinary(hexInput)

def cthMenu():
    binInput = input("Enter the binary string to convert: ")
    convertToHex(binInput)

menu_actions = {'main_menu': main_menu,'1': ctbMenu, '2': cthMenu, '3': programQuit}

if __name__ == "__main__":
    main_menu()