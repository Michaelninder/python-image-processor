from PIL import Image
from math import gcd

def empty_line(count = 1):
    for i in range(count):
        print()

def emptyLine(count):
    empty_line(count)

def get_input(prompt, valid_options=None, case_sensitive=False):
    while True:
        user_input = input(prompt)
        
        if valid_options is None:
            return user_input
        
        check_input = user_input if case_sensitive else user_input.lower()
        check_options = (
            valid_options if case_sensitive 
            else [opt.lower() for opt in valid_options]
        )
        
        if check_input in check_options:
            return check_input
        
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

def load_image(filepath):
    try:
        return Image.open(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, output_path):
    try:
        image.save(output_path)
        print(f"Image saved to: {output_path}")
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

def check_if_starts(haystack, not_needle):
    return haystack[0] == not_needle

def check_if_ends(haystack, not_needle):
    return haystack[-1] == not_needle

def trim_quotes(string):
    if (check_if_ends(string, '"') and check_if_starts(string, '"')):
        return string[1:-1]
    elif (check_if_ends(string, "'") and check_if_starts(string, "'")):
        return string[1:-1]
    return string

def calc_ratio(width, height):
    width = int(width)
    height = int(height)
    divisor = gcd(width, height)
    return f"{width // divisor}:{height // divisor}"