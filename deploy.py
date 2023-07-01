import os
# import shutil
# import imgkit
import time
import msvcrt
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--no-build', action='store_true', help='skip the build step')
args = parser.parse_args()

# Build the React app if --no-build is not specified
if not args.no_build:
    # Back to root directory
    os.system('cd .. && cd .. && cd ..')

    # Build the React app - includes eslint and jest per package.json
    os.system("npm run build")

def get_commit_message(timeout=30):
    start_time = time.time()
    message = ""
    while True:
        if msvcrt.kbhit():  # Check if a key has been pressed
            char = msvcrt.getwche()  # Read a character without waiting for a newline
            if char == '\r':  # If the Enter key was pressed, exit the loop
                break
            message += char  # Append the character to the message
        elif time.time() - start_time > timeout:  # If the timeout has elapsed, exit the loop
            break
    if not message:
        message = "commit from deploy"  # Use default message if no input was received
    return message

print('Enter a commit message (optional, 30s timeout for "commit from deploy", careful no backspace!):')
commit_message = get_commit_message()
os.system(f'git add . && git commit -m "{commit_message}" && git push')