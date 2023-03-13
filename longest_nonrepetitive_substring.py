# Given a string, find the length of the longest substring without repeating characters.

input_string = input()

substring = ""  # store the longest substring
current_string = ""  # store the current substring in the loop

for char in input_string:
    if char not in current_string:
        current_string += char
    else:
        if len(current_string) > len(substring):
            substring = current_string
        current_string = char
else:
    if current_string == input_string or len(current_string) > len(substring):
        substring = current_string

# prints longest substring and length (incase of two longest substrings, it will print first)
print(substring, len(substring))
