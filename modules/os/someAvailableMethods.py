import os

print("Current Working Directory")
print(os.getcwd())
print("\n")

print("Change Current Working Directory with : os.chdir('../')")
os.chdir('../')
print(os.getcwd())
print("\n")