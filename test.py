import os
import subprocess
import pickle

def run_eval():
    user_input = input("Enter something: ")
    print(eval(user_input))

def list_files():
    filename = input("Enter filename: ")
    os.system(f"cat {filename}")

def load_data(data):
    return pickle.loads(data)

run_eval()
list_files()c
