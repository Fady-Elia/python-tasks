def isBalanced(s):
    stack = []  # create an empty stack to keep track of opening brackets
    for bracket in s:  # iterate through each bracket in the string
        if bracket in ["(", "[", "{"]:  # if it's an opening bracket, push it onto the stack
            stack.append(bracket)
        elif bracket in [")", "]", "}"]:  # if it's a closing bracket, check if it matches the top element of the stack
            if len(stack) == 0:  # if the stack is empty, the brackets are not balanced
                return "NO"
            top = stack.pop()  # pop the top element of the stack
            if (bracket == ")" and top != "(") or \
               (bracket == "]" and top != "[") or \
               (bracket == "}" and top != "{"):  # if the closing bracket doesn't match the corresponding opening bracket, the brackets are not balanced
                return "NO"
    if len(stack) == 0:  # if the stack is empty at the end of the iteration, the brackets are balanced
        return "YES"
    else:
        return "NO"


n = int(input())  # read the number of strings
for i in range(n):
    s = input()  # read each string of brackets
    print(isBalanced(s))  # print "YES" or "NO" depending on whether the brackets are balanced or not
