# Task 1: Command Parser
# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.
request = input("How can I help you today?: ").lower()

if "help" in request:
    print("I am here to help.")
if "contact support" in request:
    print("I will connect you with someone who can help")
if "issue" in request:
    category = input("Can you give me more details? ").lower()
    print("login") if "login" in category else print("performance") if "performance" in category else print("error") if "error" in category else print("Issue Unknown")
else:
    print("Error")

# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.

