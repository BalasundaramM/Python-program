# Input is an array of strings of an arithmetic expression. Calculate the value.
# eg - input ["1", "2", "+", "5", "*"]
# output =  15
# explanation (1 + 2) * 5 = 15

# input ["10", "2", "3", "+","-", "5", "*"]
# output =  25
# explanation (10 - ( 2 + 3)) * 5 = 25
# Hint : Use the concept of stack. Push and pop. 
# Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
# operator, pop two elements from the stack, apply the operation and push the result back.


def arithmetic_stack(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for element in expression:
        if element not in operators:
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == '+':
                result = operand1 + operand2
            elif element == '-':
                result = operand1 - operand2
            elif element == '*':
                result = operand1 * operand2
            elif element == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack.pop()

stack_1 = ["1", "2", "+", "5", "*"]
op_stack1=arithmetic_stack(stack_1)
print(f'output 1 = {op_stack1}') 

stack_2 = ["10", "2", "3", "+", "-", "5", "*"]
op_stack2=arithmetic_stack(stack_2)
print(f'output 2 = {op_stack2}') 