import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

create_directory("code")  # Directory for source code
create_directory("tests")  # Directory for test cases

# Additional code to be executed in the directory below "code"
