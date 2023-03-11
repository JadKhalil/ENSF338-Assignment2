from stack import Stack
import sys


def calculateResult(postfix):

    postfixStack = Stack()

    operandSet = {'+', '-', '*', '/'}

    for i in range(len(postfix)):
        if postfix[i] == '(' or postfix[i] in operandSet:
            postfixStack.push(postfix[i])
        elif postfix[i] == ')':
            num1 = postfixStack.pop()
            num2 = postfixStack.pop()
            operator = postfixStack.pop()
            postfixStack.pop()
            result = eval(str(num2) + operator + str(num1))
            postfixStack.push(result)
        elif postfix[i] != ' ':
            postfixStack.push(postfix[i])
    return postfixStack.pop()


if __name__ == "__main__":
    x = calculateResult(sys.argv[1])
    print(x)
