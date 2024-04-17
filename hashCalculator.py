import hashlib

def calculate_hash(data, algorithm):
    """
    Calculate the cryptographic hash of data using the specified algorithm.
    
    Parameters:
        data (str): The input data to be hashed.
        algorithm (str): The hashing algorithm to use ('md5', 'sha1', 'sha256', etc.).
    
    Returns:
        str: The hexadecimal representation of the hash.
    """
    algorithm = algorithm.lower()  # Convert algorithm name to lowercase
    hasher = hashlib.new(algorithm)
    hasher.update(data.encode())
    return hasher.hexdigest()

def main():
    print("Welcome to the Cryptographic Hash Calculator!")

    while True:
        data = input("Enter the data to hash (type 'end' to exit): ")
        if data.lower() == 'end':
            break

        algorithm = input("Choose the hashing algorithm (e.g., md5, sha1, sha256): ").lower()

        if algorithm in hashlib.algorithms_available:
            hash_value = calculate_hash(data, algorithm)
            print(f"The {algorithm.upper()} hash of '{data}' is: {hash_value}")
        else:
            print("Invalid hashing algorithm!")

if __name__ == "__main__":
    main()
