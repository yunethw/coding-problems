# Given a string, find the length of the longest substring without repeating characters

input_string = input()


def longest_nonrepetitive_substring(string):
    substring = ""  # store the longest substring
    current_string = ""  # store the current substring in the loop

    for char in string:
        if char not in current_string:
            current_string += char
        else:
            if len(current_string) > len(substring):
                substring = current_string
            current_string = char
    else:
        if current_string == string or len(current_string) > len(substring):
            substring = current_string

    return substring


result = longest_nonrepetitive_substring(input_string)
print(result, len(result))

# Test strings
# "hzfjlzhdgqlmntoyrqpp"
# "vmmjujwnkpgnawfuxxzt"
# "tyvtifbvyjzllbsyggnw"
# "qxzzpbjwnfjhslsyowgw"
# "tzmfrlssjydyysdxiidw"
