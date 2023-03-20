# Given a list of numbers,
# find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

# take list as input
# input_list = input().split()
# input_list = [int(x) for x in input_list]
# input_list.sort()
# sq_list = [x**2 for x in input_list]


input_list = [2, 5, 12, 4, 14, 25, 7, 24]
input_list.sort()
sq_list = [x**2 for x in input_list]

for i, x in enumerate(sq_list[:len(sq_list)-2]):
    j = i
    for y in sq_list[i+1:len(sq_list)-1]:
        j += 1
        if x + y in sq_list[j:]:
            print('True')
            break
    else:
        continue

    break
else:
    print('False')

