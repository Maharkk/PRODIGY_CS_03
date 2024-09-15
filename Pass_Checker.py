import re

def check_password_strength(password):
    # Initialize the strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check the overall strength based on the criteria
    if all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]):
        return "Strong password!"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (number_criteria or special_char_criteria):
        return "Moderate password!!"
    else:
        return "Weak password!!!"

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
