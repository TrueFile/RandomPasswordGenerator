from string import ascii_lowercase, ascii_uppercase, digits as _digits, punctuation
from random import choice
import sys


# Solution using the function
def password_generator(length=16, lower_case=True, upper_case=False, digits=False, symbols=False):
    vocabulary = f"{ascii_lowercase if lower_case else ''}" \
                 f"{ascii_uppercase if upper_case else ''}" \
                 f"{_digits if digits else ''}" \
                 f"{punctuation if symbols else ''}"
    password = ''   # Password assembly
    try:
        for _ in range(length):
            password += choice(vocabulary)
    except IndexError:
        print('Error: ', 'No parameters! There is nothing to generate a password.')
    return password

# First solution using the class
# class PasswordGenerator:
#     def __init__(self, length=16, lower_case=True, upper_case=True, digits=False, symbols=False):
#         self.length = length
#         self.vocabulary = f"{ascii_lowercase if lower_case else ''}" \
#                           f"{ascii_uppercase if upper_case else ''}" \
#                           f"{_digits if digits else ''}" \
#                           f"{punctuation if symbols else ''}"
#
#     def generator(self):
#         password = ''
#         for _ in range(self.length):
#             password += choice(self.vocabulary)
#         return password


if __name__ == '__main__':
    print(password_generator(length=8, lower_case=False, upper_case=True, digits=True, symbols=False))      # test? ;d
