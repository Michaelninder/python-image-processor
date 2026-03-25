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