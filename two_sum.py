# Given a list of numbers, and a target number k.
# Return whether there are two numbers in the list that add up to k.
# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return True since 4 + 1 = 5.

# input format : a b c d -> ['a', 'b', 'c', 'd']
num_list = input('list: ').split(sep=' ')
k = int(input('k = '))
num_list = [int(x) for x in num_list]

for i in num_list:
    if (k - i) in num_list:
        print('True')
        break
else:
    print('False')


