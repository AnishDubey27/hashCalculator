# Cryptographic Hash Calculator
This Python script is a Cryptographic Hash Calculator that allows users to calculate the cryptographic hash of input data using specified algorithms such as MD5, SHA-1, or SHA-256.

## Usage
To use the Cryptographic Hash Calculator, follow these steps:

Run the script in a Python environment.
Follow the prompts to input data to hash and choose the hashing algorithm.
Input "end" to exit the program.
Functionality
The script consists of the following main components:

calculate_hash(data, algorithm): This function calculates the cryptographic hash of the input data using the specified algorithm. It takes two parameters:

data (str): The input data to be hashed.
algorithm (str): The hashing algorithm to use ('md5', 'sha1', 'sha256', etc.).
It returns the hexadecimal representation of the hash.
main(): This function contains the main execution logic of the program. It prompts the user to input data and choose the hashing algorithm. It then calculates and prints the hash value using the specified algorithm. The program continues to run until the user inputs "end" to exit.

## Supported Algorithms
The script supports the following hashing algorithms:

MD5
SHA-1
SHA-256
and more, based on the hashlib library in Python.
Requirements
This script requires Python 3.1 and the hashlib library.

## Example
Here's an example of how to use the Cryptographic Hash Calculator:
```
Welcome to the Cryptographic Hash Calculator!
Enter the data to hash (type 'end' to exit): Hello, world!
Choose the hashing algorithm (e.g., md5, sha1, sha256): md5
The MD5 hash of 'Hello, world!' is: 6cd3556deb0da54bca060b4c39479839
Enter the data to hash (type 'end' to exit): end
```
