# Rezoan Hossain
# IS 211
# Assignment 14

def fibonnaci(n):
    # returns the nth Fibonacci number using recursion
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    # returns the greatest common divisor using recursion
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
    # compares two strings recursively

    # if both strings are empty, they are equal
    if s1 == "" and s2 == "":
        return 0

    # if first string is empty, it is smaller
    if s1 == "":
        return -1

    # if second string is empty, first is bigger
    if s2 == "":
        return 1

    # compare first character
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])

    # if first characters are same, compare rest of string
    return compareTo(s1[1:], s2[1:])