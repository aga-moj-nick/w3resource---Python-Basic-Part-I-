# 84. Write a Python program to count the number occurrence of a specific character in a string.



count = 0

string = 'aaabbbbbbaaaaallllapapapa'
literka = 'a'



for i in string:
    if i == literka:
        count += 1

print(count)
