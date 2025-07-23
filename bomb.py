import os

def vulnerable_command_execution(user_input):
    # ❌ Never pass raw input to os.system
    os.system("echo You entered: " + user_input)
