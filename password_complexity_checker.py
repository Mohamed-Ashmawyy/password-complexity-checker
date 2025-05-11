import re

def check_password_strength(password):
    score = 0
    feedback = []

    # length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # uppercase letter check
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # lowercase letter check
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # digit check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    # special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def display_result(strength, feedback):
    print("\nPassword strength:", strength)
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")
    print("-" * 40)

def main():
    print("Welcome to the Password Strength Checker\n")

    while True:
        user_input = input("Enter a password (or 'exit' to quit): ").strip()

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        strength, feedback = check_password_strength(user_input)
        display_result(strength, feedback)

if __name__ == "__main__":
    main()
