# Task 1: Input Length Validator
# Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

users_name = input("Please enter your first and last name: ")

length_of_name = len(users_name)

if length_of_name < 2:
    print("Error")
elif " " in users_name:
    print(length_of_name - 1)
else:
    print(length_of_name)


# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.
def password_checker(u_password):
    feedback = "Your password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number."
    if len(u_password) > 8 and not u_password.isalpha() and not u_password.islower() and not u_password.isupper():
        return "Password changed!"
    else:
        return feedback


password = input("Please enter a new password: ")
print(password_checker(password))


# Task 3: Email Formatter
# Implement a script that ensures all user email addresses are in a standard format
def email_formatter(user_email):
    return user_email.lower()


print(email_formatter("KelseaConrad19@gmail.com"))



