import os

def insecure_function():
    password = "hardcoded_password"
    os.system("echo Running insecure command")  # vulnerable

if __name__ == "__main__":
    insecure_function()
