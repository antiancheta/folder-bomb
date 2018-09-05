# Import os module and random module
import os, random
# Define an array fileNames with random characters
fileNames = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# Define a variable that is a concatenation of random choices in that array
fileName = random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames) + random.choice(fileNames)
# Make as many folders as we can
os.system("mkdir " + random.choice(fileName))
