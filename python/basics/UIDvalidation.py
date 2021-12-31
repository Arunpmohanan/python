"""ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks."""

UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
DIGITS    = '0123456789'
ALPHA     = UPPERCASE + LOWERCASE + DIGITS

def valid(uid):
    return (
        two_ucase(uid)        # must contain at least 2 uppercase characters
        and three_digits(uid) # must contain at least 3 digits
        and only_alpha(uid)   # must contain only alphanumeric characters
        and no_repeats(uid)   # no character should repeat
        and ten_chars(uid)    # must be exactly 10 characters long
    )

def two_ucase(uid):    
   return sum(1 for i in uid if i in UPPERCASE) >= 2

def three_digits(uid):
    return sum(1 for i in uid if i in DIGITS) >= 3

def only_alpha(uid):    
    return all(i in ALPHA for i in uid)

def no_repeats(uid):
    return len(set(uid)) == len(uid)

def ten_chars(uid):
    return len(uid) == 10


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print('Valid' if valid(input()) else 'Invalid')
   