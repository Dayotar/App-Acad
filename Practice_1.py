# Andrew's Solutions

# Problem 1

def reverse(string):

    new_string = ""
    for index in range(1, len(string) + 1):
        new_string = new_string + string[-index]
    return new_string

print(reverse("five"))

# Problem 2

def factorial(integer):
    
    total = 1

    if integer == 0:
        return 1
    else:
        for index in range(integer):
            total = total * (integer - index)
    return total

print(factorial(6))

# Problem 3

def longest(string):

    temp_list = string.split()
    longest = ""
    for item in temp_list:
        if longest == "":
            longest = item
        else:
            if len(item) > len(longest):
                longest = item

    return longest

print(longest("abc def abcde"))

# Problem 4

def sum_num(integer):

    total = 0
    for item in range(1, integer + 1):
        total += item

    return total

print(sum_num(5))

# Problem 5

def time_conversion(minutes):

    final_mins = minutes % 60
    hours = minutes // 60
    if final_mins < 10:
        final_mins = "0" + str(final_mins)
    if final_mins == 0:
        final_mins = "00"
    return "'" + str(hours) + ":" + str(final_mins) + "'"

print(time_conversion(125))

# Problem 6

def vowels(string):

    total = 0
    vowels = ["a", "i", "e", "o", "u"]
    for letter in string:
        if letter in vowels:
            total += 1
    return total

print(vowels("amino"))

# Problem 7

def palindrome(string):

    if string == reverse(string):
        return True
    else:
        return False

print(palindrome("dadad"))

# Problem 8

def nearby(string):

    count = 0
    for letter in string:
        if letter == "a":
            if "z" in string[count: count + 3]:
                return True
        count += 1
    return False

print(nearby("baeeeeez"))

# Problem 9

def two_sum(num_list):

    first = 0
    second = 0
    for number_1 in num_list:
        for number_2 in num_list:
            if number_1 + number_2 == 0:
                return [first, second]
            second += 1
        first += 1
        second = 0
    return "nil"

print(two_sum([1, 3, 5, -5]))

# Problem 10

def power_2(number):

    for index in range(number - 1 // 2):
        if 2 ** index == number:
            return True
    return False

print(power_2(64))

# Problem 11

def third_greatest(num_list):
    
    first = float('Inf')
    second = float('Inf')
    third = float('Inf')

    for item in num_list:
        if item < first:
            third = second
            second = first
            first = item
        elif item < second:
            third = second
            second = item
        elif item < third:
            third = item
    print(first, second, third)

    return third

print(third_greatest([1, 3, 7, 4]))

# Problem 12

def common(string):

    count = 0
    temp_count = 0
    letter = ""

    for first in string:
        for second in string:
            if first == second:
                temp_count += 1
        if temp_count > count:
            count = temp_count
            letter = first
        temp_count = 0

    return [letter, count]

print(common("abbaaab"))

# Problem 13

def dasherize(number):

    new_string = "-"
    num = str(number)
    for item in num:
        if int(item) % 2 == 1:
            if new_string[-1] != "-":
                new_string += "-" + item + "-"
            else:
                new_string += item + "-"
        else:
            new_string += item
    if new_string[-1] == "-":
        new_string = new_string[:-1]
    if new_string[0] == "-":
        new_string = new_string[1:]

    return new_string

print(dasherize(203))

# Problem 14

def capitalize(string):

    new_string = ""
    split_list = string.split()
    for item in split_list:
        new_string = new_string + item[0].upper() + item[1:] + " "
    return new_string[:-1]

print(capitalize("this is a sentence"))

# Problem 15

def scramble(string, array):

    new_string = ""
    for item in array:
        new_string += string[item]

    return new_string

print(scramble("markov", [5, 3, 1, 4, 2, 0]))

# Problem 16

def prime(integer):

    count = 0
    for number in range(1, integer + 1):
        if integer % number == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

print(prime(7))

# Problem 17

def nth_prime(number):

    import sys

    count = 0
    for num in range(2, sys.maxsize):
        if prime(num) == True:
            count += 1
            if count == number:
                return num

print(nth_prime(100))

# Problem 18

def longest_pal(string):

    length = 0
    pal = ""
    
    for index in range(len(string) + 1):
        for second_index in range(len(string) + 1):
            test = string[index:second_index]
            if palindrome(test) == True and len(test) > length:
                length = len(test)
                pal = test

    return [pal, length]

print(longest_pal("abcbd"))

# Problem 19

def gcf(num_1, num_2):

    max = num_1
    if num_2 > num_1:
        max = num_2

    gcf = 0

    for number in range(1, max + 1):
        if num_1 % number == 0 and num_2 % number == 0:
            gcf = number

    return gcf

print(gcf(16, 24))

# Problem 20

def caesar(offset, string):

    new_string = ""

    for item in string:
        if item.isalpha():
            asc = ord(item)
            if asc + offset < 123:
                asc = asc + offset
            else:
                asc = ord(item) - (26 - offset)
            new_string += chr(asc)
        else:
            new_string += item

    return new_string

print(caesar(3, "abc xyz"))

# Problem 21

def repeated(string):

    count = 0
    temp_list = []
    temp_list_2 = []

    for item in string:
        if item not in temp_list:
            temp_list.append(item)
        elif item in temp_list and item not in temp_list_2:
            temp_list_2.append(item)
            count += 1

    return count

print(repeated("cadac"))