import os
import sqlite3
import subprocess
import pickle

# 1. Hardcoded secret (SAST)
import os

API_KEY = os.getenv("API_KEY")

# 2. SQL Injection vulnerability (SAST)
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)  # vulnerable
    return cursor.fetchall()

# 3. Command Injection (SAST)
def run_command(user_input):
    os.system("echo " + user_input)  # vulnerable

# 4. Insecure subprocess usage (SAST)
def run_process(cmd):
    subprocess.call(cmd, shell=True)  # vulnerable

# 5. Insecure deserialization (SAST)
def load_data():
    with open("data.pkl", "rb") as f:
        return pickle.load(f)  # vulnerable

# 6. Weak random usage
import random
def generate_token():
    return str(random.random())  # not secure

# 7. Debug mode (bad practice)
DEBUG = True

if __name__ == "__main__":
    print("Running vulnerable app...")
    get_user("admin' OR '1'='1")
    run_command("test")query = f"SELECT * FROM users WHERE username = '{username}'"

