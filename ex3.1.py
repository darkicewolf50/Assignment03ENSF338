import sys

# Define the operators
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

# Define a stack data structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Define a stack-based interpreter function
def evaluate(expression):
    stack = Stack()
    for token in expression.split():
        print(f'print1 {token}')
        if token in operators:
            # Push the operator onto the stack
            stack.push(token)
        elif token.isdigit():
            # If the token is a digit, push it onto the stack as an integer
            stack.push(int(token))
        elif token == ')':
            # Pop the top operator and the two top operands from the stack
            operand1 = stack.pop()
            print(operand1)
            operand2 = stack.pop()
            print(operand2)
            operator = stack.pop()
            print(operator)
            # Apply the operator to the operands and push the result onto the stack
            result = operators[operator](operand1, operand2)
            stack.push(result)
        # Ignore open parentheses
        elif token == '(':
            pass
    # The final result is the top element of the stack
    return stack.pop()


# Get the expression from the command line argument
expression = sys.argv[1]

# Remove the first and last parentheses
parsed_expression = expression[1:-1].split()

# Evaluate the expression and print the result
result = evaluate(' '.join(parsed_expression))
print(f'result: {result}')

