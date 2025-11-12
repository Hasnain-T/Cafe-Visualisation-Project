# This Module is for the custom styling of the CLI
import os

def custom_border_message(message: str, symbol: str = "*", length: int = 70, align: str = "center"):
    # Prints a message between matching top and bottom borders.
    # Supports multi-line messages with optional alignment: 'left', 'center', or 'right'.
    border = symbol * length
    inner_width = length -4

    print(border)
    for line in message.splitlines():
        line = line.strip()
        if align == "left":
            aligned = line.ljust(inner_width)
        elif align == "right":
            aligned = line.rjust(inner_width)
        else: # Default to center
            aligned = line.center(inner_width)
        print(f"| {aligned} |")
    print(border)

def print_border(symbol="-", length=70):
    print(symbol * length)

def press_enter_to_continue():
    print_border()
    input("Press Enter to continue...".rjust(68))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen