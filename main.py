import random
import string

def generate_password(length=12):
    # Define the character set: uppercase + lowercase + digits + punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Run the App
print("🔐 Password Generator")

try:
    user_length = int(input("Enter password length (e.g. 8, 12, 16): "))
    if user_length < 4:
        print("Password should be at least 4 characters long.")
    else:
        password = generate_password(user_length)
        print(f"\nYour secure password is:\n➡️ {password}")
except ValueError:
    print("Please enter a valid number.")
