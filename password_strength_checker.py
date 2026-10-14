import re  #Calling the regex (Regular Expressions) library which searches for patterns inside text

# Common weak passwords list
weak_passwords = [
    "password", "123456", "qwerty", "letmein", "admin",
    "welcome", "iloveyou", "abc123", "monkey", "dragon"
]  #This is a list of the most common weak passwords attackers often try

# Simple dictionary words for detection
dictionary_words = [
    "hello", "love", "sun", "moon", "star", "computer",
    "security", "football", "secret", "name"
]  #Small list of simple dictionary words to detect easy content

def check_password_strength(password):  #This def function checks the strength of a given password
    score = 0  #The password strength score begins at 0 and is stored in the variable called 'score'
    feedback = []  #The empty list called 'feedback' stores recommendations

    # Length check
    if len(password) >= 12:  #If the password length is 12 or more
        score += 2  #Two points are added for strong length to the score variable
    elif len(password) >= 8:  #Otherwise if the length  is at least 8
        score += 1  #One point is added for acceptable length
    else:  #Else if the length is less than 8
        feedback.append("Password is too short (minimum 8 characters).")  #This message is output to warn the user that the password length is too short

    # Character variety
    if re.search(r"[A-Z]", password):  #If the password contains at least one uppercase letter
        score += 1  #One point is added for having an uppercase letter
    else:  #Else if there are no uppercase letters found
        feedback.append("Add uppercase letters.")  #This message is output to suggest adding uppercase letters to the user

    if re.search(r"[a-z]", password):  #Checks if the password contains at least one lowercase letter
        score += 1  #One point is added if lowercase letter is present
    else:  #Else if no lowercase letters are found
        feedback.append("Add lowercase letters.")  #This message is output to suggest using lowercase letters

    if re.search(r"[0-9]", password):  #Checks if the password contains at least one digit
        score += 1  #One point is added for having numbers
    else:  #Else if no numbers are found
        feedback.append("Add numbers.")  #This message is output to suggest adding numbers

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  #Checks if the password contains at least one special character
        score += 1  #One point is added for special characters
    else:  #Else if no special characters are present
        feedback.append("Add special characters.")  #This message is output to suggest using special characters

    # Weak password check
    if password.lower() in weak_passwords:  #Checks if the password matches any of the known weak passwords (case-insensitive)
        feedback.append("This is a commonly used weak password.")  #This message is output to warn the user that the password is very weak

    # Dictionary word check
    for word in dictionary_words:  #Loops through each dictionary word
        if word in password.lower():  #Checks if the word appears in the password (case-insensitive)
            feedback.append(f"Contains dictionary word: '{word}'")  #This message is output to warn the user that the password is an easy word
            break  #Stop checking after the first match

    # Final rating
    if score <= 3:  #If the total score is 3 or less
        strength = "Weak"  #Set strength label to Weak
    elif score <= 5:  #If the score is 4 or 5
        strength = "Medium"  #Set the strength label to Medium
    else:  #If the score is 6 or more
        strength = "Strong"  #Set the strength label to Strong

    return strength, feedback  #Return both the strength label and the feedback list


# Main program
password = input("Enter a password to check: ")  #Ask the user to input a password
strength, feedback = check_password_strength(password)  #Calls the function and get strength and feedback

print(f"\nPassword Strength: {strength}")  #Output the strength of the password

if feedback:  #If there are any feedback messages
    print("\nRecommendations:")  #Print a heading for recommendations
    for item in feedback:  #Loop through each feedback message
        print(f"- {item}")  #Print each recommendation with a bullet
else:  #If there is no feedback as the password passed all checks
    print("Your password looks strong!")  #Output this message to tell the user their password is strong

