#importing main functionality
import hashlib
import os.path

#calculating MD5
def calculate_checksummd5(filename):
    with open(filename, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()
        
#calculating SHA-1
def calculate_checksum1(filename):
    with open(filename, 'rb') as file:
        return hashlib.sha1(file.read()).hexdigest()

#calculating SHA-256
def calculate_checksum256(filename):
    with open(filename, 'rb') as file:
        return hashlib.sha256(file.read()).hexdigest()

#description
print('\nThis Python Script will calculate Checksums (MD5, SHA-1, SHA-256) for a given file.\n'
'Input path to file below\n')

#User will input path here
path = str(input('>>>'))

#checking if path is correct and leads to a file
try:
    calculate_checksum1(path)
#error-handling if path to file incorrect or not found
except (FileNotFoundError, SyntaxError, NameError):
    print('File not found! Please check the path!')
#printing output
else:
    print('\nMD5 Checksum:')
    md5 = (calculate_checksummd5(path))
    print(md5)
    print('\nSHA-1 Checksum:')
    sha1 = (calculate_checksum1(path))
    print(sha1)
    print('\nSHA-256 Checksum:')
    sha256 = (calculate_checksum256(path))
    print(sha256)
