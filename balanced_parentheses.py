# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

# ((())) -> True
# [()]{} -> True
# ({[)] or (( or ()[} -> False

s = input()
open_brackets = ['(', '{', '[']
b_list = []

for b in s:
    if b in open_brackets:
        b_list.append(b)
    else:
        try:
            bracket = b_list.pop()
            match bracket:
                case '(':
                    if b != ')':
                        print('False')
                        break
                case '{':
                    if b != '}':
                        print('False')
                        break
                case '[':
                    if b != ']':
                        print('False')
                        break
                case _:
                    print("Invalid String")
                    break
        except IndexError:
            print('False')
            break
else:
    if len(b_list) != 0:
        print('False')
    else:
        print('True')
