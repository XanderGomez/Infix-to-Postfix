#Name: Alexander Gomez
#ID: 27930798
#Email: xandergomez@unomaha.edu


def convert(infix:str) -> list | str:
    """
    Converts input/infix into postfix

    Parameters:
        infix(str): Infix is the user input that needs to be converted

    Returns:
        list|str: Returns either a string of an error message, or a successfully converted list of the postfix 
    """
    
    # Use a stack to covert infix to postfix
    stack = []
    postfix = []# output
    full_num = ''
    #Removes all whitespace from the equation so the testcases only check actual characters
    infix = str(infix).replace(" ", "")

    #Makes sure that the equation doesn't end with an operator which would be illegal syntax
    if len(infix) > 0:
            if str(infix[-1]).isdigit() == False and infix[-1] != ')':
                if str(infix[-1]).isalnum():
                    return 'Only numbers allowed'
                else:
                    return 'Invalid Input'
                
    for c in infix:
        #Checks if c is a digit and adds it to a full_num value so that if the number is more than 1 digit it will be captured as so
        if str(c).isdigit():
            full_num += str(c)
            last = c
        #Returns the fully completed number once a digit no longer follows another digit
        elif full_num != '':
            postfix.append(full_num)
            full_num = ''
        #Starts checking loop for operands
        if c == '(':
            stack.append(c)
            last = c
        elif c == ')':
            #Checks to make sure that there is a parentheses to close before closing, otherwise returning error
            if '(' in stack:
                while len(stack) > 0 and stack[-1] != '(':
                    poped_char = stack.pop()
                    postfix.append(poped_char)
                stack.pop()
            else:
                return 'Invalid Input'
        elif c == '+' or c == '-':
            #Last refers to the last character evaluated, so that it catches cases where multiple operators are put together (3++3 or 3*-20, etc.)
            if last == '*' or last == '/' or last == '+' or last == '-':
                return 'Invalid Input'
            #Makes sure to pop all operands that a + or - needs to in the stack
            while len(stack) > 0 and (stack[-1] == '/' or stack[-1] == '*' or stack[-1] == '+' or stack[-1] == '-'):
                if stack[-1] == '(':
                    break
                poped_char = stack.pop()
                postfix.append(poped_char)
            stack.append(c)
            last = c
        elif c == '/' or c == '*':
            #Same as last applying to all other evaluations
            if last == '*' or last == '/' or last == '+' or last == '-':
                return 'Invalid Input'
            #Makes sure to pop but only applies to * and /
            while len(stack) > 0 and (stack[-1] == '/' or stack[-1] == '*'):
                if stack[-1] == '(':
                    break
                poped_char = stack.pop() 
                postfix.append(poped_char)
            stack.append(c)
            last = c
        #Used to include the isdigit() check in the main if/else statment itself as the first is separate
        elif str(c).isdigit():
            last = c
        #Catches alphabetical letters entered in the middle of the evaluation as well as other unknown characters
        else:
            if str(c).isalnum():
                return 'Only numbers allowed'
            else:
                return "Invalid Input"           
    
    #Makes sure to deposit whatever number may be left to put in the stack(necessary as part of my multi-digit num implementation)
    if full_num != '':
            postfix.append(full_num)
    #Pops and appends any remaining operators in the stack (also checks to make sure no open parentheses are there)
    while len(stack) > 0:
        poped_char = stack.pop()
        if poped_char == '(':
            return 'Invalid Input'
        else:
            postfix.append(poped_char)

    return postfix

# Returns double for division
def evaluate(postfix:list) -> str|float:
    """
    Takes the postfix created by the convert function and evaluates it

    Parameters:
        postfix(list): List of the postfix values needed to be evaluated
    
    Returns:
        str|float: Returns either a str value for an error message or the float value of the evaluated postfix
    """
    stack = []
    
    if postfix == 'Only numbers allowed' or postfix == 'Invalid Input':
        return ''
    # Keep the instructions below with your code.
    # implement as directed
    #• Repeat
    for x in postfix:
        #• If operand, push onto stack
        if str(x).isdigit():
            dig = float(x)
            stack.append(dig)
        #Checks for whether the postfix input is an operator and calculates as needed
        elif x == '*':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 * val1)
        elif x == '/':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 / val1)
        elif x == '+':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 + val1)
        elif x == '-':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 - val1)

    """Returns the last value in the stack, aka the evaluated value. Also checks to make sure all nums evaluated.
    Prevents inputs such as (3)3-2 so that an operator must be present to work"""
    if len(stack) == 1:
        result = stack.pop()
        result_str = f"Result = {result:.2f}\n"
        return result_str
    else:
        return 'Invalid Input\n'
        
def main():
    """
    Main function that calls the previous functions, as well as creates the prompt message and the loop to continually accept inputs
    """
    #Loops and asks for equations to evaluate until q is entered
    print("Enter equation you want evaluated using '*, /, +, -' operators. Enter q to quit.\n")
    infix = input("Input: ")
    while infix != 'q':
        postfix = convert(infix)
        result = evaluate(postfix)

        if result != 'Invalid Input':
            print(f"Postfix: {postfix}")
            print(result)
        else:
            print(result)

        print("Enter equation you want evaluated using '*, /, +, -' operators. Enter q to quit\n")
        infix = input("Input: ")


if __name__ == '__main__':
    main()
