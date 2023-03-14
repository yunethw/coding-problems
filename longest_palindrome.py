# A palindrome is a sequence of characters that can be read both forward and backwards.
# eg: racecar
# Given a string, s, find the longest palindromic substring in s

# The method I chose to detect a palindrome is based on the fact that in the middle of any palindrome
# we can find either 3 letters in the form of 'aba' or two letter in the form of 'aa'.
# From there onwards we can expand the selection in both sides to check if it is still a palindrome or not

s = input()
palindrome = ''  # starting value

# check 3 chars for palindrome eg: racecars -> cec
for i in range(len(s)-2):
    chars = s[i:i+3]
    if chars == chars[::-1]:
        temp, j = chars, 1
        while i > 0 and i - j >= 0:
            chars = s[i-j:i+3+j]  # expanding selection of chars
            if chars == chars[::-1]:
                temp = chars
            elif len(temp) > len(palindrome):
                palindrome = temp
            else:
                break
            j += 1
        else:
            if len(temp) > len(palindrome):
                palindrome = temp

# check 2 chars for palindrome eg: million -> ll
for i in range(len(s)-1):
    chars = s[i:i+2]
    if chars[0] == chars[1]:
        temp, j = chars, 1
        while i > 0 and i - j >= 0:
            chars = s[i-j:i+2+j]  # expanding selection of chars
            if chars == chars[::-1]:
                temp = chars
            elif len(temp) > len(palindrome):
                palindrome = temp
            else:
                break
            j += 1
        else:
            if len(temp) > len(palindrome):
                palindrome = temp

print(palindrome)

# Test Strings
# racecars (racecar)
# deified
# civical (civic)
# kayaking (kayak)
# civicalago (civic)
# rtjloljtrbhwkmvskmwhbrtjlojltr (rtjloljtr)
# okmbalxyzzyxlamclddiyclmbmkoa (alxyzzyxla)


