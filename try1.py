class InvalidAgeError(Exception):
    pass


age=1


try:
    if age<0:
        raise InvalidAgeError("Age cannot be negative")
except InvalidAgeError as e:
    print(e)
else:
    print("Valid age:",age)