from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice
import sys


def password_generator(length=16, lower_case=True, upper_case=True, _digits=False, symbols=False):
    vocabulary = f"{ascii_lowercase if lower_case else ''}" \
                 f"{ascii_uppercase if upper_case else ''}" \
                 f"{digits if _digits else ''}" \
                 f"{punctuation if symbols else ''}"
    password = ''
    for _ in range(length):
        password += choice(vocabulary)
    return password


# class PasswordGenerator:
#     def __init__(self, length=16, lower_case=True, upper_case=True, _digits=False, symbols=False):
#         self.length = length
#         self.vocabulary = f"{ascii_lowercase if lower_case else ''}" \
#                           f"{ascii_uppercase if upper_case else ''}" \
#                           f"{digits if _digits else ''}" \
#                           f"{punctuation if symbols else ''}"
#
#     def generator(self):
#         password = ''
#         for _ in range(self.length):
#             password += choice(self.vocabulary)
#         return password
