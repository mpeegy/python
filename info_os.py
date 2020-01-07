import os

print(os.getcwd(), "\n")

for item in os.environ:
    print(item, os.environ[item])


