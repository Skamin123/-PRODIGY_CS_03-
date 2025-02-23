import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f" - {item}")

if __name__ == "__main__":
    main()
