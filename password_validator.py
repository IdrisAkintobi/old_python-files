import re

# Without regular expression
symbols = {'!', '@', '#', '$', '%', '&', '*', }
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def pass_check(password):
    password_set = set(password)
    if password and len(password) >= 7 and len(password_set & symbols) >= 1 and len(password_set & numbers) >= 1:
        return "Strong"
    return "Weak"


# Using regular expression
pattern1 = re.compile(r'[!@#$%&*]')
pattern2 = re.compile(r'[0-9]')


def pass_validator(password=input("Enter password: ")):
    if len(password) > 6:
        if len(pattern1.findall(password)) >= 1 and not len(pattern2.findall(password)) >= 1:
            return("Medium")
        elif len(pattern2.findall(password)) >= 1 and not len(pattern1.findall(password)) >= 1:
            return("Medium")
        elif len(pattern1.findall(password)) >= 1 and len(pattern2.findall(password)) >= 1:
            return("Strong")
    return("Weak")


# print(pass_check(input("Enter Passphrase: ")))
# print(pass_validator())
