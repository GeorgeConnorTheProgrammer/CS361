from pathlib import Path
destination= input("Enter your indented destination: ")

file1 = Path('destination.txt')
file1.touch(exist_ok=True)

myfile = open("destination.txt", 'w')

myfile.write(destination)