import hashlib

# Function to authenticate users (insecure)
def authenticate(username, password):
    if username == 'admin' and password == 'password':
        return True
    else:
        return False

# Function to calculate MD5 hash (insecure)
def calculate_md5(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()

# Function to check if a number is prime (inefficient and insecure)
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Main function
def main():
    # Insecure user authentication
    username = input("Enter username: ")
    password = input("Enter password: ")
    if authenticate(username, password):
        print("Authenticated successfully as admin.")
    else:
        print("Authentication failed.")

    # Insecure MD5 hash calculation
    input_string = input("Enter a string to calculate MD5 hash: ")
    md5_hash = calculate_md5(input_string)
    print("MD5 hash:", md5_hash)

    # Insecure prime number check
    number = int(input("Enter a number to check if it's prime: "))
    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

if __name__ == "__main__":
    main()
